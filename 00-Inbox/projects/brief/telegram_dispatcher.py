"""
telegram_dispatcher.py — State-gated Telegram dispatcher for scalp_engine.py
Sends alerts only on material state change. Suppresses identical repeat signals.
"""

import json
import datetime
from pathlib import Path

# -- Paths ---------------------------------------------------------------------
_STATE_FILE = Path(__file__).parent / "last_sent_state.json"

# -- Hysteresis thresholds -----------------------------------------------------
ENTER_THRESHOLD = 45.0  # minimum score to send an ENTER signal
EXIT_THRESHOLD = 25.0  # score below this triggers EXIT signal
MIN_SCORE_DELTA = 2.0  # ignore resend unless score shifted by this much


# -- State I/O -----------------------------------------------------------------
def load_state() -> dict:
    if _STATE_FILE.exists():
        try:
            return json.loads(_STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_state(state: dict) -> None:
    _STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


# -- Signature -----------------------------------------------------------------
def _make_signature(symbol: str, score: float, tier: str, flags: list) -> dict:
    """Fingerprint of the signal state. Key on action only (ENTER_LONG, WATCH, EXIT)."""
    action = (
        "ENTER_LONG"
        if score >= ENTER_THRESHOLD
        else ("EXIT" if score < EXIT_THRESHOLD else "WATCH")
    )
    return {
        "symbol": symbol,
        "action": action,
    }


# -- Gate ----------------------------------------------------------------------
def should_send(symbol: str, score: float, tier: str, flags: list, state: dict) -> bool:
    """
    Returns True only when signal state has materially changed.
    Updates state in-place when True — caller must save_state() after dispatch.
    """
    sig = _make_signature(symbol, score, tier, flags)
    if state.get(symbol) == sig:
        return False
    state[symbol] = sig
    return True


# -- Formatter -----------------------------------------------------------------
def format_verdict(
    symbol: str, score: float, tier: str, f: dict, flags: list, regime: str
) -> str:
    """
    Actionable verdict card. Sent only on state change.
    Replaces format_summary() for signal dispatch.
    """
    emoji = {"T1": "\U0001f7e2", "T2": "\U0001f7e1", "RISK": "\U0001f534"}.get(
        tier, "\u26aa"
    )
    action = "ENTER_LONG" if score >= ENTER_THRESHOLD else "WATCH"

    lines = [
        f"{emoji} *{action} \u2014 {symbol}* `[{tier}]`",
        f"Score: `{score:.1f}` | Regime: `{regime}`",
        f"1h: `{f.get('change_1h', 0):+.2f}%` | "
        f"Vol Accel: `{f.get('vol_accel', 0):.2f}x` | "
        f"Flow: `{f.get('flow_strength', 0):+.2f}`",
        f"Liq: `${f.get('liquidity', 0):,.0f}` | "
        f"Pressure: `{f.get('liq_pressure', 0):.2f}`",
    ]
    if flags:
        lines.append("\u26a0\ufe0f " + " | ".join(flags))
    lines.append(f"_{datetime.datetime.now().strftime('%H:%M:%S')}_")
    return "\n".join(lines)


# -- Publisher -----------------------------------------------------------------
def publish_signal(
    symbol: str,
    score: float,
    tier: str,
    f: dict,
    flags: list,
    regime: str,
    state: dict,
    send_fn,
) -> bool:
    """
    Gate + dispatch with hysteresis. Returns True if message was sent.
    Holds ENTER_LONG until score drops below EXIT_THRESHOLD; ignores oscillation in between.
    Enforces tier-specific score floors: T1 ≥ 65, T2 ≥ 50, RISK bypasses.
    send_fn = scalp_engine.send_telegram (injected to avoid circular import)
    """
    # Tier-specific score floors
    tier_floors = {"T1": 65, "T2": 50, "RISK": 0}
    floor = tier_floors.get(tier, 50)
    prev_sig = state.get(symbol, {})
    prev_action = prev_sig.get("action", "WATCH")
    if prev_action == "ENTER_LONG" and score >= EXIT_THRESHOLD:
        return False  # hysteresis hold ? still above exit floor, suppress resend

    if tier != "RISK" and score < floor:
        return False  # below tier floor — suppress

    if score < ENTER_THRESHOLD and tier != "RISK":
        return False  # below action threshold — suppress
    if not should_send(symbol, score, tier, flags, state):
        return False  # no material change — suppress
    msg = format_verdict(symbol, score, tier, f, flags, regime)
    send_fn(msg)
    return True
