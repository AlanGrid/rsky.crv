# brief.py - Alan's Morning Research Agent
# Part of: rsky.profit.os / rsky.crv
# Path:     C:/Users/RSky/Documents/AI.ProFit/rsky.crv/01-Market/briefs
# Model:    Google Gemini - Multimodal Pipeline Failover with Structured Schema
# Data:     CoinGecko Demo API + Jupiter DEX synthetics + LMArena leaderboard + RSS feeds
# Run:      python brief.py
# Updated:  2026-05-30 — added Jupiter synthetic token monitor (TSLAx, ANTHROPICx, NEURALINKx, NBISon, PLTRx, GOOGLx, NVDAx)

import os
import json
import datetime
import pathlib
import logging
import sys
import time
import urllib.request
import urllib.error

import feedparser
from google import genai
from google.genai import types

# Paths
BASE = pathlib.Path(r"D:\Users\RSky\Desktop\AI.ProFit\rsky.crv\01-Market\briefs")
BASE.mkdir(parents=True, exist_ok=True)

LOG_FILE = BASE / "agent-run.log"
LATEST   = BASE / "brief-latest.json"
DATED    = BASE / f"brief-{datetime.date.today()}.json"

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("morning_agent")

# Portfolio - Alan's holdings (CoinGecko IDs)
PORTFOLIO = [
    # CoinGecko portfolio
    "bitcoin", "solana", "uniswap", "ethereum", "cosmos", "ripple",
    "zksync", "arbitrum", "aave", "optimism", "hedera-hashgraph",
    "cardano", "celestia", "story-2", "jupiter-exchange-solana",
    "virtuals-protocol", "wrapped-bitcoin", "mantra-dao",
    "initia", "kite-ai", "power-ledger",
    "binancecoin", "pudgy-penguins", "usd-coin",
    "osmosis", "berachain-bera", "lava-network", "saga-2",
    "hashpack", "avail", "chainlink", "vechain", "payai-network",
    "algorand", "avalanche-2", "ankr", "dappradar", "wen-4",
    "dymension", "telcoin", "particle-network",
    "babylon-2", "matic-network", "orbiter-finance",
    "metaverse-index", "dogecoin", "energy-web-token",
    "stride", "quick", "juno-network",
    "altlayer", "zetachain", "world-mobile-token", "shapeshift-fox-token",
    "vethor-token", "dai", "raydium", "utrust",
    "secret", "evmos", "rivalz-network",
    "sei-network", "stargaze", "agoric",
    # Jupiter DEX native crypto
    "helium", "bittensor", "sui", "near", "zcash",
    "coinbase-wrapped-btc", "pyth-network", "bonk",
    "official-trump", "fartcoin", "hyperliquid",
    "wormhole", "eliza-2",
]

# Synthetic stock tokens on Jupiter DEX - tracked via underlying equity news
EQUITY_WATCHLIST = {
    "PLTRx":      "Palantir Technologies (PLTR)",
    "OPENAIx":    "OpenAI",
    "ANTHROPICx": "Anthropic",
    "MUon":       "Micron Technology (MU)",
    "GOOGLx":     "Alphabet / Google (GOOGL)",
    "MSFTx":      "Microsoft (MSFT)",
    "NVDAx":      "NVIDIA (NVDA)",
    "ANDURIL":    "Anduril Industries",
    "CRWVon":     "CoreWeave (CRWV)",
    "INTCx":      "Intel (INTC)",
    "TSLAx":      "Tesla (TSLA)",
    "TSLAon":     "Tesla (TSLA)",
    "USOon":      "US Oil Fund (USO)",
    "SPACEXx":    "SpaceX",
    "CRCLx":      "Circle (CRCL)",
    "METAon":     "Meta Platforms (META)",
    "GLDx":       "Gold (GLD)",
    "MSTRx":      "MicroStrategy (MSTR)",
    "COINx":      "Coinbase (COIN)",
    "HOODx":      "Robinhood (HOOD)",
    "STRCx":      "MicroStrategy / Strategy (STRC)",
    "OKLOon":     "Oklo (OKLO)",
    "elizaOS":    "ElizaOS / AI16Z",
}

SCALP_WATCHLIST = [
    "bitcoin", "solana", "ethereum", "ripple", "binancecoin",
    "cardano", "avalanche-2", "uniswap", "arbitrum", "optimism",
    "sui", "bonk", "hyperliquid",
]

# RSS Sources
FEEDS = {
    "ai": [
        ("Anthropic Blog",              "https://www.anthropic.com/rss.xml"),
        ("TechCrunch AI",               "https://techcrunch.com/category/artificial-intelligence/feed/"),
        ("The Batch (DeepLearning.AI)", "https://www.deeplearning.ai/the-batch/feed/"),
    ],
    "crypto": [
        ("CoinDesk",        "https://www.coindesk.com/arc/outboundfeeds/rss/"),
        ("CoinTelegraph",   "https://cointelegraph.com/rss"),
        ("The Block",       "https://www.theblock.co/rss.xml"),
    ],
    "finance": [
        ("Bloomberg Markets", "https://feeds.bloomberg.com/markets/news.rss"),
        ("Reuters Finance",   "https://feeds.reuters.com/reuters/businessNews"),
    ],
    "health": [
        ("Longevity Technology", "https://longevity.technology/feed/"),
        ("Nature Longevity",     "https://www.nature.com/nataging.rss"),
    ],
}

MAX_PER_FEED = 3
CG_BASE      = "https://api.coingecko.com/api/v3"
ARENA_BASE   = "https://raw.githubusercontent.com/oolong-tea-2026/arena-ai-leaderboards/main/data"
ARENA_API    = f"{ARENA_BASE}/latest.json"

# Generic fetch helper
def fetch_json(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        log.warning(f"HTTP {e.code} for {url}")
        return None
    except Exception as e:
        log.warning(f"Fetch error {url}: {e}")
        return None

# CoinGecko portfolio data
def fetch_portfolio_data(api_key):
    log.info("Fetching portfolio data from CoinGecko...")
    ids  = ",".join(PORTFOLIO)
    url  = (f"{CG_BASE}/coins/markets?vs_currency=usd&ids={ids}"
            f"&order=market_cap_desc&per_page=100&page=1"
            f"&price_change_percentage=24h,7d&sparkline=false")
    data = fetch_json(url, {"x-cg-demo-api-key": api_key})
    if not data:
        return [], []

    portfolio_summary = []
    scalp_signals     = []

    for coin in data:
        change_24h = coin.get("price_change_percentage_24h") or 0
        change_7d  = coin.get("price_change_percentage_7d_in_currency") or 0
        volume     = coin.get("total_volume") or 0
        mcap       = coin.get("market_cap") or 1
        vol_mcap   = round(volume / mcap * 100, 2)

        entry = {
            "id":             coin["id"],
            "symbol":         coin["symbol"].upper(),
            "name":           coin["name"],
            "price":          coin.get("current_price"),
            "change_24h":     round(change_24h, 2),
            "change_7d":      round(change_7d, 2),
            "volume_24h":     volume,
            "vol_mcap_ratio": vol_mcap,
        }
        portfolio_summary.append(entry)

        if coin["id"] in SCALP_WATCHLIST and vol_mcap > 5:
            scalp_signals.append(entry)

    log.info(f"Portfolio: {len(portfolio_summary)} assets, {len(scalp_signals)} scalp signals")
    return portfolio_summary, scalp_signals

# CoinGecko trending
def fetch_trending(api_key):
    log.info("Fetching trending coins...")
    data = fetch_json(f"{CG_BASE}/search/trending",
                      {"x-cg-demo-api-key": api_key})
    if not data:
        return []
    trending = []
    for item in data.get("coins", [])[:5]:
        c = item.get("item", {})
        trending.append(f"{c.get('name')} ({c.get('symbol','').upper()})")
    return trending

# Jupiter DEX synthetic token monitor
JUPITER_WATCH = {
    "TSLAx": {
        "mint":        "XsDoVfqeBukxuZHWhdvWHBhgEHjGNst4MLodqsJHzoB",
        "alert_low":   None,
        "alert_exit":  None,
        "position":    True,
        "note":        "Post-spike bleed — $440 to $15 in 10 days. Residual ~$0.48. Full cycle observed.",
    },
    "ANTHROPICx": {
        "mint":        "Pren1FvFX6J3E4kXhJuCiAD5aDmGEb7qJRncwA8Lkhw",
        "alert_low":   700,
        "alert_exit":  634,
        "position":    True,
        "note":        "Active position — watch $700 add / $634 invalidation",
    },
    "NEURALINKx": {
        "mint":        "PrekqLJvJ3qVdXmBGDiexvwUTF4rLFDa6HWS4HJbw9S",
        "alert_low":   None,
        "alert_exit":  None,
        "position":    True,
        "note":        "Accumulation phase — watch holder count direction",
    },
    "NBISon": {
        "mint":        "DiRshqNDE68bWbGdLHm1GwQ76MvWQG3af6w1NdQondo",
        "alert_low":   None,
        "alert_exit":  None,
        "position":    True,
        "note":        "Pre-accumulation — 31 holders, watch for inflection",
    },
    "PLTRx": {
        "mint":        "XsoBhf2ufR8fTyNSjqfU71DYGaE6Z3SUGAidpzriAA4",
        "alert_low":   None,
        "alert_exit":  None,
        "position":    False,
        "note":        "No position — watch holders >500, liquidity >$150K",
    },
    "GOOGLx": {
        "mint":        "XsCPL9dNWBMvFtTmwcCA5v3xWPSMEBCszbQdiLLq6aN",
        "alert_low":   None,
        "alert_exit":  None,
        "position":    True,
        "note":        "Hold — entries at 4.48-4.54 SOL/token. Low volatility, no catalyst active.",
    },
    "NVDAx": {
        "mint":        "Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh",
        "alert_low":   None,
        "alert_exit":  None,
        "position":    True,
        "note":        "Hold — 0.07302 NVDAx, blended ~$216.50. Watch NVIDIA earnings and export control news.",
    },
}

JUPITER_PRICE_API = "https://api.jup.ag/price/v2?ids={mint}"

def fetch_jupiter_synthetics():
    log.info("Fetching Jupiter synthetic token data...")
    results = []
    for symbol, cfg in JUPITER_WATCH.items():
        mint = cfg["mint"]
        entry = {
            "symbol":    symbol,
            "position":  cfg["position"],
            "note":      cfg["note"],
            "price":     None,
            "liquidity": None,
            "holders":   None,
            "vol_24h":   None,
            "signal":    "unknown",
            "alert":     None,
        }
        # Fetch price from Jupiter Price API
        price_data = fetch_json(JUPITER_PRICE_API.format(mint=mint))
        if price_data:
            price_info = price_data.get("data", {}).get(mint, {})
            entry["price"] = price_info.get("price")

        # Check alert levels for ANTHROPICx
        if entry["price"] and cfg.get("alert_low"):
            try:
                p = float(entry["price"])
                if p <= cfg["alert_exit"]:
                    entry["alert"] = f"HARD INVALIDATION — price at ${p:.2f}, below ${cfg['alert_exit']} exit level"
                elif p <= cfg["alert_low"]:
                    entry["alert"] = f"ADD DECISION POINT — price at ${p:.2f}, at ${cfg['alert_low']} watch level"
            except (TypeError, ValueError):
                pass

        results.append(entry)
        time.sleep(0.3)

    log.info(f"Jupiter synthetics: {len(results)} tokens fetched")
    return results

# LMArena AI leaderboard
def fetch_ai_leaderboard():
    log.info("Fetching LMArena AI leaderboard...")
    headers = {"User-Agent": "Mozilla/5.0"}
    meta = fetch_json(ARENA_API, headers)
    if not meta:
        log.warning("Leaderboard unavailable — skipping")
        return []
    date_path = meta.get("path") or meta.get("date") or datetime.date.today().isoformat()
    url  = f"{ARENA_BASE}/{date_path}/text.json"
    data = fetch_json(url, headers)
    if not data:
        return []
    models  = []
    entries = data.get("models", []) if isinstance(data, dict) else data
    for item in entries[:10]:
        name   = item.get("model") or item.get("model_name") or item.get("name") or ""
        score  = item.get("score") or item.get("rating") or item.get("elo") or ""
        rank   = str(item.get("rank", ""))
        vendor = item.get("vendor", "")
        if name:
            models.append({"rank": rank, "name": name, "score": str(score), "vendor": vendor})
    log.info(f"Leaderboard: {len(models)} models fetched")
    return models

# RSS headlines
def fetch_headlines():
    headlines       = []
    sources_scanned = 0
    for tag, feeds in FEEDS.items():
        for name, url in feeds:
            try:
                feed    = feedparser.parse(url)
                entries = feed.entries[:MAX_PER_FEED]
                for e in entries:
                    headlines.append({
                        "tag":     tag,
                        "source":  name,
                        "title":   e.get("title", "").strip(),
                        "summary": e.get("summary", "")[:300].strip(),
                        "link":    e.get("link", ""),
                    })
                sources_scanned += 1
                log.info(f"Fetched {len(entries)} items from {name}")
            except Exception as ex:
                log.warning(f"Failed to fetch {name}: {ex}")
    return headlines, sources_scanned

# Prompt
SYSTEM = """You are Alan's morning research agent. Alan is a crypto scalp trader,
AI researcher, and longevity enthusiast based in Ukraine. He runs a liquidity-first
scalp strategy: filter by high volume/market-cap ratio and rising holder count.
Surface only items directly relevant to his context. Be direct, no fluff, no flattery."""

def build_prompt(headlines, portfolio, scalp_signals, trending, leaderboard, jupiter_synthetics=None):
    # Cap at 8 headlines, trim summary to 100 chars to reduce token overhead
    rss_lines = "\n".join(
        f"[{h['tag'].upper()}] {h['source']}: {h['title']} — {h['summary'][:100]}"
        for h in headlines[:8]
    )
    # Top 8 movers only — sorted by absolute 24h change
    portfolio_lines = "\n".join(
        f"  {c['symbol']}: ${c['price']} | 24h: {c['change_24h']}% | 7d: {c['change_7d']}% | vol/mcap: {c['vol_mcap_ratio']}%"
        for c in sorted(portfolio, key=lambda x: abs(x['change_24h']), reverse=True)[:8]
    ) if portfolio else "  No data."

    # Cap scalp signals at 6
    scalp_lines = "\n".join(
        f"  {c['symbol']}: vol/mcap {c['vol_mcap_ratio']}% | 24h {c['change_24h']}%"
        for c in scalp_signals[:6]
    ) if scalp_signals else "  No signals today."

    trending_line = ", ".join(trending[:5]) if trending else "None"

    # Leaderboard top 5 only
    lb_lines = "\n".join(
        f"  #{m['rank']} {m['name']} — {m['score']}"
        for m in leaderboard[:5]
    ) if leaderboard else "  Unavailable."

    # Equity watchlist — symbols only to save tokens
    equity_line = ", ".join(EQUITY_WATCHLIST.keys())

    # Jupiter synthetic token monitor block
    if jupiter_synthetics:
        jupiter_lines = []
        for t in jupiter_synthetics:
            price_str = f"${float(t['price']):.2f}" if t.get("price") else "n/a"
            alert_str = f" ⚠ {t['alert']}" if t.get("alert") else ""
            pos_str   = "ACTIVE" if t["position"] else "WATCH"
            jupiter_lines.append(
                f"  {t['symbol']} [{pos_str}]: price={price_str} | {t['note']}{alert_str}"
            )
        jupiter_block = "JUPITER SYNTHETIC MONITOR:\n" + "\n".join(jupiter_lines)
    else:
        jupiter_block = "JUPITER SYNTHETIC MONITOR: unavailable"

    return f"""Today is {datetime.date.today().strftime('%A, %B %d, %Y')}.

{jupiter_block}

PORTFOLIO SNAPSHOT (top movers):
{portfolio_lines}

SCALP SIGNALS (high vol/mcap from watchlist):
{scalp_lines}

TRENDING ON COINGECKO: {trending_line}

SYNTHETIC STOCK EXPOSURE (Jupiter DEX tokens — surface news on these companies):
{equity_line}

AI MODEL LEADERBOARD (LMArena, top 10):
{lb_lines}

RSS HEADLINES:
{rss_lines}

Select 6-8 most relevant news items for your final list. 
Priorities:
- Portfolio assets with unusual 24h move or scalp setup
- News on companies in SYNTHETIC STOCK EXPOSURE list (NVDA, GOOGL, Tesla, Anthropic, OpenAI etc.)
- Macro/crypto news affecting positions
- AI leaderboard shifts — flag if Claude/Anthropic moved ranks
- Longevity research with strong methodology

MACRO REGIME ASSESSMENT:
Based on the portfolio data, headlines, and market context above, classify the current macro regime.
Return as the macro_regime field with: classification (RISK-ON / RISK-OFF / TRANSITIONAL),
liquidity (EXPANDING / CONTRACTING / NEUTRAL), dominant_force (one phrase),
confidence (HIGH / MEDIUM / LOW), invalidation (one condition that flips the classification).
Base this only on observable data in this brief — do not hallucinate conditions."""

# Hard Definition of the Expected Structure for the SDK
RESPONSE_SCHEMA = types.Schema(
    type=types.Type.OBJECT,
    properties={
        "generated_at": types.Schema(type=types.Type.STRING, description="Current time format HH:MM"),
        "date": types.Schema(type=types.Type.STRING, description="ISO Date string YYYY-MM-DD"),
        "sources_scanned": types.Schema(type=types.Type.INTEGER),
        "scalp_signals": types.Schema(
            type=types.Type.ARRAY,
            items=types.Schema(type=types.Type.STRING)
        ),
        "trending": types.Schema(
            type=types.Type.ARRAY,
            items=types.Schema(type=types.Type.STRING)
        ),
        "ai_leaderboard": types.Schema(
            type=types.Type.ARRAY,
            items=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "rank": types.Schema(type=types.Type.STRING),
                    "name": types.Schema(type=types.Type.STRING),
                    "score": types.Schema(type=types.Type.STRING),
                    "vendor": types.Schema(type=types.Type.STRING)
                }
            )
        ),
        "jupiter_synthetics": types.Schema(
            type=types.Type.ARRAY,
            items=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "symbol":   types.Schema(type=types.Type.STRING),
                    "price":    types.Schema(type=types.Type.STRING),
                    "signal":   types.Schema(type=types.Type.STRING,
                                description="One of: Accumulation, Building, Pre-spike, Spike, Distribution, Bleed, Support test, Pre-accumulation, Invalidated, Dead, Unknown"),
                    "alert":    types.Schema(type=types.Type.STRING),
                    "note":     types.Schema(type=types.Type.STRING),
                }
            )
        ),
        "macro_regime": types.Schema(
            type=types.Type.OBJECT,
            properties={
                "classification": types.Schema(type=types.Type.STRING,
                    description="One of: RISK-ON, RISK-OFF, TRANSITIONAL"),
                "liquidity":      types.Schema(type=types.Type.STRING,
                    description="One of: EXPANDING, CONTRACTING, NEUTRAL"),
                "dominant_force": types.Schema(type=types.Type.STRING,
                    description="Primary driver in one phrase e.g. 'Fed tightening', 'BTC ETF inflow'"),
                "confidence":     types.Schema(type=types.Type.STRING,
                    description="One of: HIGH, MEDIUM, LOW"),
                "invalidation":   types.Schema(type=types.Type.STRING,
                    description="One condition that would flip the classification"),
            }
        ),
        "items": types.Schema(
            type=types.Type.ARRAY,
            items=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "source": types.Schema(type=types.Type.STRING),
                    "headline": types.Schema(type=types.Type.STRING),
                    "summary": types.Schema(type=types.Type.STRING, description="2 sentences on why it matters for Alan."),
                    "tag": types.Schema(type=types.Type.STRING, description="Must be one of: ai, crypto, finance, health"),
                    "tag_label": types.Schema(type=types.Type.STRING, description="Capitalized title layout matching tag"),
                    "url": types.Schema(type=types.Type.STRING)
                },
                required=["source", "headline", "summary", "tag", "tag_label"]
            )
        )
    },
    required=["generated_at", "date", "sources_scanned", "scalp_signals", "trending", "ai_leaderboard", "jupiter_synthetics", "macro_regime", "items"]
)

# Main
def run():
    log.info("Morning agent starting...")

    gemini_key = os.environ.get("GEMINI_API_KEY", "AIzaSyA9CaJqSU1fgFntYObOVEFBuDDxNYlTviA")
    if not gemini_key:
        log.error("No Gemini API key.")
        sys.exit(1)

    cg_key = os.environ.get("COINGECKO_API_KEY", "CG-6yyRPUjnMkoGrXPrsps6EK6q")
    if not cg_key:
        log.error("No CoinGecko API key.")
        sys.exit(1)

    portfolio, scalp_signals = fetch_portfolio_data(cg_key)
    time.sleep(1)
    trending         = fetch_trending(cg_key)
    leaderboard      = fetch_ai_leaderboard()
    headlines, sources_scanned = fetch_headlines()
    jupiter_synthetics = fetch_jupiter_synthetics()

    log.info(f"Headlines: {len(headlines)} from {sources_scanned} sources")

    client = genai.Client(api_key=gemini_key)
    prompt_content = build_prompt(headlines, portfolio, scalp_signals, trending, leaderboard, jupiter_synthetics)

    # Failover pipeline: 429 drops to next model, 503 retries with exponential backoff
    model_pipeline = ["gemini-2.5-pro", "gemini-2.5-flash", "gemini-2.0-flash"]
    result = None

    def attempt_generation(client, model_name, prompt):
        """Single model attempt with exponential backoff for 503s. Raises on 429."""
        max_retries = 3
        delay = 2
        gen_config = types.GenerateContentConfig(
            system_instruction=SYSTEM,
            max_output_tokens=8192,
            temperature=0.1,
            response_mime_type="application/json",
            response_schema=RESPONSE_SCHEMA,
        )
        for attempt in range(max_retries):
            try:
                log.info(f"Attempting {model_name} (try {attempt + 1}/{max_retries})...")
                return client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                    config=gen_config,
                )
            except Exception as e:
                err_msg = str(e)
                if "429" in err_msg or "RESOURCE_EXHAUSTED" in err_msg:
                    log.warning(f"{model_name} quota exhausted (429) — dropping to next model.")
                    raise  # Don't retry 429 — move to next model immediately
                elif "503" in err_msg or "UNAVAILABLE" in err_msg:
                    if attempt == max_retries - 1:
                        log.warning(f"{model_name} still unavailable after {max_retries} retries — dropping to next model.")
                        raise
                    log.warning(f"{model_name} bottlenecked (503). Retrying in {delay}s...")
                    time.sleep(delay)
                    delay *= 2  # Exponential backoff: 2s → 4s → 8s
                else:
                    log.error(f"{model_name} unexpected error: {err_msg} — dropping to next model.")
                    raise

    for current_model in model_pipeline:
        try:
            result = attempt_generation(client, current_model, prompt_content)
            log.info(f"Generation successful using {current_model}.")
            break
        except Exception:
            continue

    if not result:
        log.error("All fallback nodes exhausted. Writing empty brief placeholder to avoid OS path crash.")
        placeholder = {
            "generated_at": datetime.datetime.now().strftime("%H:%M"),
            "date": datetime.date.today().isoformat(),
            "sources_scanned": sources_scanned,
            "scalp_signals": [c["symbol"] for c in scalp_signals],
            "trending": trending,
            "ai_leaderboard": leaderboard[:5],
            "jupiter_synthetics": jupiter_synthetics,
            "items": [{
                "source": "System",
                "headline": "All AI model nodes failed — quota exhausted or service unavailable.",
                "summary": "Run again later or check agent-run.log for details.",
                "tag": "finance",
                "tag_label": "Finance",
                "url": ""
            }],
            "portfolio_snapshot": portfolio,
        }
        import shutil
        LATEST.write_text(json.dumps(placeholder, ensure_ascii=False, indent=2), encoding="utf-8")
        shutil.copy2(LATEST, DATED)
        log.info(f"Placeholder brief written to {LATEST}")
        return

    # Safe Sanitization Layer using hex codes to completely avoid string formatting breaks
    try:
        raw_text = result.text.strip()
        backtick_fence = "\x60\x60\x60"
        json_fence = "\x60\x60\x60json"
        
        if raw_text.startswith(json_fence):
            raw_text = raw_text.replace(json_fence, "", 1).rstrip("\x60").strip()
        elif raw_text.startswith(backtick_fence):
            raw_text = raw_text.replace(backtick_fence, "", 1).rstrip("\x60").strip()
            
        brief = json.loads(raw_text)
    except json.JSONDecodeError as parse_err:
        log.error("API response returned structurally flawed payload. Dumping output trace:")
        log.error(result.text)
        raise parse_err
    
    # Inject missing dynamic fields from python state
    if "sources_scanned" not in brief or not brief["sources_scanned"]:
        brief["sources_scanned"] = sources_scanned
    if "scalp_signals" not in brief or not brief["scalp_signals"]:
        brief["scalp_signals"] = [c['symbol'] for c in scalp_signals]
    if "trending" not in brief or not brief["trending"]:
        brief["trending"] = trending
    if "ai_leaderboard" not in brief or not brief["ai_leaderboard"]:
        brief["ai_leaderboard"] = leaderboard[:10]
        
    if "jupiter_synthetics" not in brief or not brief["jupiter_synthetics"]:
        brief["jupiter_synthetics"] = jupiter_synthetics
    brief["portfolio_snapshot"] = portfolio

    if "macro_regime" not in brief or not brief["macro_regime"]:
        brief["macro_regime"] = {
            "classification": "UNKNOWN",
            "liquidity":      "UNKNOWN",
            "dominant_force": "Gemini failed to assess",
            "confidence":     "LOW",
            "invalidation":   "n/a"
        }

    import shutil
    LATEST.write_text(json.dumps(brief, ensure_ascii=False, indent=2), encoding="utf-8")
    shutil.copy2(LATEST, DATED)

    log.info(f"Brief written — {len(brief['items'])} items")
    log.info(f"Latest : {LATEST}")
    log.info(f"Archive: {DATED}")


if __name__ == "__main__":
    try:
        run()
    except json.JSONDecodeError as e:
        log.error(f"JSON parse failed: {e}")
        sys.exit(1)
    except Exception as e:
        log.error(f"Unexpected error: {e}")
        sys.exit(1)