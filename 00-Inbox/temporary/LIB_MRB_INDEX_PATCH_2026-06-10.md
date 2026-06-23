# LIB.MRB.INDEX.md — PATCH 2026-06-10
# Paste these two blocks into the existing LIB.MRB.INDEX.md at the locations indicated.

---

## ADDITION 1 — Section 7 (System Specifications)
# Paste after the existing [[HARNESS]] entry in Section 7.

---

### [[HARNESS_INVARIANTS]]

**Type:** System Enforcement Specification
**Version:** INVARIANTS_v1.0
**Status:** ACTIVE
**Location:** `04-Claude/HARNESS_INVARIANTS.md`
**Last Updated:** 2026-06-10
**Purpose:** Defines pre-commit gate layer for all ACT and CHECKPOINT transitions in the HARNESS.md execution loop. 10 gates across four categories: PRE-EXECUTION, POST-EXECUTION, MEMORY COMPRESSION, ROLE ISOLATION. Gate failures trigger governance halts (blocked until explicit Alan override or abort). Does not replace HARNESS.md — constrains all transitions within it.
**Layer:** L1 — Enforcement
**Theoretical Lineage:** `05-Library\lib.fwk\profit.os\`

---

## ADDITION 2 — Section 4 (Active MRB Registry)
# Paste as a new entry in Section 4.

---

### ARCH_HARNESS_SplitEnforcement_2026-06-10

**ID:** ARCH_HARNESS_SplitEnforcement_2026-06-10
**Type:** SYSTEM ARCHITECTURE
**Status:** CHECKPOINTED
**Domain:** CROSS-DOMAIN
**Prefixes:** ARCH_

**Tags:**
- HARNESS
- Enforcement Layer
- Split Architecture
- Invariants
- System Design

**Created:** 2026-06-10
**Last Updated:** 2026-06-10
**Promotion Threshold:** 14 days

**Key Decision:** Split Enforcement Architecture (Option D). HARNESS_INVARIANTS.md created as L1 enforcement gate. L2 reference material vaulted at `05-Library\lib.fwk\profit.os\`. Failure model clarified as governance halt (not terminal). Role isolation reformulated for single-session enforceability.

**Storage Path:**
`04-Claude\memory\mrb\2026-06-10_MRB_HARNESS_invariants-layer.md`
