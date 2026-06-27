# signal_audit_llm.py
# Offline analyst module — NOT in execution path.
# Reads event_log.jsonl + verdict history, produces audit_report_YYYY-MM-DD.md.
# Run manually or on scheduled daily trigger. No thresholds auto-updated.

import os
import json
import logging
import datetime
import requests
from pathlib import Path

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

BASE_DIR = Path(__file__).parent
EVENT_LOG   = BASE_DIR / "event_log.jsonl"
VERDICT_DIR = BASE_DIR
OUTPUT_DIR  = Path(r"D:\Users\RSky\Desktop\AI.ProFit\rsky.crv\00-Inbox\exports")

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_URL     = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL   = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = """You are a post-trade signal auditor for Profit.OS.

Your role:
- Detect contradictions between regime classification and asset verdicts
- Flag potential regime misclassification (asset behavior inconsistent with declared regime)
- Identify which scoring features drove verdicts (vol_accel, change_1h, flow)
- Surface recurring false positives or suppressed signals
- Recommend threshold or weight adjustments as suggestions ONLY

Output format:
## Contradiction Flags
## Regime Misclassification Candidates  
## Feature Importance Notes
## Threshold Recommendations (advisory only)
## Post-Trade Notes

Rules:
- No capital allocation decisions
- No EXECUTE/REJECT verdicts
- Advisory output only — human reviews before any config change
- Be concise. Flag anomalies. Skip noise."""


def _load_recent_events(n: int = 50) -> list:
    if not EVENT_LOG.exists():
        log.warning("event_log.jsonl not found")
        return []
    events = []
    with open(EVENT_LOG, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return events[-n:]


def _load_latest_verdict() -> dict:
    vpath = VERDICT_DIR / "verdict.json"
    if not vpath.exists():
        return {}
    try:
        return json.loads(vpath.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _load_shortlist() -> list:
    spath = VERDICT_DIR / "scalp-shortlist.json"
    if not spath.exists():
        return []
    try:
        return json.loads(spath.read_text(encoding="utf-8"))
    except Exception:
        return []


def _build_audit_payload(events: list, verdict: dict, shortlist: list) -> str:
    lines = []
    lines.append(f"AUDIT DATE: {datetime.date.today().isoformat()}")
    lines.append(f"EVENTS SAMPLED: {len(events)}")
    lines.append("")

    lines.append("=== LATEST VERDICTS ===")
    scalp = verdict.get("scalp_verdicts", {})
    for sym, v in scalp.items():
        lines.append(f"  {sym}: {v}")

    lines.append("")
    lines.append("=== SHORTLIST (last run) ===")
    for item in shortlist:
        lines.append(
            f"  {item.get('symbol','?')} | tier={item.get('tier','?')} "
            f"score={item.get('score','?')} regime={item.get('regime','?')} "
            f"flags={item.get('flags',[])} "
            f"vol_accel={item.get('vol_accel','?')} "
            f"change_1h={item.get('change_1h','?')}"
        )

    lines.append("")
    lines.append("=== RECENT EVENTS (last 50) ===")
    for e in events[-20:]:
        lines.append(f"  {json.dumps(e)}")

    return "\n".join(lines)


def _call_groq(payload: str) -> str:
    if not GROQ_API_KEY:
        return "ERROR: GROQ_API_KEY not set"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": payload},
        ],
        "max_tokens": 1500,
        "temperature": 0.2,
    }
    try:
        r = requests.post(GROQ_URL, headers=headers, json=body, timeout=30)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"ERROR: {e}"


def _write_report(content: str) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.date.today().isoformat()
    out_path = OUTPUT_DIR / f"audit_report_{date_str}.md"
    report = f"# Signal Audit Report — {date_str}\n\n{content}\n"
    out_path.write_text(report, encoding="utf-8")
    log.info(f"Audit report written: {out_path}")
    return out_path


def run_audit() -> None:
    log.info("signal_audit_llm: starting audit run")
    events   = _load_recent_events(50)
    verdict  = _load_latest_verdict()
    shortlist = _load_shortlist()

    if not events and not verdict:
        log.warning("No data available for audit — aborting")
        return

    payload  = _build_audit_payload(events, verdict, shortlist)
    analysis = _call_groq(payload)
    out_path = _write_report(analysis)
    print(f"\nAudit complete → {out_path}\n")
    print(analysis)


if __name__ == "__main__":
    run_audit()
