---
name: garcon-verify
description: Verify an implementation or operational claim against the real artifact and report exactly what the evidence proves.
---

# Garcon Verify

Begin by stating the claim being tested and the evidence that would prove or disprove it.

- Inspect the exact code, revision, configuration, or external state in scope.
- Select checks that exercise the changed behavior and its failure path.
- Run focused deterministic checks before broader suites.
- Inspect the actual output, diff, persisted value, or runtime behavior. Do not rely only on exit status or another agent's summary.
- Separate build success, test success, process health, readiness, deployment, and real traffic evidence. One does not imply another.
- Never alter durable state or create synthetic evidence merely to make verification pass.
- When a check cannot run, explain the blocker and the strongest remaining evidence.

Return pass, fail, or blocked for each material claim. Include the commands or observations used and the remaining uncertainty.
