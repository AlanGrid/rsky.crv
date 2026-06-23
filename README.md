# rsky.crv

**Profit.OS — Alan + AI Co-work Surface**

This repository is the public exchange layer of the `rsky.crv` Obsidian vault.  
It is not a full vault mirror. The vault is private. This repo exposes one folder only.

---

## Structure

```
00-Inbox/
  datasets/       — signal logs, watchlist snapshots
  downloads/      — external data staged for review
  exports/        — pipeline outputs (briefs, verdicts)
  memory/         — MRB exchange, index, rules, template ← NEW
  notes/          — session checkpoints, architecture notes
  projects/       — active build artifacts (prompts, schemas)
  screenshots/    — diagnostic captures
  temporary/      — scratch space
  unsorted/       — unclassified drops
```

Everything outside `00-Inbox/` is excluded via `.gitignore`.  
No pipeline scripts, no credentials, no private library content is present in this repo.

---

## Co-work Protocol

**Alan → AI**  
Drop files into `00-Inbox/`, push, reference by raw URL or by name in session.  
AI fetches directly. No copy-paste required.

**AI → Alan**  
Artifacts produced in session (MRBs, prompt files, configs, schemas) are staged here  
for Alan to pull, review, and promote into the local vault.

**Commit convention**
```
inbox: <what was added and why>
update: <what changed>
remove: <what was cleaned out>
```

---

## AI Consumers

All three operate under the same access rule:  
**Read from `00-Inbox/` only. Write by producing artifacts for Alan to commit.**  
No direct repo write access. No access to vault paths outside `00-Inbox/`.

| AI | Access | Raw base URL |
|----|--------|--------------|
| Claude (Anthropic) | `00-Inbox/` read | `https://raw.githubusercontent.com/AlanGrid/rsky.crv/main/00-Inbox/` |
| ChatGPT (OpenAI) | `00-Inbox/` read | `https://raw.githubusercontent.com/AlanGrid/rsky.crv/main/00-Inbox/` |
| Grok (xAI) | `00-Inbox/` read | `https://raw.githubusercontent.com/AlanGrid/rsky.crv/main/00-Inbox/` |

To fetch any file, append the relative path to the base URL.  
Example: `https://raw.githubusercontent.com/AlanGrid/rsky.crv/main/00-Inbox/notes/session.md`

---

## What This Is Not

- Not a backup of the vault
- Not a deployment target
- Not a public project in the conventional sense

It is a structured handoff surface between a human operator and AI co-workers  
operating inside a personal financial intelligence system called **Profit.OS**.

---

## System

**Profit.OS** is a liquidity-aware portfolio operating system built for:
- capital survivability
- regime-aware positioning
- asymmetric deployment
- autonomous signal-to-verdict pipeline (Solana/Jupiter DEX)

Pipeline: `scalp_engine.py` → `scalp-shortlist.json` → `brief_daemon.py` → `bridge.py` → ASI1 → `verdict.json` → Telegram

The pipeline code lives in the private vault. Only artifacts and documentation surface here.

---

*Last updated: 2026-06-23*
