# MRB INDEX — Memory Restoration Block Registry

**System:** Profit.OS — rsky.crv Knowledge Architecture
**Maintained By:** Claude (session-generated) + Alan (manual review)
**Target Directory:** `D:\Users\RSky\Desktop\AI.ProFit\rsky.crv\04-Claude\memory`
**Last Updated:** 2026-06-24
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

| Load Order | File                                           | Provides                                |
| ---------- | ---------------------------------------------- | --------------------------------------- |
| 1          | `2026-05-31_MRB_claude-memory.md`              | Capital framework + Profit.OS rules     |
| 2          | `2026-06-05_MRB_weekly-review-rotation-pipeline.md` | Trade 1 HYPE card + pipeline state |
| 3          | `2026-05-31_MRB_protocols.md`                  | HYPE protocol card                      |
| 4          | `2026-05-31_MRB_jupiterdex-defi-legitimacy.md` | Captive liquidity thesis                |

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

| Load Order | File                                           | Provides                              |
| ---------- | ---------------------------------------------- | ------------------------------------- |
| 1          | `2026-06-02_MRB_cardano-venture-layer.md`      | VEI scores, redemption framework      |
| 2          | `2026-05-31_MRB_claude-memory.md`              | Capital framework (if ADA deployment) |

**Default action on load:** Redeem → Assess Pogun status → Rotate to ADA unless catalyst confirms.

---

### Brief Daemon Session

Trigger: Any modification to `brief_daemon.py`, Task Scheduler issues, daemon not running,
`brief-report.md` output review, or pipeline architecture changes.

| Load Order | File | Provides |
|---|---|---|
| 1 | `2026-06-13_MRB_brief-daemon-pipeline.md` | Daemon architecture + pipeline state |
| 2 | `2026-06-16_SESSION_UPDATE.md` | Groq injection, headlines gate, regime gate |
| 3 | `2026-06-17_MRB_brief-daemon-pipeline.md` | BASE scope fix, scalp_engine regime gate |
| 4 | `2026-06-18_MRB_brief-daemon-pipeline.md` | Verdict parser hardened, watchlist fixed |
| 5 | `2026-06-18_SESSION_UPDATE_2.md` | Jupiter v3 migration, scalp_engine Task Scheduler |
| 6 (if verdict logic) | `2026-06-11_MRB_asi1-briefjson-integration.md` | System prompt + gate logic |

**Constraint:** Do not load for capital decision, trade evaluation, or Morning Brief sessions.
**`run_brief.bat` retired** — daemon owns the full loop.
**Escalation rule:** If daemon fails across 2+ boot cycles → check `LastTaskResult` via `Get-ScheduledTaskInfo -TaskName "brief_daemon"` before touching code.

---

### Scalp Arbitration Session

Trigger: Any modification to `scalp-shortlist.json` handoff, `bridge.py --mode scalp`, `verdict.json` schema, `event_log.jsonl`, or Telegram verdict dispatch format.

| Load Order | File | Provides |
|---|---|---|
| 1 | `2026-06-21_SESSION_UPDATE_4.md` | Change 3 complete — heuristic parser, architecture |
| 2 | `2026-06-19_SESSION_UPDATE_3.md` | Arbitration architecture + build sequence |
| 3 | `2026-06-13_MRB_brief-daemon-pipeline.md` | Daemon orchestration patterns |
| 4 (if verdict logic) | `2026-06-11_MRB_asi1-briefjson-integration.md` | System prompt + gate logic |

**Current build state:** Change 4 (VerdictEventHandler → Telegram dispatch) is the sole remaining item.
**Constraint:** Do not load for capital decision, Morning Brief, or Brief Daemon sessions.
**ASI1 behavior locked:** Does not comply with `FINAL_VERDICT:` format or `max_tokens`. Heuristic parser (APPROVE/HOLD/REJECT keywords) is the active Strategy 2.

---

### Morning Brief Session

| Load Order | File                                           | Provides                         |
| ---------- | ---------------------------------------------- | -------------------------------- |
| 1          | `2026-05-31_MRB_tokens.md`                     | Daily monitoring obligations     |
| 2          | `2026-06-20_MRB_physical-ai-humanoid-watch.md` | Physical AI listing surveillance (12-company universe) |
| On-demand  | Relevant MRB                                   | Context-specific review          |

---

### Physical AI / Humanoid Robotics Forward Watch Session

Trigger: Any humanoid robotics news, RoboStrategy feed update, or Jupiter new listing check.

| Load Order | File                                           | Provides                              |
| ---------- | ---------------------------------------------- | ------------------------------------- |
| 1          | `2026-06-20_MRB_physical-ai-humanoid-watch.md` | VEI_synth scores + 12-company universe + surveillance rules |
| 2          | `2026-05-31_MRB_claude-memory.md`              | Capital framework (if listing occurs) |
| 3          | `2026-05-31_MRB_tokens.md`                     | Position card template reference      |

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

| Load Order | File | Provides |
| --- | --- | --- |
| 1 | `2026-06-11_MRB_asi1-briefjson-integration.md` | Integration test state + step sequence + gap analysis |
| 2 (if capital verdict logic involved) | `2026-05-31_MRB_claude-memory.md` | Capital framework + gate logic reference |

**Constraint:** ASI:One = interactive shell only. All programmable logic stays in `rsky.crv`.
**Do not load for capital decision, trade evaluation, or Morning Brief sessions.**

---

### Cardano Leios Scalability Session (New)

**Trigger:** Leios testnet/mainnet updates, Midnight synergies, ADA staking/scale reviews.

| Load Order | File                                           | Provides |
| ---------- | ---------------------------------------------- | -------- |
| 1          | `2026-06-24_MRB_Cardano.Leios.Scalability_Review.md` | Leios throughput uplift, Midnight/Hydra stack, ADA staker impact, scalability comparison |
| 2          | `2026-06-02_MRB_cardano-venture-layer.md`      | Existing Cardano venture context |

**EDS**: 85/100 (High). **Signal**: HOLD. Maintain staking. Monitor Musashi Dojo metrics.

---

## Key System Change Summary

### New MRB Added (2026-06-24)
**Cardano Leios Scalability Review** — Leios parallel consensus + Midnight privacy for mass adoption. Integrated into rsky.crv runtime. ADA staking thesis reinforced.

---

## MRB Capture Rule

Every completed session containing durable knowledge, decisions, workflows, frameworks, or project progress must be converted into an MRB and registered in this index.

---

## Template

Current Template: `MRB_v1_TEMPLATE.md`
Current Version: **MRB_v1.2**
Location: `D:\Users\RSky\Desktop\AI.ProFit\rsky.crv\04-Claude\memory\MRB_v1_TEMPLATE.md`