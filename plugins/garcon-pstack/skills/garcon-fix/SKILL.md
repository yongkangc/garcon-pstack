---
name: garcon-fix
description: Reproduce and fix a confirmed defect with a focused regression test and evidence that the root cause is resolved.
---

# Garcon Fix

Do not edit until the failing path and expected behavior are understood well enough to choose a focused change.

- Reproduce the symptom or establish an equivalent failing check.
- Trace the symptom to the earliest violated invariant. Distinguish root cause from downstream damage.
- Inspect the worktree and preserve unrelated changes.
- Add or strengthen a regression test when it can represent the defect faithfully.
- Implement the smallest coherent fix at the owning boundary.
- Run the focused check first, then the broader validation justified by the blast radius.
- Inspect the final diff for accidental scope, generated noise, and weakened safety behavior.

If reproduction is impossible, state that clearly. Do not manufacture a failing test or claim the defect is fixed from code inspection alone.
