# bridge.py
# Execution kernel — single authority for all ASI:One calls.
# Daemon calls this. Nothing else should.
# Restored clean copy (fixed corrupted editor buffer)

import re
import json
import logging
import os
import requests
import datetime
from pathlib import Path

log = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent
PROMPT_FILE = BASE_DIR / "system-prompt-v1.3.md"
SCALP_PROMPT_FILE = BASE_DIR / "system-prompt-scalp-v1.0.md"
ALT_PROMPT_DIR = BASE_DIR / "asi1.ai"
ALT_PROMPT_FILE = ALT_PROMPT_DIR / "system-prompt-v1.3.md"
ALT_SCALP_PROMPT_FILE = ALT_PROMPT_DIR / "system-prompt-scalp-v1.0.md"


def _load_prompt_file(primary: Path, fallback: Path) -> str:
    try:
        return primary.read_text(encoding="utf-8")
    except FileNotFoundError:
        if fallback.exists():
            return fallback.read_text(encoding="utf-8")
        raise


def load_prompt() -> str:
    return _load_prompt_file(PROMPT_FILE, ALT_PROMPT_FILE)


_TG_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
_TG_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")


def _dispatch_scalp_verdicts(verdicts: dict, shortlist: list) -> None:
    """Dispatch EXECUTE verdicts to Telegram. Suppresses if no actionable signals."""
    if not _TG_TOKEN or not _TG_CHAT_ID:
        log.warning("Telegram not configured — skipping verdict dispatch")
        return

    execute = [sym for sym, v in verdicts.items() if v == "EXECUTE"]
    if not execute:
        log.info("SCALP ARBITRATION: no EXECUTE verdicts — suppressing push")
        return

    lines = ["🟢 *SCALP ARBITRATION — EXECUTE*\n"]
    for item in shortlist:
        sym = item["symbol"].upper()
        if sym not in execute:
            continue
        lines.append(
            f"`{sym}` score={item['score']} "
            f"1h={item['change_1h']:+.1f}% "
            f"acc={item['vol_accel']:.1f}x "
            f"dex={item['dex']}"
        )

    try:
        r = requests.post(
            f"https://api.telegram.org/bot{_TG_TOKEN}/sendMessage",
            json={
                "chat_id": _TG_CHAT_ID,
                "text": "\n".join(lines),
                "parse_mode": "Markdown",
            },
            timeout=10,
        )
        if not r.ok:
            log.warning(f"Telegram verdict push failed: {r.status_code} {r.text[:100]}")
    except Exception as e:
        log.error(f"Telegram verdict dispatch error: {e}")


def evaluate_verdict(asset: dict) -> str:
    """Pure gate logic for a single asset. No external calls.

    Rules:
    - regime must be exactly "RISK_ON" to proceed
    - any CRITICAL_FLAGS present -> REJECT
    - T1 with score>=65 -> EXECUTE
    - T2 with score>=50 -> WATCHLIST
    - otherwise -> REJECT

    Also normalizes `tier` when it's None (fixes JUP [None] bug).
    """
    regime = asset.get("regime", "UNKNOWN")
    score = asset.get("score", 0)
    tier = asset.get("tier") or ""
    flags = asset.get("flags") or []

    CRITICAL_FLAGS = {"REGIME_CONFLICT", "DATA_QUALITY", "LOW_LIQUIDITY"}

    if regime != "RISK_ON":
        return "REJECT"
    if flags and CRITICAL_FLAGS.intersection(set(flags)):
        return "REJECT"
    if tier == "T1" and score >= 65:
        return "EXECUTE"
    if tier == "T2" and score >= 50:
        return "WATCHLIST"
    return "REJECT"


def run_scalp(shortlist: list, api_key: str = "") -> dict:
    """Gate-based scalp arbitration. Replaces ASI:One — no external API calls.

    Expects `shortlist` to be a list of asset dicts containing at least
    `symbol`, `regime`, `score`, `tier`, and `flags` (scalp_engine normalizes these).
    """
    if not shortlist:
        log.warning("SCALP GATE: shortlist empty — skipping")
        return {}

    verdicts = {}
    for item in shortlist:
        sym = (item.get("symbol") or "").upper()
        if not sym:
            continue
        # Normalize tier/flags to avoid None values (fix JUP None tier bug)
        if item.get("tier") is None:
            item["tier"] = ""
        if item.get("flags") is None:
            item["flags"] = []

        verdict = evaluate_verdict(item)
        verdicts[sym] = verdict

    # Write verdict.json so other components can watch it
    verdict_path = Path(__file__).parent / "verdict.json"
    with open(verdict_path, "w", encoding="utf-8") as vf:
        json.dump(
            {"scalp_verdicts": verdicts, "ts": datetime.datetime.now().isoformat()},
            vf,
            indent=2,
        )
    log.info(f"verdict.json written — {len(verdicts)} assets")
    _dispatch_scalp_verdicts(verdicts, shortlist)
    return verdicts


# ASI:One pathway removed. Verdict extraction and heuristic parsing deleted in favor
# of deterministic gate logic implemented in `evaluate_verdict` above.
