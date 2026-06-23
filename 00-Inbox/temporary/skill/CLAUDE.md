# CLAUDE.md — Router & Bootstrap Loader

**Version:** CLAUDE_v2.0
**Location:** `D:\Users\RSky\Desktop\AI.ProFit\rsky.crv\04-Claude\CLAUDE.md`
**Last Updated:** 2026-06-08
**Role:** Entry point. Routes Claude to the correct system files, skills, and vault locations.
**Does NOT contain:** Behavioral rules, execution logic, research methodology, user preferences.

---

## 1. System File References

Load these in order at session start.

| Priority | File | Location | Purpose |
|----------|------|----------|---------|
| 1 | SYSTEM.md | `04-Claude\SYSTEM.md` | Operating constitution — purpose, hierarchy, decision rules |
| 2 | HARNESS.md | `04-Claude\HARNESS.md` | Execution protocol — loop, tool permissions, state persistence, error recovery |
| 3 | This file | `04-Claude\CLAUDE.md` | Vault discovery, skill routing, startup sequence |

**Rule:** SYSTEM.md and HARNESS.md take precedence over anything in this file. If conflict exists, defer to SYSTEM.md.

---

## 2. Vault Map

```
rsky.crv\
├── 00-Inbox\          ← Raw captures, unprocessed inputs
├── 01-Market\         ← Briefs, narratives, watchlist, theses
│   ├── briefs\
│   ├── narratives\
│   ├── theses\
│   └── watchlist\
├── 02-Research\       ← Protocol, token, macro, chain research
│   ├── chains\
│   ├── macro\
│   ├── protocols\
│   └── tokens\
├── 03-Journal\        ← Trade logs, archive logs
├── 04-Claude\         ← System files, skills, memory
│   ├── CLAUDE.md      ← THIS FILE
│   ├── SYSTEM.md
│   ├── HARNESS.md
│   ├── memory\
│   │   └── mrb\       ← MRB session artifacts
│   └── skills\        ← Skill files 01–08
└── 05-Library\        ← Knowledge system (Library.OS)
    ├── lib.mrb\
    │   └── intelligence\  ← INTEL_ daily briefs
    ├── books\
    ├── papers\
    └── frameworks\
```

---

## 3. Skill Registry

| # | Skill ID | Activation Domain | File |
|---|----------|------------------|------|
| 01 | `rsky-profit-os` | Portfolio decisions, macro regime, trade evaluation, deployment eligibility | `skills\01_brief.md` |
| 02 | `rsky-finance-research` | Token research, thesis construction, protocol evaluation, market intelligence | `skills\02_weekly.research.session.md` |
| 03 | `personal-librarian` | Books, papers, articles, knowledge extraction, LIB.MRB creation, reading queue | `skills\03_token.research.template.md` |
| 04 | `obsidian-architect` | Vault structure, templates, Dataview queries, PKM design | `skills\04_claude.instruction.md` |
| 05 | `code-project-instructions` | Code project scaffolding, file structure, project-level coding conventions | `skills\05_code-project-instructions.md` |
| 06 | `profit-os_synthetic-token-monitor` | Synthetic token monitoring, Jupiter DEX position tracking, token metrics | `skills\06_profit-os_synthetic-token-monitor.md` |
| 07 | `multi-agent-harness` | Agent orchestration, multi-agent pipeline design, harness architecture | `skills\07_multi_agent_harness.md` |
| 08 | `body-health` | Longevity, biomarkers, health interventions, recovery, healthspan optimization | `skills\08_body-health.md` |
| 09 | `coding-coach` | Scripts, automation, debugging, system architecture, MCP integration | `skills\09_coding-coach.md` |

---

## 4. Routing Rules

**Priority override:** If input has any portfolio or capital allocation implication → route to `rsky-profit-os` first, regardless of other signals.

**Ambiguous input:** If two skills are plausible → do not blend. Classify as OBSERVE-INCOMPLETE. Ask Alan to confirm routing before proceeding.

**Harness-governed routing:** Full routing logic (including pipeline definitions) lives in `HARNESS.md` Section 1.2. This file only declares the skill registry. Execution behavior is defined by the harness.

---

## 5. File Discovery

| Content Type | Canonical Location |
|-------------|-------------------|
| Operating constitution | `04-Claude\SYSTEM.md` |
| Execution harness | `04-Claude\HARNESS.md` |
| MRB session artifacts | `04-Claude\memory\mrb\` |
| Daily intel briefs | `05-Library\lib.mrb\intelligence\` |
| Token position cards | `02-Research\tokens\` |
| Protocol research | `02-Research\protocols\` |
| Macro research | `02-Research\macro\` |
| Trade log | `03-Journal\` |
| Reading queue | `05-Library\LIB.READING.QUEUE.md` |
| MRB index | `05-Library\LIB.MRB.INDEX.md` |
| MRB template | `05-Library\LIB.MRB.TEMPLATE.md` |
| Workflow definitions | `05-Library\lib.mrb\intelligence\RSKY.GMAIL_SUMMARY.md` |

---

## 6. Startup Sequence

On session open, Claude executes in this order:

```
1. Load SYSTEM.md         → establish purpose + hierarchy
2. Load HARNESS.md        → establish execution constraints
3. Load CLAUDE.md         → resolve vault + skill routing
4. Classify input         → OBSERVE (HARNESS Section 1.1)
5. Route to skill         → ROUTE (HARNESS Section 1.2)
6. Load skill file        → THINK (HARNESS Section 1.3)
7. Load relevant MRB(s)   → max 2, domain-relevant
8. Execute                → ACT (HARNESS Section 1.4)
9. Checkpoint             → CHECKPOINT (HARNESS Section 1.5)
```

---

## 7. Daily Workflow Entry Points

| Trigger | Pipeline | Governed By |
|---------|----------|------------|
| "Do today's digest" | Gmail Daily Digest | HARNESS.md Section 5.1 |
| Token / asset evaluation | Trade Evaluation Pipeline | HARNESS.md Section 5.2 |
| Session with state change | MRB Creation | HARNESS.md Section 5.3 |
| Agent observation (r$ky) | Midnight City Observability | HARNESS.md Section 6 |

---

END OF CLAUDE.md
