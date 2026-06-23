---
type: mrb
domain: system-infrastructure
asset: GitHub — rsky.crv co-work surface
status: complete — operational
created: 2026-06-23
updated: 2026-06-23
tags: [github, git, cowork, memory, mrb-exchange, ai-protocol, claude, chatgpt, grok]
template-version: MRB_v1.2
promotion_threshold: 14
---

# Memory Restoration Block — GitHub Co-work Surface (2026-06-23)

## Session Restore — One Fetch

**Primary restore URL (any AI, any session):**
```
https://raw.githubusercontent.com/AlanGrid/rsky.crv/main/00-Inbox/memory/MRB_INDEX.md
```

Paste this URL at session start. AI fetches MRB_INDEX, identifies session type, loads required MRBs in order. Full context restored without copy-paste.

**Direct file access pattern:**
```
https://raw.githubusercontent.com/AlanGrid/rsky.crv/main/00-Inbox/memory/<filename>
```

---

## What Was Built

### Repository
- **Repo:** `https://github.com/AlanGrid/rsky.crv` (Public)
- **Owner:** AlanGrid
- **Branch:** `main`
- **Surface:** `00-Inbox/` only — all other vault paths excluded

### `.gitignore` — Allowlist Architecture
```gitignore
# Exclude everything
*

# Except
!.gitignore
!00-Inbox/
!00-Inbox/**
```

Credential files explicitly excluded before allowlist was set:
- `01-Market/briefs/brief_daemon.py` — hardcoded ASI1 key
- `01-Market/briefs/run_brief.bat` — Gemini, CoinGecko, ASI1, Groq keys
- `01-Market/briefs/asi1.ai/asi1_test.py`, `step3_ping.py`, `step4_raw.py`, `step5_prompt.py`
- `05-Library/` — private intel, API config, private keys (full exclusion)

### `00-Inbox/` Structure (Public Exchange Layer)
```
00-Inbox/
  datasets/     — watchlist snapshots, signal logs, scored asset exports
  downloads/    — external data staged for review
  exports/      — pipeline outputs (briefs, verdicts, reports)
  memory/       — MRB exchange, index, rules, template ← SESSION RESTORE LAYER
  notes/        — freeform session checkpoints, scratch architecture thinking
  projects/     — active build artifacts (prompts, schemas, configs)
  screenshots/  — diagnostic captures
  temporary/    — scratch space, not expected to persist
  unsorted/     — unclassified drops
```

### `00-Inbox/memory/` — MRB Exchange Layer
```
00-Inbox/memory/
  MRB_INDEX.md          ← master registry + load order by session type
  MRB_RULE_01.md        ← capture rule (what qualifies, how to package)
  MRB_RULE_02.md        ← additional governance rules
  MRB_v1_TEMPLATE.md    ← template every MRB is built from
  [individual MRBs]     ← session artifacts, accumulate over time
```

**Design rule:** `notes/` = freeform. `memory/` = structured, rule-governed, MRB-only.

### AI Consumer Table
| AI | Access | Raw Base URL |
|----|--------|--------------|
| Claude (Anthropic) | `00-Inbox/` read | `https://raw.githubusercontent.com/AlanGrid/rsky.crv/main/00-Inbox/` |
| ChatGPT (OpenAI) | `00-Inbox/` read | `https://raw.githubusercontent.com/AlanGrid/rsky.crv/main/00-Inbox/` |
| Grok (xAI) | `00-Inbox/` read | `https://raw.githubusercontent.com/AlanGrid/rsky.crv/main/00-Inbox/` |

**Access rule (all three):** Read from `00-Inbox/` only. Write by producing artifacts for Alan to commit. No direct repo write access.

---

## Co-work Protocol

**Alan → AI**
```powershell
# Add new content
git add 00-Inbox/
git commit -m "inbox: <description>"
git push origin main
```

**AI → Alan**
AI produces artifact in session → Alan saves locally → Alan commits and pushes.

**Commit convention:**
```
inbox: <what was added and why>
update: <what changed>
remove: <what was cleaned out>
```

**MRB sync pattern:**
Vault-canonical copy lives at `04-Claude/memory/mrb/`.
Exchange copy lives at `00-Inbox/memory/`.
After any new MRB is filed locally, copy to `00-Inbox/memory/` and push.

---

## Key Learnings

**GitHub raw access constraint:**
Claude cannot fetch a raw.githubusercontent.com URL unless it appeared in a prior search result or was pasted directly by the user. First-reference must come from Alan. After that, fetch works.

**Allowlist `.gitignore` is the correct pattern for selective exposure:**
`*` excludes everything. `!00-Inbox/**` re-admits only the exchange surface. No risk of accidentally staging private vault content on future commits.

**Credential audit before first commit is mandatory:**
Four `.py` files and one `.bat` contained hardcoded API keys. Identified via `Get-ChildItem | Select-String` before any `git add` was run. Pattern to reuse on any new script before staging.

**`memory/` separation from `notes/` is a design decision, not a naming preference:**
`memory/` is structured, rule-governed, MRB-only — machine-readable session restore artifacts.
`notes/` is freeform — human-readable scratch, checkpoints, architecture thinking.
Mixing them degrades AI restore reliability.

---

## Operational State

| Item | Status |
|---|---|
| Repo initialized and pushed | ✅ |
| `.gitignore` allowlist active | ✅ |
| `00-Inbox/memory/` live with system files | ✅ |
| `MRB_INDEX.md` verified identical to vault copy | ✅ |
| Claude fetch access confirmed | ✅ |
| README updated — three AI consumers documented | ✅ |
| `00-Inbox/00-Inbox.md` routing file | ⏳ Pending |
| Credential migration (hardcoded → env vars) | ⏳ Deferred — scripts excluded for now |

---

## Open Items

| Item | Priority | Notes |
|---|---|---|
| `00-Inbox/00-Inbox.md` | High | Routing file for cold-start AI. Without it, AI hitting repo root has no map to `memory/` |
| PowerShell sync script | Medium | One-command sync from `04-Claude/memory/mrb/` → `00-Inbox/memory/` + push |
| Credential migration | Low | Move hardcoded keys to env vars, then unexclude pipeline scripts |
| Register this MRB in `MRB_INDEX.md` | Required | Domain: `system-infrastructure`, new session type: `GitHub Co-work Session` |

---

## New Session Type — GitHub Co-work Session

Add to `MRB_INDEX.md`:

```markdown
### GitHub Co-work Session

Trigger: Any modification to repo structure, .gitignore, 00-Inbox/ layout,
memory/ contents, AI access protocol, or sync workflow.

| Load Order | File | Provides |
|---|---|---|
| 1 | `2026-06-23_MRB_github-cowork-surface.md` | Repo structure, access protocol, co-work rules |

Constraint: Do not load for capital decision, coding, or Morning Brief sessions.
```

---

## Restore Instructions

At the start of any GitHub or co-work infrastructure session:

1. Paste `https://raw.githubusercontent.com/AlanGrid/rsky.crv/main/00-Inbox/memory/MRB_INDEX.md`
2. Identify session type → load this MRB
3. Check Open Items table — next action is `00-Inbox/00-Inbox.md`
4. Confirm `.gitignore` allowlist is intact before any new `git add`

[[MRB_INDEX]]
[[2026-06-21_SESSION_UPDATE_4]]
