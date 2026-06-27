import datetime
import json
import pathlib
import signal
import subprocess
import sys
import threading
import time

import requests
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

BRIEF_PATH = "brief-latest.json"
STATE_PATH = "state.json"
BRIEF_SCRIPT = "brief.py"
PYTHON_EXE = r"C:\Users\RSky\AppData\Local\Programs\Python\Python314\python.exe"
JOURNAL_DIR = pathlib.Path(r"D:\Users\RSky\Desktop\AI.ProFit\rsky.crv\03-Journal\daily.brief")

API_KEY = "sk_6d8d327d4e4e414d9fbc0cbe4e44527abee5b0eb96e54fdc98be4ca68c1d253d"
SESSION_ID = "brief_analyst_rsky"
INTERVAL = 300  # seconds between brief.py runs

_running = False       # guard: prevents overlapping run_cycle calls
_run_timer = None      # debounce handle for file watcher


def call_asi(brief):
    response = requests.post(
        "https://api.asi1.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "x-session-id": SESSION_ID,
        },
        json={
            "model": "asi1",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are .brief — a Profit.OS gate evaluator.\n\n"
                        "ROLE: Return structured verdicts on assets. No capital allocation. "
                        "No position sizes. Verdicts are for Alan to action.\n\n"
                        "EVALUATION ORDER:\n\n"
                        "1. ELIGIBILITY GATE\n"
                        "   FAIL if: price null, vol/mcap >1000%, contract deprecated/migrated, no liquidity.\n"
                        "   FAIL → REJECT, state blocking condition. PASS → continue.\n\n"
                        "2. SIGNAL TIER\n"
                        "   SCALP — <72hr, price-action driven\n"
                        "   PORTFOLIO — thesis-driven, multi-week\n"
                        "   NOISE — narrative only, no data\n\n"
                        "3. EDS CLASS\n"
                        "   Fully Deterministic (85-100), High (70-84), Partial (50-69), "
                        "Fragile (25-49), Non-Deterministic (0-24)\n"
                        "   Synthetics default: Partial. Pre-listing: Non-Deterministic.\n\n"
                        "4. VERDICT\n"
                        "   EXECUTE — PASS, EDS ≥50, regime-aligned\n"
                        "   WATCHLIST — PASS, EDS <50 or misaligned\n"
                        "   RESEARCH STATE — thesis incomplete\n"
                        "   REJECT — FAIL or noise\n\n"
                        "5. ANOMALIES\n"
                        "   Flag only vol/mcap >1000%, null price, deprecated contract.\n"
                        "   Format: ANOMALY — [asset] — [condition] — [value]\n\n"
                        "OUTPUT PER ASSET:\n"
                        "Asset / Eligibility / Signal Tier / EDS Class / Verdict / Anomaly\n\n"
                        "CAPITAL ALLOCATION PROHIBITED. Role ends at verdict.\n\n"
                        "No macro_regime provided → state REGIME UNKNOWN, proceed without regime conditioning.\n"
                        "No JSON provided → evaluate the asset or question as stated.\n\n"
                        "SUMMARY VERDICT: After all assets, return ONE overall session verdict:\n"
                        "EXECUTE, WATCHLIST, RESEARCH_STATE, or REJECT — based on dominant signal."
                    ),
                },
                {
                    "role": "user",
                    "content": json.dumps(brief),
                },
            ],
        },
        timeout=30,
    )
    content = response.json()["choices"][0]["message"]["content"].strip()

    # v1.3 returns full structured output per asset + a SUMMARY VERDICT line at the end.
    # Parse bottom-up to find the first verdict token in the response.
    for line in reversed(content.splitlines()):
        line_upper = line.strip().upper()
        for token in ["EXECUTE", "WATCHLIST", "RESEARCH_STATE", "REJECT"]:
            if token in line_upper:
                return token

    # Fallback: no verdict token found — return truncated content for diagnosis
    return content[:80]


def update_state(verdict, brief_file):
    # 1. Machine-readable state
    state = {
        "last_brief": brief_file,
        "verdict": verdict,
        "timestamp": time.time(),
    }
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

    # 2. Human-readable report — appended to brief-report.md (Obsidian-readable)
    now = datetime.datetime.now()
    try:
        with open(brief_file, "r", encoding="utf-8") as f:
            brief = json.load(f)
        scalp = ", ".join(brief.get("scalp_signals", [])[:3]) or "none"
        regime = brief.get("macro_regime", {}).get("classification", "UNKNOWN")
        liquidity = brief.get("macro_regime", {}).get("liquidity", "UNKNOWN")
    except Exception:
        scalp, regime, liquidity = "unavailable", "UNKNOWN", "UNKNOWN"

    # brief-report.md — rolling log in briefs directory
    report_path = pathlib.Path("brief-report.md")
    with open(report_path, "a", encoding="utf-8") as r:
        r.write(
            f"## {now.strftime('%Y-%m-%d %H:%M')}\n"
            f"**VERDICT:** {verdict}\n"
            f"**Regime:** {regime} | **Liquidity:** {liquidity}\n"
            f"**Top Scalp Signals:** {scalp}\n\n"
        )

    # 3. Obsidian daily note injection
    # Creates YYYY-MM-DD_daily.brief.md in 03-Journal/daily.brief/ if missing,
    # then appends a verdict block. One file per day, multiple cycles append cleanly.
    try:
        JOURNAL_DIR.mkdir(parents=True, exist_ok=True)
        date_str = now.strftime("%Y-%m-%d")
        daily_path = JOURNAL_DIR / f"{date_str}_daily.brief.md"

        # Write header only if file is new
        if not daily_path.exists():
            with open(daily_path, "w", encoding="utf-8") as d:
                d.write(f"# Daily Brief — {date_str}\n\n")

        # Append verdict block
        with open(daily_path, "a", encoding="utf-8") as d:
            d.write(
                f"## {now.strftime('%H:%M')}\n"
                f"**VERDICT:** {verdict}\n"
                f"**Regime:** {regime} | **Liquidity:** {liquidity}\n"
                f"**Top Scalp Signals:** {scalp}\n\n"
            )
    except Exception as e:
        pathlib.Path("daemon-error.log").open("a").write(
            f"{datetime.datetime.now()} JOURNAL ERROR: {e}\n"
        )




def run_cycle():
    global _running
    if _running:
        print("SKIP: cycle already running")
        return
    _running = True

    try:
        with open(BRIEF_PATH, "r", encoding="utf-8") as f:
            brief = json.load(f)

        verdict = call_asi(brief)

        if verdict not in ["EXECUTE", "WATCHLIST", "RESEARCH_STATE", "REJECT"]:
            print(f"INVALID VERDICT: {verdict!r} — defaulting to RESEARCH_STATE")
            verdict = "RESEARCH_STATE"

        update_state(verdict, BRIEF_PATH)
        print(f"VERDICT: {verdict}")

    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        _running = False  # always release guard


class BriefEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global _run_timer
        if "brief-latest.json" in event.src_path:
            # Debounce: Windows fires multiple events per write — collapse into one call
            if _run_timer is not None:
                _run_timer.cancel()
            _run_timer = threading.Timer(1.0, run_cycle)
            _run_timer.start()
            print("FILE EVENT: brief-latest.json updated — triggering evaluation")


def generate_brief():
    print("GENERATING: running brief.py")
    try:
        result = subprocess.run(
            [PYTHON_EXE, BRIEF_SCRIPT],
            capture_output=True,
            text=True,
            timeout=300,  # kill brief.py if it hangs beyond 5 min
        )
        if result.returncode != 0:
            pathlib.Path("daemon-error.log").open("a").write(
                f"{datetime.datetime.now()} BRIEF ERROR: {result.stderr}\n"
            )
        else:
            print("BRIEF: generated successfully")
    except subprocess.TimeoutExpired:
        pathlib.Path("daemon-error.log").open("a").write(
            f"{datetime.datetime.now()} TIMEOUT: brief.py exceeded 300s\n"
        )


def timer_loop():
    while True:
        generate_brief()   # writes brief-latest.json → fires file watcher → run_cycle()
        time.sleep(INTERVAL)


if __name__ == "__main__":
    observer = Observer()
    observer.schedule(BriefEventHandler(), path=".", recursive=False)
    observer.start()

    # Explicit signal handlers — catches SIGTERM (Task Scheduler shutdown)
    # without conflating it with KeyboardInterrupt from console control events
    def shutdown(signum, frame):
        observer.stop()
        sys.exit(0)

    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)

    try:
        timer_loop()
    except Exception as e:
        # Catch any unhandled exception — log and exit cleanly rather than crash-loop
        pathlib.Path("daemon-error.log").open("a").write(
            f"{datetime.datetime.now()} FATAL: {e}\n"
        )
        observer.stop()

    observer.join()
