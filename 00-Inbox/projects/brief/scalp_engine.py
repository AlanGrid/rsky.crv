"""
scalp_engine.py � Regime-based scalp signal scoring engine
Reads watchlist.json ? fetches DexScreener data ? scores ? ranks ? Telegram push

Data source: DexScreener API (free, no auth, covers all Solana DEX tokens)
  GET https://api.dexscreener.com/latest/dex/tokens/{mint}
  Returns: price, priceChange (m5/h1/h6/h24), volume (h1/h24), liquidity.usd

Architecture:
  - Stateless scoring function per asset
  - Modular feature-engine layer
  - Batch evaluation across full watchlist
  - 1-minute polling loop
  - T1/T2/Risk alerts via Telegram

Env vars required:
  TELEGRAM_BOT_TOKEN
  TELEGRAM_CHAT_ID
"""

import json
import logging
import os
import pathlib
import sys
import time
import datetime

import requests

sys.path.insert(0, str(pathlib.Path(__file__).parent / "rsky.profit_telegram.bot"))
from telegram_dispatcher import publish_signal, load_state, save_state

# -- Logging -------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-7s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("scalp-engine.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger(__name__)

# -- Config --------------------------------------------------------------------
TG_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TG_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")
POLL_INTERVAL = 60  # seconds between full watchlist scans
MIN_LIQUIDITY = 10_000  # USD � below this, skip scoring (manipulation risk)
WATCHLIST_PATH = pathlib.Path(__file__).parent / "watchlist.json"
SIGNAL_LOG = pathlib.Path(__file__).parent / "signal_log.jsonl"
BRIEF_PATH = pathlib.Path(__file__).parent / "brief-latest.json"
SHORTLIST_PATH = pathlib.Path(__file__).parent / "scalp-shortlist.json"

# Alert cooldown � prevents repeat alerts for same asset within window
_alert_cooldown: dict[str, float] = {}
COOLDOWN_SECONDS = 300  # 5 min between alerts per asset

DEXSCREENER_URL = "https://api.dexscreener.com/latest/dex/tokens/{mint}"


# -- Watchlist loader ----------------------------------------------------------
def load_watchlist() -> list[dict]:
    with open(WATCHLIST_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["rsky.watch"]


# -- DexScreener fetch ---------------------------------------------------------
def fetch_dexscreener(mint: str) -> dict | None:
    """
    Fetch token data from DexScreener for a single mint address.
    Returns the highest-liquidity pair's data, or None if not found.

    DexScreener may return multiple pairs per token (different pools).
    We pick the one with highest liquidity � most reliable signal source.
    """
    try:
        r = requests.get(
            DEXSCREENER_URL.format(mint=mint),
            timeout=10,
            headers={"User-Agent": "scalp-engine/1.0"},
        )
        if r.status_code != 200:
            log.warning(f"DexScreener HTTP {r.status_code} for {mint[:8]}...")
            return None

        pairs = r.json().get("pairs") or []
        if not pairs:
            return None

        # Pick highest liquidity pair � most reliable vol/price data
        pairs.sort(
            key=lambda p: p.get("liquidity", {}).get("usd", 0) or 0, reverse=True
        )
        p = pairs[0]

        # Data quality gate � reject pair if any priceChange field is implausible
        # DexScreener occasionally returns corrupt deltas (e.g. +497112%) on low-liquidity pairs
        _chg = p.get("priceChange", {})
        _chg_fields = [
            _chg.get("m5", 0),
            _chg.get("h1", 0),
            _chg.get("h6", 0),
            _chg.get("h24", 0),
        ]
        if any(abs(float(v or 0)) > 1000 for v in _chg_fields):
            log.warning(
                f"DATA QUALITY: {mint[:8]}... rejected � implausible priceChange {_chg}"
            )
            return None

        liq = p.get("liquidity", {})
        vol = p.get("volume", {})
        chg = p.get("priceChange", {})
        txns = p.get("txns", {})

        # Flow strength proxy: buys vs sells in last 1h
        buys_1h = txns.get("h1", {}).get("buys", 0) or 0
        sells_1h = txns.get("h1", {}).get("sells", 0) or 0
        total_txns_1h = buys_1h + sells_1h
        flow_raw = (buys_1h - sells_1h) / total_txns_1h if total_txns_1h > 0 else 0

        return {
            "price": float(p.get("priceUsd", 0) or 0),
            "change_5m": float(chg.get("m5", 0) or 0),
            "change_1h": float(chg.get("h1", 0) or 0),
            "change_6h": float(chg.get("h6", 0) or 0),
            "change_24h": float(chg.get("h24", 0) or 0),
            "volume_1h": float(vol.get("h1", 0) or 0),
            "volume_24h": float(vol.get("h24", 0) or 0),
            "liquidity": float(liq.get("usd", 0) or 0),
            "mc": float(p.get("marketCap", 0) or 0),
            "net_volume_1h": flow_raw,  # buy/sell ratio proxy (-1 to +1)
            "holders_change_24h": 0,  # not available on DexScreener
            "dex": p.get("dexId", "unknown"),
            "pair": p.get("pairAddress", ""),
        }

    except Exception as e:
        log.warning(f"DexScreener fetch failed for {mint[:8]}...: {e}")
        return None


def fetch_all(watchlist: list[dict]) -> dict[str, dict]:
    """
    Fetch DexScreener data for all watchlist assets.
    Sequential with 200ms gap � DexScreener has no strict rate limit
    but parallel hammering can trigger soft throttling.
    """
    results = {}
    for asset in watchlist:
        mint = asset["mint"]
        symbol = asset["symbol"]
        data = fetch_dexscreener(mint)
        if data:
            results[mint] = data
            log.debug(
                f"  {symbol}: ${data['price']:.4f} "
                f"1h={data['change_1h']:+.1f}% "
                f"liq=${data['liquidity']:,.0f}"
            )
        time.sleep(0.2)
    return results


# -- Feature engineering -------------------------------------------------------
def compute_features(d: dict) -> dict:
    """
    Derive signal features from raw DexScreener data.
    All values are raw � normalization happens in normalize().
    """
    vol_24h = d.get("volume_24h", 0) or 1  # avoid div/0
    vol_1h = d.get("volume_1h", 0) or 0
    liq = d.get("liquidity", 0) or 1

    # Vol acceleration: 1h pace vs average 1h pace from 24h total
    # >1 = accelerating, >2 = strong acceleration, >3 = spike
    vol_accel = vol_1h / (vol_24h / 24) if vol_24h > 0 else 0

    # Flow strength: buy/sell ratio proxy from txn counts (-1 sell-heavy, +1 buy-heavy)
    flow_strength = float(d.get("net_volume_1h", 0) or 0)
    flow_strength = max(-1.0, min(1.0, flow_strength))

    # Liquidity pressure: vol stress on pool � >1 means pool is being drained
    liq_pressure = vol_24h / liq if liq > 0 else 0

    # Momentum slope: is the 1h move faster than the 24h average hourly move?
    change_24h = d.get("change_24h", 0) or 0
    change_1h = d.get("change_1h", 0) or 0
    momentum_slope = (change_1h / (change_24h / 24)) if change_24h != 0 else 0

    return {
        "vol_accel": round(vol_accel, 3),
        "flow_strength": round(flow_strength, 3),
        "liq_pressure": round(liq_pressure, 3),
        "momentum_slope": round(momentum_slope, 3),
        "change_5m": d.get("change_5m", 0) or 0,
        "change_1h": change_1h,
        "change_6h": d.get("change_6h", 0) or 0,
        "change_24h": change_24h,
        "holders_change": d.get("holders_change_24h", 0) or 0,
        "liquidity": liq,
        "volume_1h": vol_1h,
        "volume_24h": vol_24h,
        "price": d.get("price", 0) or 0,
        "dex": d.get("dex", "unknown"),
    }


# -- Normalization -------------------------------------------------------------
def normalize(f: dict) -> dict:
    """Clamp all features to [0, 1] per spec normalization rules."""

    def clamp(v, lo=0.0, hi=1.0):
        return max(lo, min(hi, v))

    return {
        "n_change_24h": clamp(f["change_24h"] / 20),
        "n_change_1h": clamp(f["change_1h"] / 5),
        "n_vol_accel": clamp((f["vol_accel"] - 1) / 3),
        "n_flow_strength": clamp((f["flow_strength"] + 1) / 2),
        "n_liq_pressure": clamp(f["liq_pressure"] / 1.5),
        "n_holders": clamp((f["holders_change"] + 10) / 20),
    }


# -- Scoring -------------------------------------------------------------------
def score_asset(raw: dict) -> tuple[float, dict, dict]:
    """
    Weighted composite scalp score (0-100).
    Weights per MRB directive spec:
      24h momentum  15%  � lagging confirmation
      1h momentum   20%  � primary momentum signal
      vol accel     20%  � early breakout indicator
      flow strength 25%  � buy/sell pressure (highest weight)
      liq pressure  10%  � pool stress
      holder press  10%  � holder conviction
    """
    f = compute_features(raw)
    n = normalize(f)

    score = (
        n["n_change_24h"] * 15
        + n["n_change_1h"] * 20
        + n["n_vol_accel"] * 20
        + n["n_flow_strength"] * 25
        + n["n_liq_pressure"] * 10
        + n["n_holders"] * 10
    )
    return round(score, 1), f, n


# -- Risk filters --------------------------------------------------------------
def risk_flags(f: dict) -> list[str]:
    flags = []
    # Distribution: price up but sell pressure dominant
    if f["flow_strength"] < -0.1 and f["change_24h"] > 10:
        flags.append("DISTRIBUTION")
    # Manipulation: vol spike with pool stress
    if f["vol_accel"] > 2.5 and f["liq_pressure"] > 1.5:
        flags.append("MANIPULATION_RISK")
    # Extended: 5m spike into already-extended 24h move
    if f["change_5m"] > 3 and f["change_24h"] > 15:
        flags.append("EXTENDED_ENTRY")
    return flags


# -- Tier classification -------------------------------------------------------
def classify_tier(score: float, f: dict) -> str:
    _flags = risk_flags(f)
    # TEMP TEST: allow score-based T1/T2 routing even when risk flags exist.
    # if _flags:
    #     return "RISK"
    if (
        score >= 70
        and f["vol_accel"] > 2
        and f["flow_strength"] > 0.25
        and f["liquidity"] >= MIN_LIQUIDITY
    ):
        return "T1"
    if 1 <= score < 80 and f["flow_strength"] > 0:
        return "T2"
    return "IGNORE"


# -- Signal log ----------------------------------------------------------------
def log_signal(symbol: str, score: float, tier: str, f: dict, flags: list[str]) -> None:
    """
    Append structured signal record to signal_log.jsonl.
    One line per signal � queryable foundation for future analysis.
    """
    record = {
        "ts": datetime.datetime.now().isoformat(),
        "symbol": symbol,
        "score": score,
        "tier": tier,
        "change_1h": f["change_1h"],
        "change_24h": f["change_24h"],
        "vol_accel": f["vol_accel"],
        "flow": f["flow_strength"],
        "liq": f["liquidity"],
        "liq_pressure": f["liq_pressure"],
        "flags": flags,
    }
    with open(SIGNAL_LOG, "a", encoding="utf-8") as sl:
        sl.write(json.dumps(record) + "\n")


# -- Telegram ------------------------------------------------------------------
def send_telegram(msg: str) -> None:
    if not TG_TOKEN or not TG_CHAT_ID:
        log.warning("Telegram not configured � skipping push")
        return
    try:
        r = requests.post(
            f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
            json={"chat_id": TG_CHAT_ID, "text": msg, "parse_mode": "Markdown"},
            timeout=10,
        )
        if r.status_code != 200:
            log.warning(f"Telegram push failed: {r.status_code} {r.text[:100]}")
    except Exception as e:
        log.error(f"Telegram error: {e}")


def format_alert(
    symbol: str, score: float, tier: str, f: dict, flags: list[str]
) -> str:
    emoji = {"T1": "??", "T2": "?", "RISK": "??"}.get(tier, "")
    lines = [
        f"{emoji} *{tier} � {symbol}*",
        f"Score: `{score}/100` | DEX: `{f['dex']}`",
        f"5m: `{f['change_5m']:+.2f}%` | 1h: `{f['change_1h']:+.2f}%` | 24h: `{f['change_24h']:+.2f}%`",
        f"Vol Accel: `{f['vol_accel']:.2f}x` | Flow: `{f['flow_strength']:+.2f}`",
        f"Liq: `${f['liquidity']:,.0f}` | Pressure: `{f['liq_pressure']:.2f}`",
        f"Vol 1h: `${f['volume_1h']:,.0f}` | 24h: `${f['volume_24h']:,.0f}`",
    ]
    if flags:
        lines.append("?? " + " | ".join(flags))
    lines.append(f"_{datetime.datetime.now().strftime('%H:%M:%S')}_")
    return "\n".join(lines)


def format_summary(results: list[dict]) -> str:
    """Ranked top-5 summary pushed every cycle."""
    lines = [f"?? *Scalp Scan � {datetime.datetime.now().strftime('%H:%M')}*"]
    top5 = [r for r in results if r["tier"] not in ("IGNORE", "LIQ")][:5]
    if not top5:
        top5 = results[:5]
    for r in top5:
        tier_tag = f" `[{r['tier']}]`" if r["tier"] != "IGNORE" else ""
        lines.append(
            f"`{r['symbol']:<10}` `{r['score']:>5.1f}` "
            f"1h=`{r['f']['change_1h']:+.1f}%` "
            f"acc=`{r['f']['vol_accel']:.1f}x`{tier_tag}"
        )
    return "\n".join(lines)


# -- Main scoring loop ---------------------------------------------------------
def run_cycle(watchlist: list[dict]) -> None:
    log.info(f"Fetching DexScreener data for {len(watchlist)} assets...")
    raw_data = fetch_all(watchlist)
    log.info(f"Data received: {len(raw_data)}/{len(watchlist)} assets")

    results = []
    _shortlist_candidates = []
    for asset in watchlist:
        mint = asset["mint"]
        symbol = asset["symbol"]
        raw = raw_data.get(mint)

        if not raw:
            log.debug(f"No data for {symbol} � skipping")
            continue

        score, f, n = score_asset(raw)
        liq = raw.get("liquidity", 0) or 0
        if liq < MIN_LIQUIDITY:
            tier = "LIQ"
            flags = ["LOW_LIQUIDITY"]
            results.append(
                {
                    "symbol": symbol,
                    "score": score,
                    "tier": tier,
                    "f": f,
                    "flags": flags,
                }
            )
            log_signal(symbol, score, tier, f, flags)
            log.debug(f"SKIP {symbol} � liquidity ${liq:,.0f} below threshold")
            continue

        tier = classify_tier(score, f)
        flags = risk_flags(f)

        results.append(
            {
                "symbol": symbol,
                "score": score,
                "tier": tier,
                "f": f,
                "flags": flags,
            }
        )

        # Log all scored assets to signal_log.jsonl
        log_signal(symbol, score, tier, f, flags)

        # Route by tier
        if tier == "RISK":
            # RISK bypasses arbitration � direct Telegram
            now = time.time()
            last = _alert_cooldown.get(symbol, 0)
            if now - last > COOLDOWN_SECONDS:
                msg = format_alert(symbol, score, tier, f, flags)
                send_telegram(msg)
                _alert_cooldown[symbol] = now
                log.info(
                    f"ALERT � {symbol} {tier} score={score} "
                    f"1h={f['change_1h']:+.1f}% acc={f['vol_accel']:.2f}x"
                )
        elif tier in ("T1", "T2"):
            # T1/T2 — regime gate then shortlist (arbitration path)
            try:
                brief = json.loads(BRIEF_PATH.read_text())
                regime = (
                    (brief.get("macro_regime") or {})
                    .get("classification", "UNKNOWN")
                    .upper()
                )
            except Exception:
                regime = "UNKNOWN"
            # Attach regime to result dict for dispatcher formatting
            results[-1]["regime"] = regime
            if regime == "UNKNOWN":
                log.info(f"REGIME GATE - {symbol} {tier} suppressed (regime UNKNOWN)")
            else:
                if regime == "RISK-OFF":
                    flags = flags + ["REGIME_CONFLICT"]
                _shortlist_candidates.append(
                    {
                        "symbol": symbol,
                        "score": score,
                        "tier": tier,
                        "flags": flags,
                        "regime": regime,
                        "change_1h": f.get("change_1h", 0),
                        "vol_accel": f.get("vol_accel", 0),
                        "dex": f.get("dex", ""),
                    }
                )

    # Rank by score
    results.sort(key=lambda x: x["score"], reverse=True)
    # Write shortlist - top 5 T1/T2 candidates for arbitration
    _shortlist_candidates.sort(key=lambda x: x["score"], reverse=True)
    shortlist = _shortlist_candidates[:5]
    try:
        SHORTLIST_PATH.write_text(json.dumps(shortlist, indent=2))
        log.info(
            f"Shortlist written � {len(shortlist)} candidates: "
            f"{[c['symbol'] for c in shortlist]}"
        )
    except Exception as e:
        log.error(f"Shortlist write failed: {e}")
    # Append scored assets to an append-only event log for auditing and downstream consumers
    event_log_path = pathlib.Path(__file__).parent / "event_log.jsonl"
    try:
        with open(event_log_path, "a", encoding="utf-8") as ef:
            for r in results:
                f = r.get("f", {})
                ef.write(
                    json.dumps(
                        {
                            "ts": datetime.datetime.now().isoformat(),
                            "symbol": r.get("symbol"),
                            "score": r.get("score"),
                            "tier": r.get("tier"),
                            "regime": r.get("regime", "N/A"),
                            "flags": r.get("flags"),
                            "vol_accel": f.get("vol_accel"),
                            "change_1h": f.get("change_1h"),
                        }
                    )
                    + "\n"
                )
    except Exception as e:
        log.error(f"Event log write failed: {e}")
    scored = [r for r in results if r["score"] >= 50]
    log.info(
        f"Cycle complete � {len(results)} scored, "
        f"{len([r for r in results if r['tier'] in ('T1','T2')])} actionable"
    )

    # Dispatcher gate — send only on material state change
    _dispatch_state = load_state()
    _dispatched = False
    for r in results:
        if r["tier"] not in ("T1", "T2", "RISK"):
            continue
        regime = r.get("regime", "UNKNOWN")
        sent = publish_signal(
            r["symbol"],
            r["score"],
            r["tier"],
            r["f"],
            r["flags"],
            regime,
            _dispatch_state,
            send_telegram,
        )
        if sent:
            _dispatched = True
            log.info(f"DISPATCH -- {r['symbol']} {r['tier']} score={r['score']}")
    if _dispatched:
        save_state(_dispatch_state)


# -- Entry point ---------------------------------------------------------------
if __name__ == "__main__":
    if not TG_TOKEN or not TG_CHAT_ID:
        log.error("TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not set � exiting")
        raise SystemExit(1)

    watchlist = load_watchlist()
    # In load_watchlist() or wherever wl is consumed before fetch_all:
    watchlist = [a for a in watchlist if not a.get("exclude_from_scalp")]

    log.info(
        f"Scalp engine started � {len(watchlist)} assets, {POLL_INTERVAL}s interval"
    )
    log.info(f"Data source: DexScreener (no auth required)")
    log.info(f"Signal log: {SIGNAL_LOG}")

    while True:
        try:
            run_cycle(watchlist)
        except Exception as e:
            log.error(f"Cycle error: {e}")
        time.sleep(POLL_INTERVAL)
