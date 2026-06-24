# MRB: <title>

id: mrb-YYYYMMDD-HHMMSS
version: 1.0
status: draft
owner: @AlanGrid
created: YYYY-MM-DDTHH:MM:SSZ
depends-on: []
purpose: |
  One-sentence summary of what this memory block represents and why it exists.

restoration:
  load-order:
    - "00-Inbox/memory/index.md"
    - "<this-file>"
  steps:
    - step: "Fetch index"
    - step: "Verify dependencies listed in depends-on"
    - step: "Validate required metadata fields"
    - step: "Record restoration timestamp and commit reference"

content:
  - type: narrative
  - data: |
      Replace with the substance of the memory block. Include full provenance: source URLs, raw filenames, and commit SHAs when available.

trace:
  what_changed: |
    Describe the change this MRB records (explicit diff/summary).
  why: |
    Describe reason/intent for the change.
  cause: |
    Source of change (manual / automated / ingestion pipeline / sensor).
  affected_files:
    - path: 00-Inbox/...
  reconstruction:
    - step: "git checkout <commit>"
    - step: "curl -o <local-file> <raw-url>"

signature:
  agent: AI
  agent_version: v1
  human_reviewed: false

# Guidance

- Use the id field to ensure deterministic ordering and to prevent collisions. The id MUST begin with the literal prefix `mrb-` followed by an ISO-like timestamp (YYYYMMDDHHMMSS) to guarantee sortability.
- Always populate depends-on with explicit paths or MRB ids. Do not leave implicit references.
- Keep restoration.load-order minimal and explicit. The loader must be able to reconstruct the exact sequence from these fields alone.
- When promoting an MRB from draft -> final, append a trace entry showing who promoted it and the commit that performed the promotion (commit SHA and message).
