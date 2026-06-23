# rsky.crv

**Profit.OS — Alan + Claude Co-work Surface**

This repository is the public exchange layer of the `rsky.crv` Obsidian vault.  
It is not a full vault mirror. The vault is private. This repo exposes one folder only.

---

## Structure

```
00-Inbox/
  datasets/     — watchlist snapshots, signal logs, scored asset exports
  downloads/    — external data staged for review
  exports/      — pipeline outputs (briefs, verdicts, reports)
  notes/        — session checkpoints, MRB drafts, architecture notes
  projects/     — active build artifacts (prompts, schemas, configs)
  screenshots/  — diagnostic captures
  temporary/    — scratch space, not expected to persist
  unsorted/     — unclassified drops
```

Everything outside `00-Inbox/` is excluded via `.gitignore`.  
No pipeline scripts, no credentials, no private library content is present in this repo.

---

## Co-work Protocol

**Alan → Claude**  
Drop files into `00-Inbox/`, push, reference by raw URL or by name in session.  
Claude fetches directly. No copy-paste required.

**Claude → Alan**  
Artifacts produced in session (MRBs, prompt files, configs, schemas) are staged here  
for Alan to pull, review, and promote into the local vault.

**Commit convention**
```
inbox: <what was added and why>
update: <what changed>
remove: <what was cleaned out>
```

---

## What This Is Not

- Not a backup of the vault
- Not a deployment target
- Not a public project in the conventional sense

It is a structured handoff surface between a human operator and an AI co-worker  
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
