# MRB INDEX — Memory Restoration Block Registry

**System:** Profit.OS — rsky.crv Knowledge Architecture
**Maintained By:** Claude (session-generated) + Alan (manual review)
**Target Directory:** `D:\Users\RSky\Desktop\AI.ProFit\rsky.crv\04-Claude\memory`
**Last Updated:** 2026-06-25
**Template Version:** MRB_v1.2

---

## What This File Is

The master load order and dependency map for all Memory Restoration Blocks.

Claude has no memory between sessions. This index is the entry point.

### Session Start Protocol

1. Open this index.
2. Identify session type.
3. Load required MRBs in specified order.
4. Apply EDS filters where relevant.
5. Do not load unnecessary MRBs — context window is finite.

---

## 🚨 Execution Determinism Layer (SYSTEM RULE)

All MRBs now inherit an implicit **Execution Determinism Score (EDS)** classification.

This affects:

- Load order priority
- Execution reliability assumptions
- Automation eligibility
- Trade feasibility modeling
- Synthetic asset deployment permissions

---

## EDS Classification Model

| Class               | Range  | Meaning                                |
| ------------------- | ------ | -------------------------------------- |
| Fully Deterministic | 85–100 | Predictable execution, automation-safe |
| High Determinism    | 70–84  | Minor slippage risk, mostly stable     |
| Partial Determinism | 50–69  | Manual confirmation required           |
| Fragile Determinism | 25–49  | Execution unreliable, high variance    |
| Non-Deterministic   | 0–24   | Execution cannot be systemized         |

---

## EDS Dependency Rule

When evaluating an MRB:

### Priority Order

1. Capital relevance
2. Protocol relevance
3. Execution Determinism Score (EDS)
4. Liquidity depth
5. Narrative relevance

---

### Synthetic Asset Default Rule

Default synthetic asset assumption:

**EDS = Partial Determinism (50–69)**

Downgrade to Fragile or Non-Deterministic when:

- Transfer Hook restrictions exist
- Automated execution is unavailable
- Liquidity depth is inconsistent
- Execution fees are mutable
- Transfer rules are upgradeable by issuer

Upgrade only after repeated execution validation.

**Pre-listing assets default to EDS = 0 (Non-Deterministic).** No execution possible. EDS upgrades to Partial Determinism upon confirmed listing.

---

## 🚨 Signal Classification Rule — Institutional Announcements (SYSTEM-WIDE)

**Added:** 2026-06-04
**Trigger:** Cosmos / UNDP-BAG membership classification session

The following signal types are classified as **Narrative Signals** by default and require no MRB load, no portfolio action, and no catalyst evaluation:

- Advisory group memberships
- Strategic partnerships
- MOUs
- Ecosystem collaborations
- Pilot announcements
- Institutional endorsements
- Conference appearances
- Foundation announcements
- Academic collaborations
- Enterprise pilots

### Default Action: IGNORE

These signals do not qualify as catalysts under Profit.OS definition unless they create a **measurable and verifiable** path to one or more of:

- Value accrual
- Revenue or fee generation
- On-chain user adoption
- Capital inflow (documented)
- Contractual implementation with defined delivery

### Escalation Condition

Escalate only when a **concrete implementation, contract, deployment, or economic impact** becomes visible and is verifiable within a ≤90-day horizon.

Escalation does not occur on:

- Intent language ("plans to", "exploring", "honored to")
- Advisory or consultative roles
- Multi-party group memberships without execution mandates

### MRB Override Rule

Individual MRBs may define exceptions to this filter for asset-specific monitoring contexts. If no such exception exists in the relevant MRB, this global rule applies without re-evaluation.

### Architecture

```
MRB_INDEX.md
    ↓
Global signal filter (this rule)
    ↓
MRB_Cosmos / MRB_Solana / MRB_Tokens / MRB_Protocols / ...
    ↓
Asset-specific exceptions (if defined in MRB)
```

---

## Load Order by Session Type

### Capital Decision Session

| Load Order | File                                           | Provides                           |
| ---------- | ---------------------------------------------- | ---------------------------------- |
| 1          | `2026-05-31_MRB_claude-memory.md`              | Profit.OS framework, capital rules |
| 2          | `2026-05-31_MRB_protocols.md`                  | Protocol position cards            |
| 3          | `2026-05-31_MRB_tokens.md`                     | Synthetic asset position cards     |
| 4          | `2026-05-31_MRB_jupiterdex-defi-legitimacy.md` | Structural market thesis           |

---

### SOL Rotation Pipeline Session

Trigger: Any session involving HYPE Trade 1, T2/T3 pipeline candidates, or sequential rotation capital decisions.

| Load Order | File                                                | Provides                            |
| ---------- | --------------------------------------------------- | ----------------------------------- |
| 1          | `2026-05-31_MRB_claude-memory.md`                   | Capital framework + Profit.OS rules |
| 2          | `2026-06-05_MRB_weekly-review-rotation-pipeline.md` | Trade 1 HYPE card + pipeline state  |
| 3          | `2026-05-31_MRB_protocols.md`                       | HYPE protocol card                  |
| 4          | `2026-05-31_MRB_jupiterdex-defi-legitimacy.md`      | Captive liquidity thesis            |

**First question every session:** Has the HYPE Trade 1 trigger fired ($56–58 or $62 close + 48h positive net vol)?
**Standing constraint:** 10 SOL JitoSOL is base layer — never deployed. 3 SOL reserve is the only rotation capital.

---

### Cosmos Ecosystem Session

| Load Order                       | File                                         | Provides                   |
| -------------------------------- | -------------------------------------------- | -------------------------- |
| 1                                | `[[2026-06-01_MRB_cosmos-l3-venture-layer]]` | Cosmos ecosystem framework |
| 2 (if capital decision involved) | `[[2026-05-31_MRB_claude-memory]]`           | Capital framework          |

---

### DeFi Infrastructure / HYPE Session

| Load Order | File                                           | Provides                 |
| ---------- | ---------------------------------------------- | ------------------------ |
| 1          | `2026-05-31_MRB_jupiterdex-defi-legitimacy.md` | Captive liquidity thesis |
| 2          | `2026-05-31_MRB_protocols.md`                  | HYPE status              |
| 3          | `2026-05-31_MRB_claude-memory.md`              | Capital framework        |

---

### Jupiter Synthetics Session (EDS-Critical Zone)

Any session involving:

- ANTHROPICx
- PLTRx
- NEURALINKx
- NBISon
- NVDAx
- TSLAx
- GOOGLx
- NBISon (Ondo)
- PLTRon (Ondo)

| Load Order | File                                           | Provides                                     |
| ---------- | ---------------------------------------------- | -------------------------------------------- |
| 1          | `2026-05-31_MRB_tokens.md`                     | Synthetic asset framework                    |
| 2          | `2026-05-31_MRB_claude-memory.md`              | Capital framework                            |
| 3          | `2026-06-02_MRB_mark.price.execution.rules.md` | Execution mechanics & Transfer Hook analysis |
| 4 (Ondo)   | `2026-06-01_MRB_ondo-synthetic-execution.md`   | Ondo JIT mechanics, spot/mark rules          |

**Ondo-specific constraint:** No entry when spot > mark. No new position until Jupiter ships Ondo GM token limit order support. 1 SOL max per position.
**PLTRx constraint:** EDS = 32 (Fragile). Post-catalyst bleed. No entry without new catalyst + complete 7-field card.

---

### Cardano Venture Layer Session

Trigger: Any NIGHT Glacier thaw, ATMA reward claim, Diffusion basket review, Pogun/Midnight update.

| Load Order | File                                      | Provides                              |
| ---------- | ----------------------------------------- | ------------------------------------- |
| 1          | `2026-06-02_MRB_cardano-venture-layer.md` | VEI scores, redemption framework      |
| 2          | `2026-05-31_MRB_claude-memory.md`         | Capital framework (if ADA deployment) |

**Default action on load:** Redeem → Assess Pogun status → Rotate to ADA unless catalyst confirms.

### Cardano Leios Scalability Session (New)

**Trigger:** Leios testnet/mainnet updates, Midnight synergies, ADA staking/scale reviews.

| Load Order | File                                                 | Provides                                                                                 |
| ---------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| 1          | `2026-06-24_MRB_Cardano.Leios.Scalability_Review.md` | Leios throughput uplift, Midnight/Hydra stack, ADA staker impact, scalability comparison |
| 2          | `2026-06-02_MRB_cardano-venture-layer.md`            | Existing Cardano venture context                                                         |

**EDS**: 85/100 (High). **Signal**: HOLD. Maintain staking. Monitor Musashi Dojo metrics.

---

## Key System Change Summary

### New MRB Added (2026-06-24)

**Cardano Leios Scalability Review** — Leios parallel consensus + Midnight privacy for mass adoption. Integrated into rsky.crv runtime. ADA staking thesis reinforced.

---

### Brief Daemon Session

Trigger: Any modification to `brief_daemon.py`, Task Scheduler issues, daemon not running,
`brief-report.md` output review, or pipeline architecture changes.

| Load Order           | File                                           | Provides                                          |
| -------------------- | ---------------------------------------------- | ------------------------------------------------- |
| 1                    | `2026-06-13_MRB_brief-daemon-pipeline.md`      | Daemon architecture + pipeline state              |
| 2                    | `2026-06-16_SESSION_UPDATE.md`                 | Groq injection, headlines gate, regime gate       |
| 3                    | `2026-06-17_MRB_brief-daemon-pipeline.md`      | BASE scope fix, scalp_engine regime gate          |
| 4                    | `2026-06-18_MRB_brief-daemon-pipeline.md`      | Verdict parser hardened, watchlist fixed          |
| 5                    | `2026-06-18_SESSION_UPDATE_2.md`               | Jupiter v3 migration, scalp_engine Task Scheduler |
| 6 (if verdict logic) | `2026-06-11_MRB_asi1-briefjson-integration.md` | System prompt + gate logic                        |

**Constraint:** Do not load for capital decision, trade evaluation, or Morning Brief sessions.
**`run_brief.bat` retired** — daemon owns the full loop.
**Escalation rule:** If daemon fails across 2+ boot cycles → check `LastTaskResult` via `Get-ScheduledTaskInfo -TaskName "brief_daemon"` before touching code.

---

### Scalp Arbitration Session

Trigger: Any modification to `scalp-shortlist.json` handoff, `bridge.py --mode scalp`, `verdict.json` schema, `event_log.jsonl`, or Telegram verdict dispatch format.

| Load Order           | File                                           | Provides                                              |
| -------------------- | ---------------------------------------------- | ----------------------------------------------------- |
| 1                    | `2026-06-25_SESSION_UPDATE_5.md`               | All 4 changes complete — pipeline verified production |
| 2                    | `2026-06-21_SESSION_UPDATE_4.md`               | Change 3 complete — heuristic parser, architecture    |
| 3                    | `2026-06-19_SESSION_UPDATE_3.md`               | Arbitration architecture + build sequence             |
| 4                    | `2026-06-13_MRB_brief-daemon-pipeline.md`      | Daemon orchestration patterns                         |
| 5 (if verdict logic) | `2026-06-11_MRB_asi1-briefjson-integration.md` | System prompt + gate logic                            |

**Current build state:** All 4 changes complete. Pipeline in verified production state.
**Constraint:** Do not load for capital decision, Morning Brief, or Brief Daemon sessions.
**ASI1 behavior locked:** Does not comply with `FINAL_VERDICT:` format or `max_tokens`. Heuristic parser (APPROVE/HOLD/REJECT keywords) is the active Strategy 2.

---

### Morning Brief Session

| Load Order | File                                           | Provides                                               |
| ---------- | ---------------------------------------------- | ------------------------------------------------------ |
| 1          | `2026-05-31_MRB_tokens.md`                     | Daily monitoring obligations                           |
| 2          | `2026-06-20_MRB_physical-ai-humanoid-watch.md` | Physical AI listing surveillance (12-company universe) |
| On-demand  | Relevant MRB                                   | Context-specific review                                |

---

### Physical AI / Humanoid Robotics Forward Watch Session

Trigger: Any humanoid robotics news, RoboStrategy feed update, or Jupiter new listing check.

| Load Order | File                                           | Provides                                                    |
| ---------- | ---------------------------------------------- | ----------------------------------------------------------- |
| 1          | `2026-06-20_MRB_physical-ai-humanoid-watch.md` | VEI_synth scores + 12-company universe + surveillance rules |
| 2          | `2026-05-31_MRB_claude-memory.md`              | Capital framework (if listing occurs)                       |
| 3          | `2026-05-31_MRB_tokens.md`                     | Position card template reference                            |

**Escalation rule:** If any humanoid xStock is confirmed listed → immediately switch to Jupiter Synthetics Session load order and begin 7-field Position Evaluation Card.
**TSLAx alert:** Optimus ramp is an active catalyst on an existing position with no documented exit thesis — open vulnerability. Check mark/spot spread on any Optimus news.

---

### HARNESS Architecture Session

Trigger: Any modification to HARNESS.md, HARNESS_INVARIANTS.md, addition of a new enforcement gate, elevation of L2 material to operational status, or review of the split enforcement architecture.

| Load Order | File                                         | Provides                                          |
| ---------- | -------------------------------------------- | ------------------------------------------------- |
| 1          | `2026-06-10_MRB_HARNESS_invariants-layer.md` | Split architecture decision + gate system context |

**Do not load for capital decision or research sessions.** This session type governs system architecture only.

---

### ASI:One Integration Session

Trigger: Any session involving the r$ky-Finance Analyst Agent on ASI:One, `brief.json` pipeline integration, system prompt development, or agent-to-agent routing via uAgents / Agentverse.

| Load Order                            | File                                           | Provides                                              |
| ------------------------------------- | ---------------------------------------------- | ----------------------------------------------------- |
| 1                                     | `2026-06-11_MRB_asi1-briefjson-integration.md` | Integration test state + step sequence + gap analysis |
| 2 (if capital verdict logic involved) | `2026-05-31_MRB_claude-memory.md`              | Capital framework + gate logic reference              |

**Constraint:** ASI:One = interactive shell only. All programmable logic stays in `rsky.crv`.
**Do not load for capital decision, trade evaluation, or Morning Brief sessions.**

---

### Cosmos / Gno.land Experimental Watch Session

Trigger: Any GNOT transfer unlock announcement, GovDAO vote, GnoSwap listing confirmation, or gno.land ecosystem update.

| Load Order              | File                                               | Provides                        |
| ----------------------- | -------------------------------------------------- | ------------------------------- |
| 1                       | `2026-06-23_MRB_gnoland-gnot-uniqueness-UPDATE.md` | GNOT + GnoSwap Testnet 13 state |
| 2 (if capital decision) | `2026-05-31_MRB_claude-memory.md`                  | Capital framework               |

**Testnet state (2026-06-23):** Rank #47, $2,027.18 portfolio, 16 LP positions, GnoSwap Testnet 13 active.
**Escalation rule:** On transfer unlock confirmation → re-classify GNOT to Research State and begin 7-field Position Evaluation Card.
**GNS flag:** Live price ($0.969), $211M TVL, 30.65% xGNS APR — monitor for mainnet launch as separate position candidate.

---

### Gno.land / Akkadia Session

Trigger: Any Akkadia alpha update, AI-agent integration news on Gno.land, BROT/Blockrot activity, or on-chain virtual world development.

| Load Order | File | Provides |
|---|---|---|
| 1 | `2026-06-25_MRB_Gnoland_Akkadia.Review.md` | Akkadia thesis, agent architecture, BROT assessment |
| 2 | `2026-06-23_MRB_gnoland-gnot-uniqueness-UPDATE.md` | GNOT testnet state + mainnet hold rules |
| 3 (if capital decision) | `2026-05-31_MRB_claude-memory.md` | Capital framework |

**Signal:** HOLD. No capital deployment until agent persistence + user retention metrics visible.
**BROT constraint:** Experimental only. Not infrastructure-grade. Reassess on maturity improvement.
**Escalation condition:** Agent persistence + user retention confirmed in Akkadia → re-evaluate signal from HOLD to Research State entry.

---

### RWA / MANTRA-NVNM Session

Trigger: Any NVNM Chain update, MANTRA staking metrics, Inveniam ecosystem news, or fee flow disclosure.

| Load Order | File                                         | Provides                                                 |
| ---------- | -------------------------------------------- | -------------------------------------------------------- |
| 1          | `2026-06-16_NVNM_MANTRA_Review.md`           | Acquisition thesis, bull/bear case, monitoring checklist |
| 2          | `[[2026-06-01_MRB_cosmos-l3-venture-layer]]` | Cosmos ecosystem context                                 |
| 3          | `2026-05-31_MRB_claude-memory.md`            | Capital framework                                        |

**Thesis status:** Strategic outlook improved. Token value capture to MANTRA stakers unconfirmed. Long-duration speculative position — 3–10 year horizon. Key unresolved: do NVNM fees flow to MANTRA validators?

---

### Nuclear On-Chain Watch Session

Trigger: First nuclear synthetic listing on Jupiter (OKLOx, CCJx, SMRx, LEUx), first Hyperliquid nuclear perp, or Securitize nuclear tokenized equity onboarding.

| Load Order | File                                         | Provides                                  |
| ---------- | -------------------------------------------- | ----------------------------------------- |
| 1          | `2026-06-05_MRB_nuclear_onchain_exposure.md` | Observation framework + trigger hierarchy |
| 2          | `2026-05-31_MRB_claude-memory.md`            | Capital framework                         |

**Current status:** OBSERVE only. Zero nuclear synthetics on Solana as of 2026-06-05. Trigger hierarchy: xStock listing (Rank 1) > Hyperliquid perp (Rank 2) > Securitize regulated listing (Rank 3) > ETF synthetic (Rank 4).

---

## Full MRB Registry

### Active MRBs

#### [[2026-05-31_MRB_tokens]]

**Type:** Experimental Token Position Cards + Deployment Status
**Template:** ✅ MRB_v1.2
**Status:** Active
**Created:** 2026-05-31
**Updated:** 2026-06-05

**Covers:**

- 7-field Position Evaluation Cards for all L3 synthetic token positions
- ANTHROPICx, PLTRx, NEURALINKx, NBISon, NVDAx, TSLAx, GOOGLx, elizaOS
- Synthetic asset cycle signature (confirmed on ANTHROPICx)
- EDS = 52/100 (Partial Determinism)

**Feeds Into:** `[[2026-05-31_MRB_claude-memory]]`
**Feeds From:** `[[2026-06-02_MRB_mark.price.execution.rules]]`, `[[2026-05-31_MRB_jupiterdex-defi-legitimacy]]`
**Storage Path:** `04-Claude\memory\mrb\2026-05-31_MRB_tokens.md`

---

#### [[2026-06-01_MRB_ondo-synthetic-execution]]

**Type:** Execution Infrastructure Research
**Template:** ✅ MRB_v1.2
**Status:** Active — HOLD
**Created:** 2026-06-01

**Covers:**

- Ondo GM tokens: JIT routing, not mark-anchored execution
- NBISon entry test trade: 9.65% slippage above mark at fill
- Spot/mark divergence is the true entry cost driver
- Limit orders not supported for Ondo GM tokens on Jupiter (as of 2026-06-01)
- PLTRon: ineligible (85% concentration, RFQ only)
- NVDAon: too liquid for early-bird edge thesis

**Key Rules Encoded:**

- No entry when spot > mark
- 1 SOL maximum per Ondo synthetic
- No new positions until Jupiter ships Ondo GM limit order support
- JIT active Sun 8PM ET → Fri 8PM ET only
- SL: -10% / TP: +10–20% / 7-day expiry

**Feeds Into:** `[[2026-05-31_MRB_claude-memory]]`
**Storage Path:** `04-Claude\memory\mrb\2026-06-01_MRB_ondo-synthetic-execution.md`

---

#### [[2026-06-02_MRB_cardano-venture-layer]]

**Type:** Venture Efficiency Evaluation
**Template:** ✅ MRB_v1.2
**Status:** Active — EDS 88/100
**Created:** 2026-06-02

**Covers:**

- VEI scoring: Diffusion Basket 51.9 (HOLD), NIGHT 51.15 (MAINTAIN YIELD), ATMA 22.5 (CLEANUP), long-tail <30 (CLEANUP)
- NIGHT Glacier allocation = zero-cost-basis, not debt
- Redemption logic: Redeem → Assess Pogun → Rotate to ADA unless catalyst confirms
- Primary future catalyst: Pogun launch + Bitcoin liquidity via Midnight

**Feeds Into:** `[[2026-05-31_MRB_claude-memory]]`
**Storage Path:** `04-Claude\memory\mrb\2026-06-02_MRB_cardano-venture-layer.md`

---

#### [[2026-06-03_MRB_PLTRx-trade-debrief]]

**Type:** Trade Debrief + Protocol Violation Log
**Template:** ✅ MRB_v1.2
**Status:** Active — RESEARCH STATE
**Created:** 2026-06-03

**Covers:**

- PLTRx pre-trade checklist returned REJECT — bypassed by operator
- Entry at $147.61 → exit $140.45 → +0.07% SOL → protocol violation → lucky, not skilled
- Pre-catalyst vs post-catalyst trade structure distinction established
- EDS = 32/100 (Fragile Determinism) — Freeze Auth + Mint Auth + 99% concentration
- PLTRx returns to Research State; re-entry requires new catalyst + complete 7-field card + liquidity >$150K

**Key Rule Encoded:** Marginal positive outcomes from protocol violations are more dangerous than losses — do not use as permission for future bypasses.

**Feeds Into:** `[[2026-05-31_MRB_tokens]]`, `[[2026-05-31_MRB_claude-memory]]`
**Feeds From:** `[[2026-06-02_MRB_mark.price.execution.rules]]`
**Storage Path:** `04-Claude\memory\mrb\2026-06-03_MRB_PLTRx-trade-debrief.md`

---

#### [[2026-06-05_MRB_weekly-review-rotation-pipeline]]

**Type:** Capital Framework + Rotation Pipeline
**Template:** ✅ MRB_v1.2
**Status:** Active
**Created:** 2026-06-05

**Covers:**

- 13 SOL → 20–25 SOL sequential rotation (3 trades, summer–fall 2026)
- Trade 1: HYPE — 7-field card complete, WATCHLIST status
  - Entry triggers: $56–58 zone OR $62 daily close + 48h positive net vol
  - Invalidation: daily close below $52
  - Thesis completion: $100 (sell 50%) / $110 (trail)
  - Time expiry: 60 days from entry
  - Max allocation: 3 SOL reserve
  - EDS: 72/100 (High Determinism)
- Trade 2 candidates: ANTHROPICx cycle 2, Nuclear proxy, HyperEVM beta
- Trade 3 candidates: RWA protocol launch, ANTHROPICx cycle 2
- BTC recovery thesis affirmed; regime = capitulation formation (week of Jun 2–5)
- HYPE institutional stack: Grayscale ETF + Bitwise $41.8M AUM + CFTC perps

**Standing constraints:**

- 10 SOL JitoSOL = base layer, never touched
- 3 SOL reserve = only rotation capital
- Sequential rotation: profits from each trade rotate directly into next candidate

**Feeds Into:** `[[2026-05-31_MRB_claude-memory]]`, `[[2026-05-31_MRB_protocols]]`, `[[2026-05-31_MRB_tokens]]`
**Storage Path:** `04-Claude\memory\mrb\2026-06-05_MRB_weekly-review-rotation-pipeline.md`

---

#### [[2026-06-05_MRB_nuclear_onchain_exposure]]

**Type:** Narrative Infrastructure Monitoring / Forward Watch
**Template:** MRB (narrative format)
**Status:** Active — OBSERVE
**Created:** 2026-06-05

**Covers:**

- Nuclear narrative active in TradFi; zero on-chain Solana exposure confirmed
- Trigger hierarchy: xStock listing > Hyperliquid perp > Securitize regulated > ETF synthetic
- 72-hour rule pre-armed on any listing discovery
- Observation window: open until first nuclear synthetic appears

**Storage Path:** `04-Claude\memory\mrb\2026-06-05_MRB_nuclear_onchain_exposure.md`

---

#### [[2026-06-09_MRB_harness-deploy-vault-cleanup]]

**Type:** System Architecture + Vault Maintenance
**Template:** MRB (session record)
**Status:** Complete
**Created:** 2026-06-09

**Covers:**

- HARNESS.md v1.0 created (predates v1.2 — superseded by 2026-06-10 session)
- CLAUDE.md v2.0 rewritten as router + bootstrap loader
- Skills directory consolidated to 7 canonical files
- Legacy files archived to `00-Inbox/temporary/skill/`

**Note:** HARNESS.md was subsequently upgraded to v1.2 in the 2026-06-10 session. This MRB documents the initial deploy; the 2026-06-10 MRB governs the current architecture.

**Storage Path:** `04-Claude\memory\mrb\2026-06-09_MRB_harness-deploy-vault-cleanup.md`

---

#### [[2026-06-10_MRB_gnoland-gnot-uniqueness]] → SUPERSEDED

**Status:** SUPERSEDED by `2026-06-23_MRB_gnoland-gnot-uniqueness-UPDATE.md`
**Storage Path:** `04-Claude\memory\mrb\2026-06-10_MRB_gnoland-gnot-uniqueness.md`

---

#### [[2026-06-23_MRB_gnoland-gnot-uniqueness-UPDATE]]

**Type:** Forward Surveillance / Testnet Active
**Template:** ✅ MRB_v1.2
**Status:** Active — Testnet Observation + Mainnet Hold
**Created:** 2026-06-10 (original) / Updated 2026-06-23
**Supersedes:** `2026-06-10_MRB_gnoland-gnot-uniqueness.md`

**Covers:**

- Mainnet GNOT: 53.42 GNOT airdrop, zero-cost-basis, EDS = 0, transfer lock status unconfirmed
- GnoSwap Testnet 13: Rank #47 (77.01 pts), $2,027.18 portfolio, 16 LP positions, Staking dominant (96% of score)
- Key efficiency levers: close dead positions (0% APR), open GNOT/GNS 1,419% APR, cycle USDT/DAI for swap volume
- GNS flag: live $0.969 price, $211M TVL, 30.65% governance APR — monitor for mainnet launch as separate candidate

**Feeds Into:** `[[2026-05-31_MRB_tokens]]` (when mainnet unlocks or listing confirmed)
**Storage Path:** `04-Claude\memory\mrb\2026-06-23_MRB_gnoland-gnot-uniqueness-UPDATE.md`

---

#### PHMN (POSTHUMAN DAO)

**Type:** Observational Record
**Template:** Narrative (no 7-field card — observational only)
**Status:** Observational — No Allocation Intent
**EDS:** 0 (Non-Deterministic)
**Created:** 2026-06-23

**Covers:**

- POSTHUMAN validator DAO governance token, 40+ networks, max supply 131,072
- Revenue accrual model: 20% commission → buybacks + LP
- Micro-cap, illiquid — outside Core and Rotational tiers
- No 7-field card. No position. No escalation path currently defined.

**Escalation condition:** Liquidity depth crosses threshold + validator metrics confirm sustained revenue accrual → re-classify to Research State, begin 7-field card
**Storage Path:** `00-Inbox\memory\2026-06-23_MRB_PHMN.Crypto_Overview.md`

---

#### [[2026-06-25_MRB_Gnoland_Akkadia.Review]]

**Type:** Ecosystem Research — Virtual World / AI-Agent Architecture
**Template:** ✅ MRB_v1.2
**Status:** Active — HOLD
**EDS:** 45/100 (Partial Determinism)
**Created:** 2026-06-25

**Covers:**

- Akkadia alpha confirms Gno.land is already executing the virtual-world thesis
- Strategic next layer: AI-native coordination, agent-owned economies, autonomous quest generation
- Blockrot/BROT (Solana): speculative, narrative-dependent, not infrastructure-grade
- Compelling autonomous world threshold: ~25–50 persistent agents with memory + goals
- Interaction density > agent count as the quality metric
- Economic outcomes non-deterministic; scale only after agent interactions prove engaging

**Escalation condition:** Agent persistence + user retention confirmed in Akkadia → re-evaluate from HOLD to Research State entry.
**Feeds Into:** `[[2026-06-23_MRB_gnoland-gnot-uniqueness-UPDATE]]`
**Storage Path:** `00-Inbox\memory\2026-06-25_MRB_Gnoland_Akkadia.Review.md`

---

#### [[2026-06-10_MRB_HARNESS_invariants-layer]]

**Type:** System Architecture Decision
**Template:** ✅ MRB_v1.2
**Status:** Active
**Created:** 2026-06-10
**Promotion Threshold:** 14 days

**Covers:**

- Split Enforcement Architecture (Option D)
- HARNESS_INVARIANTS.md as L1 enforcement gate, 10 gates across 4 categories
- Governance halts (not terminal failures)
- Role isolation reformulated for single-session enforceability

**Storage Path:** `04-Claude\memory\mrb\2026-06-10_MRB_HARNESS_invariants-layer.md`

---

#### [[2026-06-11_MRB_asi1-briefjson-integration]]

**Status:** Active — integration complete, pipeline operational
**Type:** Coding Integration Directive
**Template:** ✅ MRB_v1.2
**Promotion Threshold:** 14 days

**Covers:**

- 7-step integration test sequence
- EDS = 72/100 (High Determinism)
- System prompt must prohibit autonomous capital allocation

**Storage Path:** `04-Claude\memory\mrb\2026-06-11_MRB_asi1-briefjson-integration.md`

---

#### [[2026-06-13_MRB_brief-daemon-pipeline]]

**Type:** Coding Integration — Daemon Architecture
**Template:** ✅ MRB_v1.2
**Status:** Active — operational (see session updates for current state)
**Created:** 2026-06-13
**Promotion Threshold:** 14 days

**Covers:** Base daemon architecture — `brief_daemon.py`, hybrid timer/file watcher, `brief-report.md`.
**Current state:** See session updates 2026-06-16 through 2026-06-21 for full pipeline state.

**Storage Path:** `04-Claude\memory\mrb\2026-06-13_MRB_brief-daemon-pipeline.md`

---

#### [[2026-06-16_SESSION_UPDATE]] (Brief Daemon)

**Type:** Session Update — appended to `2026-06-13_MRB_brief-daemon-pipeline`
**Status:** Checkpointed
**Created:** 2026-06-16

**Covers:**

- brief.py: NameError fix, set JSON bug, Groq fallback added
- bridge.py: regime gate deployed (EXECUTE on UNKNOWN blocked), TIMEOUT=60s
- scalp_engine.py: built from scratch (DexScreener, 32 assets, Telegram alerts)
- watchlist.json: 32/32 mints resolved
- GROQ_API_KEY injection: pending Task Scheduler (resolved 2026-06-17)
- INTERVAL: 300 → 10800 (3h)
- headlines_changed() gate: wired

**Storage Path:** `04-Claude\memory\mrb\2026-06-16_SESSION_UPDATE.md`

---

#### [[2026-06-16_NVNM_MANTRA_Review]]

**Type:** Investment Thesis Review — RWA / AI Infrastructure
**Template:** MRB (narrative format)
**Status:** Active — Long-duration Speculative
**Created:** 2026-06-16

**Covers:**

- Inveniam acquisition of MANTRA: vertical integration of AI + RWA stack
- NVNM Chain inherits security from MANTRA via Interchain Security
- Bull: captive security demand, regulatory moat, institutional positioning
- Bear: token value capture unproven, enterprise revenue leakage risk
- Key unresolved: do NVNM fees flow to MANTRA validators?
- Classification: Strategic AI + RWA Infrastructure Option, 3–10yr horizon

**Feeds From:** `[[2026-06-01_MRB_cosmos-l3-venture-layer]]`, `[[2026-05-31_MRB_claude-memory]]`
**Storage Path:** `04-Claude\memory\mrb\2026-06-16_NVNM_MANTRA_Review.md`

---

#### [[2026-06-17_MRB_brief-daemon-pipeline]] (Session Update)

**Type:** Session Update — appended to `2026-06-13_MRB_brief-daemon-pipeline`
**Status:** Checkpointed
**Created:** 2026-06-17

**Covers:**

- brief.py BASE scope bug fixed (NameError: BASE not defined at import)
- headlines_changed() gate confirmed operational
- scalp_engine.py regime gate deployed (P2): T1 + RISK-ON → alert; T1 + UNKNOWN → suppressed
- `flags = flags + ["REGIME_CONFLICT"]` for T1 + RISK-OFF

**Storage Path:** `04-Claude\memory\mrb\2026-06-17_MRB_brief-daemon-pipeline.md`

---

#### [[2026-06-18_MRB_brief-daemon-pipeline]] (Session Update)

**Type:** Session Update — appended to `2026-06-13_MRB_brief-daemon-pipeline`
**Status:** Checkpointed
**Created:** 2026-06-18

**Covers:**

- watchlist.json: 16/32 missing assets diagnosed — 6 wrong mints, 10 synthetics excluded
- `exclude_from_scalp` flag added to 15 synthetic assets
- bridge.py: verdict volatility root cause fixed — substring match → whole-line equality
- system-prompt-v1.3.md: `FINAL_VERDICT:` terminal instruction added
- EDS classification for verdict parser: format contract over fuzzy fallback

**Storage Path:** `04-Claude\memory\mrb\2026-06-18_MRB_brief-daemon-pipeline.md`

---

#### [[2026-06-18_SESSION_UPDATE_2]] (Brief Daemon Continuation)

**Type:** Session Update — continuation of 2026-06-18
**Status:** Checkpointed — pipeline fully automated
**Created:** 2026-06-18

**Covers:**

- Jupiter Price API v2 → v3 migration (v2 deprecated Oct 2025)
- Parser updated: `"data"` wrapper removed, `usdPrice` field
- JUP_API_KEY: free tier from portal.jup.ag, injected via brief_daemon.py
- scalp_engine Task Scheduler registration: AtLogOn, LastTaskResult 267009
- **Pipeline fully automated** — no manual intervention required as of this session

**Storage Path:** `04-Claude\memory\mrb\2026-06-18_SESSION_UPDATE_2.md`

---

#### [[2026-06-19_SESSION_UPDATE_3]] (Scalp Arbitration)

**Type:** Session Update — Scalp Arbitration Architecture
**Status:** Change 1 complete — monitoring for signal population
**Created:** 2026-06-19

**Covers:**

- brief.json contract v1.0: four authority classes (GATE / COLLECT / CANDIDATE / IGNORE)
- Scalp arbitration architecture locked: scalp_engine → shortlist → daemon → bridge → verdict → Telegram
- T1+T2 → shortlist (cap 5) → ASI1 arbitration; RISK → direct Telegram; IGNORE → dropped
- Change 1 (scalp-shortlist.json write path): ✅ complete
- Content hash gate, event_log.jsonl schema, target Telegram format defined

**Remaining:** Changes 2 (daemon shortlist watcher), 3 (bridge --mode scalp), 4 (verdict Telegram dispatch)
**Feeds Into:** `[[2026-06-13_MRB_brief-daemon-pipeline]]`
**Storage Path:** `04-Claude\memory\mrb\2026-06-19_SESSION_UPDATE_3.md`

---

#### [[2026-06-20_MRB_physical-ai-humanoid-watch]]

**Type:** Forward Surveillance — Universe Expansion
**Template:** ✅ MRB_v1.2
**Status:** Active — Surveillance Only (supersedes 2026-06-04 version)
**Created:** 2026-06-20
**Supersedes:** `2026-06-04_MRB_physical-ai-humanoid-watch.md`
**Promotion Threshold:** 14 days

**Covers:**

- Universe expanded: 4 → 12 companies
- Full synthetic ticker watch table with Jupiter listing status
- Zero humanoid xStocks listed as of 2026-06-20 — gap persists
- Tesla/Optimus: existing TSLAx position has no stop or exit thesis — open vulnerability
- Agibot is correct Chinese unit-volume leader (5,168 units 2025), not Unitree
- Agility Robotics RaaS model structurally superior for synthetic thesis
- Narrative compression risk: one listing triggers attrition across all others
- All EDS = 0 until listing confirmed

**Feeds Into:** `[[2026-05-31_MRB_tokens]]` (when listing occurs)
**Feeds From:** `[[2026-05-31_MRB_claude-memory]]`, `[[2026-05-31_MRB_jupiterdex-defi-legitimacy]]`
**Storage Path:** `04-Claude\memory\mrb\2026-06-20_MRB_physical-ai-humanoid-watch.md`

---

#### [[2026-06-21_SESSION_UPDATE_4]] (Scalp Arbitration)

**Type:** Session Update — Scalp Arbitration
**Status:** Change 3 complete — Change 4 unblocked
**Created:** 2026-06-21

**Covers:**

- Changes 2 + 3 resolved
- ASI1 root cause: ignores FINAL_VERDICT format + max_tokens — heuristic parser built
- Heuristic parser: APPROVE → EXECUTE, HOLD → WATCHLIST, REJECT → REJECT, fallback → RESEARCH_STATE
- verdict.json now returns real non-RESEARCH_STATE verdicts: ZEC=EXECUTE, CBBTC=EXECUTE confirmed
- Telegram dispatcher built: state-gated, signature deduplication, ENTER_THRESHOLD=45 (P95)
- scalp_engine spam resolved: send_telegram removed from unconditional cycle end

**Remaining:** Change 4 complete — see SESSION_UPDATE_5
**Feeds Into:** `[[2026-06-19_SESSION_UPDATE_3]]`
**Storage Path:** `04-Claude\memory\mrb\2026-06-21_SESSION_UPDATE_4.md`

---

#### [[2026-06-25_SESSION_UPDATE_5]] (Scalp Arbitration)

**Type:** Session Update — Scalp Arbitration + Dispatcher Hardening
**Status:** All 4 changes complete — pipeline verified production
**Created:** 2026-06-25

**Covers:**

- Change 4: `VerdictEventHandler` wired to `brief_daemon.py` — Option C transition gate
- Dispatcher hardened: state-based signature (action only), tier floors T1≥65/T2≥50, hysteresis hold until score < EXIT_THRESHOLD (25)
- `scalp-debug.txt` removed from `bridge.py` — debug artifact cleanup
- Regime display bug fixed: `results[-1]["regime"] = regime` in `scalp_engine.py`
- Data quality gate added in `fetch_dexscreener`: rejects pairs with priceChange > ±1000%
- Stale `last_sent_state.json` wiped on signature schema change
- Both Task Scheduler tasks confirmed running: `267009`

**Key learnings:**
- Hysteresis requires clean state file on deployment — mixed schema = false transitions = spam
- `save_state()` only called if `_dispatched = True` — state file must be inspected during dispatcher debugging
- Data quality gates belong at fetch layer, not scoring layer
- Regime must be explicitly attached to result dicts before dispatcher loop

**Feeds Into:** `[[2026-06-21_SESSION_UPDATE_4]]`
**Storage Path:** `04-Claude\memory\mrb\2026-06-25_SESSION_UPDATE_5.md`

---

```text
MRB_claude-memory (ROOT)

├── MRB_protocols
├── MRB_tokens
│   ├── ANTHROPICx
│   ├── PLTRx
│   │   └── MRB_PLTRx-trade-debrief (PROTOCOL VIOLATION LOG)
│   ├── NBISon
│   │   └── MRB_mark.price.execution.rules
│   │   └── MRB_ondo-synthetic-execution (JIT/spot-mark rules)
│   ├── PLTRon (Ondo — ineligible, RFQ only)
│   ├── NEURALINKx
│   ├── NVDAx
│   ├── TSLAx [OPTIMUS CATALYST OPEN — no exit thesis documented]
│   ├── GOOGLx
│   ├── GNOT (gno.land) [TESTNET ACTIVE — EDS 0 mainnet]
│   │   └── MRB_gnoland-gnot-uniqueness-UPDATE (2026-06-23)
│   │   └── MRB_Gnoland_Akkadia.Review (2026-06-25) [HOLD — agent persistence gate]
│   └── PHMN (POSTHUMAN DAO) [OBSERVATIONAL — EDS 0 — no allocation intent]
│
├── MRB_jupiterdex-defi-legitimacy
│
├── MRB_cosmos-l3-venture-layer
│   └── MRB_cardano-venture-layer (NIGHT/ATMA/Diffusion)
│   └── MRB_NVNM-MANTRA-Review (RWA/AI stack)
│
├── MRB_weekly-review-rotation-pipeline
│   └── HYPE Trade 1 (7-field card complete, WATCHLIST)
│   └── T2 candidates: ANTHROPICx cycle 2, Nuclear proxy, HyperEVM beta
│   └── T3 candidates: RWA launch, ANTHROPICx cycle 2
│
├── MRB_physical-ai-humanoid-watch (2026-06-20 — 12 companies) [FORWARD WATCH — EDS 0]
│   ├── FIGUREx (pre-listing, VEI 63.95 — HIGH priority)
│   ├── TSLAx/OPTIMUSx (existing instrument, catalyst window open)
│   ├── AGIBOTx (pre-listing, est. VEI 58–65 — China unit leader)
│   ├── AGILITYx (pre-listing, est. VEI 55–62 — RaaS model)
│   ├── NEURAx, UNITREEx, ATLASx (MEDIUM)
│   └── UBTECHx, GALBOTx, 1Xx, SUNDAYx (LOW/WATCH ONLY)
│
├── MRB_nuclear_onchain_exposure [FORWARD WATCH — zero listings]
│
├── MRB_HARNESS_invariants-layer [SYSTEM ARCHITECTURE]
│   ├── HARNESS.md (L0)
│   └── HARNESS_INVARIANTS.md (L1)
│
└── MRB_asi1-briefjson-integration [CODING INTEGRATION]
    ├── system-prompt-v1.3 (operational)
    └── MRB_brief-daemon-pipeline (base + 5 session updates)
        ├── brief_daemon.py (event-driven, AtLogOn)
        ├── brief.py (Gemini → Groq fallback, Jupiter v3, headlines gate)
        ├── bridge.py (regime gate, FINAL_VERDICT parser, --mode scalp)
        ├── scalp_engine.py (17 active assets, regime gate, dispatcher)
        ├── telegram_dispatcher.py (state-gated, tier floors T1≥65/T2≥50, hysteresis)
        ├── scalp-shortlist.json (T1+T2 candidates, cap 5)
        ├── verdict.json (heuristic parser: APPROVE/HOLD/REJECT)
        └── verdict.json → VerdictEventHandler → Telegram (Option C transition gate) ✅
```

---

## Key System Change Summary

### New MRB Added (2026-06-25)

**Gno.land Akkadia Review** — Akkadia alpha positions Gno.land in the virtual world / AI-agent space. Strategic thesis: autonomous agent economies > scripted NPC populations. BROT classified experimental. Signal: HOLD pending persistence metrics. New session type added.

### Pipeline Verified Production (2026-06-25)

Change 4 complete. VerdictEventHandler wired. Dispatcher hardened (tier floors T1≥65/T2≥50,
hysteresis, state-based signature). scalp-debug.txt removed. Regime display bug fixed.
cbBTC data quality gate added. Both Task Scheduler tasks running. SESSION_UPDATE_5 is now
the authoritative state for Scalp Arbitration Session load order.

### Observational Asset Added (2026-06-24)

**PHMN (POSTHUMAN DAO)** — Classified Observational, no allocation intent. EDS = 0. Registered in Active MRBs and dependency graph. No load order entry, no 7-field card. Escalation condition defined.

### New Session Type Added (2026-06-23)

**Cosmos / Gno.land Watch** — updated to reflect GnoSwap Testnet 13 active participation. MRB superseded to `2026-06-23_MRB_gnoland-gnot-uniqueness-UPDATE.md`. Mainnet rules unchanged (EDS = 0).

### MRB Superseded (2026-06-20)

**Physical AI / Humanoid Robotics** — `2026-06-20_MRB_physical-ai-humanoid-watch.md` supersedes June 4 version. Universe expanded 4 → 12 companies. Morning Brief Session load order updated.

### New Session Types Added (2026-06-19 / 2026-06-21)

**Scalp Arbitration Session** — governs scalp-shortlist.json handoff, bridge.py --mode scalp, verdict.json, Telegram verdict dispatch. Load SESSION_UPDATE_4 + SESSION_UPDATE_3 + base daemon MRB. Change 4 (VerdictEventHandler) is the sole remaining build item.

### Pipeline Fully Automated (2026-06-18)

Both `brief_daemon` and `scalp_engine` Task Scheduler tasks running at logon. No manual intervention required.

### New Session Types Added (2026-06-16)

**RWA/MANTRA-NVNM Session** — Inveniam acquisition of MANTRA creates new long-duration speculative position. Token value capture unconfirmed.

### New MRBs Added (2026-06-01 through 2026-06-09)

Ondo synthetic execution rules, Cardano venture layer VEI, PLTRx protocol violation debrief, Nuclear on-chain forward watch, HARNESS deploy/cleanup.

---

## Critical Insight

The system now separates:

"Can I understand this asset?"

from

"Can I reliably execute actions on this asset?"

from

"Does this asset exist yet?"

Three independent dimensions. Forward Watch MRBs address the third.

---

## MRB Capture Rule

Every completed session containing durable knowledge, decisions, workflows, frameworks, or project progress must be converted into an MRB and registered in this index.

---

## Template

Current Template: `MRB_v1_TEMPLATE.md`
Current Version: **MRB_v1.2**
Location: `D:\Users\RSky\Desktop\AI.ProFit\rsky.crv\04-Claude\memory\MRB_v1_TEMPLATE.md`
