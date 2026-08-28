---
name: garcon-investigate
description: Investigate a repository, behavior, or incident without changing it, and produce an evidence-backed explanation with facts separated from inferences.
---

# Garcon Investigate

Treat investigation as read-only unless the user separately asks for a change.

- Identify the exact repository, revision, runtime, and question in scope.
- Read the governing instructions and primary entry points before following references.
- Trace the relevant data and control path across boundaries. Record who owns state, persistence, retries, and failure handling.
- Search tests, history, documentation, schemas, and live read-only state when they can confirm intent or behavior.
- Verify drift-prone facts against the current source or runtime.
- Use parallel investigators only when the questions are independent. Give each a narrow scope and synthesize their evidence.
- Do not turn missing evidence into a negative conclusion. State what was searched and what remains unknown.

Return a direct answer followed by supporting file links or source links. Label consequential statements as confirmed, inferred, or unknown.
