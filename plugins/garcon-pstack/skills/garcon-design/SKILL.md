---
name: garcon-design
description: Design a repository change by settling data shapes, ownership, interfaces, failure behavior, and verification before implementation.
---

# Garcon Design

Design against the current repository rather than an imagined clean slate.

- Map the current data flow, computation, side effects, and ownership boundaries.
- State the proposed data shape and public interfaces before implementation details.
- Make invalid states difficult to represent. Parse external data at boundaries and keep internal contracts explicit.
- Identify concurrency, persistence, retry, idempotency, and partial-failure behavior where relevant.
- Compare alternatives only when the decision is material. Explain why the selected design fits the repository better.
- Define the migration or rollout boundary. Avoid compatibility layers unless the repository requires them.
- Define observable verification for each risky claim.

Unless implementation was requested, stop after the design and identify the decision that unlocks coding. If implementation was requested, reread the agreed design before editing.
