# MRB — Harness Engineering Deploy + Skills Vault Cleanup
**Date:** 2026-06-09
**Session Type:** System Architecture + Vault Maintenance
**Status:** COMPLETE
**Tags:** harness, CLAUDE.md, skills, vault-cleanup, system-architecture

---

## Facts

### New Files Created
- `04-Claude/HARNESS.md` — HARNESS_v1.0 — full execution harness spec
- `04-Claude/CLAUDE.md` — CLAUDE_v2.0 — rewritten as router + bootstrap loader

### HARNESS.md Contents (8 sections)
1. Execution Loop — OBSERVE → ROUTE → THINK → ACT → CHECKPOINT
2. Tool Permission Matrix — Gmail, Calendar, Drive, Notion, PayPal, native tools
3. State Persistence Rules — naming conventions, what persists, what doesn't
4. Error Recovery — 7 error types with deterministic recovery paths
5. Pipeline Definitions — Gmail Digest, Trade Evaluation, MRB Creation
6. Agent Observability — Midnight City / r$ky log template
7. Harness Maintenance — version control, update triggers
8. Quick Reference — session checklist, hard stops, never-do list

### CLAUDE.md v2.0 Contents
- References SYSTEM.md (priority 1) and HARNESS.md (priority 2)
- Correct vault map with actual paths
- Full 9-skill registry with file pointers
- File discovery table (13 canonical locations)
- 9-step startup sequence with HARNESS section pointers
- Daily workflow entry points → pipeline references

### Skills Directory — Final State
Canonical files (7):
- `01_brief.md` — morning brief workflow prompt
- `02_weekly.research.session.md` — weekly research workflow prompt
- `03_token.research.template.md` — token research card template
- `06_profit-os_synthetic-token-monitor.md` — Jupiter DEX synthetic token module
- `07_multi_agent_harness.md` — agent architecture spec
- `08_body-health.md` — canonical body-health skill (YAML frontmatter)
- `09_coding-coach.md` — canonical coding-coach skill (YAML frontmatter)

Data layer (intact):
- `claude.body.health/` — health data files, protocols, reports, MRBs

### Deleted / Archived
Moved to `00-Inbox/temporary/skill/` (30-day recovery window):
- `04_claude.instruction.md` — legacy persona file, conflicts with SYSTEM.md
- `05_code-project-instructions.md` — superseded by 09_coding-coach.md
- `claude.skills/` folder — entire subfolder (guides, .skill files, SKILL.md)
- `claude.finace.istructions/` folder — legacy finance instructions
- `BODY.HEALTH_SKILL.md` (root) — identical to 08_body-health.md

Reference material moved to `05-Library/books/ai/claude.skills.guides/`:
- `claude.skills.guide.01-03.md` — generic prompting tips (Twitter threads)
- `img/` — skill guide screenshots

---

## Decisions Made

1. **CLAUDE.md = Router only.** No behavioral rules. References SYSTEM.md and HARNESS.md. Single source of truth per layer.
2. **HARNESS.md = Execution protocol.** Sits below SYSTEM.md and CLAUDE.md in load order. Governs runtime, not values.
3. **Skill file naming:** 01–03 stay as workflow prompts (descriptive names). 08–09 are canonical skill specs (YAML frontmatter). Inconsistency noted, not resolved this session.
4. **`claude.body.health/` stays as data layer.** Not merged into skills root. Feeds `08_body-health.md`.
5. **`07_multi_agent_harness.md` is NOT a duplicate of `HARNESS.md`.** Different layers: 07 = agent architecture, HARNESS.md = execution runtime.
6. **`04_claude.instruction.md` deleted** — newsletter persona predates current architecture, conflicts with SYSTEM.md principal layer.

---

## Open Questions

1. Should `01_brief.md`, `02_weekly.research.session.md`, `03_token.research.template.md` be upgraded to YAML frontmatter skill spec format to match `08` and `09`?
2. `BODY.HEALTH_SKILL.md` was found in `skills/` root (not in `claude.body.health/`) — confirm deleted.
3. CLAUDE.md now references skill files by number. If files are renumbered, CLAUDE.md and HARNESS.md route tables both need updating. Consider whether a gap at 04/05 (deleted files) should be filled or left.

---

## Next Actions

| Priority | Action | Owner |
|----------|--------|-------|
| HIGH | Delete `BODY.HEALTH_SKILL.md` from `skills/` root | Alan |
| HIGH | Deploy `CLAUDE.md` v2.0 to `04-Claude/CLAUDE.md` on disk | Alan |
| HIGH | Deploy `HARNESS.md` v1.0 to `04-Claude/HARNESS.md` on disk | Alan |
| HIGH | Add HARNESS.md backlink to `SYSTEM.md` | Alan |
| HIGH | Register HARNESS.md in `LIB.MRB.INDEX.md` Section 6 | Alan |
| MEDIUM | Build `08_context_harness.md` skill — context rot prevention rules | Next session |
| MEDIUM | Decide: upgrade 01/02/03 to YAML skill spec format | Next session |
| LOW | Phase 2 Midnight City — begin agent observability logging (5 sessions minimum before conclusions) | When ready |

---

## System State Delta

| Component | Before | After |
|-----------|--------|-------|
| HARNESS.md | Did not exist | v1.0 deployed |
| CLAUDE.md | Stub with placeholder content, wrong paths | v2.0 router with correct paths + 9-skill registry |
| `04-Claude/skills/` | 9 numbered files + 3 legacy subfolders + duplicates | 7 canonical files + 1 data subfolder, no duplicates |
| Skill registry | Incomplete, 2 skills listed | 9 skills, all with file pointers |
| Tool permission boundaries | Undefined | Defined in HARNESS.md Section 2 |
| Error recovery paths | None | 7 error types, deterministic handling |
| Pipeline definitions | Implicit | 3 explicit pipelines in HARNESS.md Section 5 |

---

**File this at:** `04-Claude/memory/mrb/2026-06-09_MRB_harness-deploy-vault-cleanup.md`
**Register in:** `LIB.MRB.INDEX.md`
**Backlinks:** `[[HARNESS]]`, `[[CLAUDE]]`, `[[SYSTEM]]`
