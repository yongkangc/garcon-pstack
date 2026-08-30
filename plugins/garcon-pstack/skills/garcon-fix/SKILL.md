---
name: garcon-fix
description: Reproduce and fix a confirmed defect with a focused regression test and evidence that the root cause is resolved.
---

# Garcon Fix

Do not edit until the failing path, expected behavior, and evidence that distinguishes the leading cause from plausible alternatives are explicit.

- Reproduce the symptom on the closest faithful surface. If that surface is unavailable, state what a narrower check does and does not prove.
- Iterate through observation, hypothesis, and a discriminating check. Source evidence can prove that a deterministic code path violates an invariant, but source inspection alone cannot prove that an external runtime or incident trigger occurred. Require direct evidence or a faithful reproduction for that claim.
- Trace the symptom to the earliest violated invariant. Distinguish root cause from downstream damage.
- Inspect the worktree and preserve unrelated changes.
- When a focused automated check can represent the defect faithfully, capture it failing before the edit and passing afterward. Otherwise record why and preserve the strongest direct pre-fix observation for post-fix comparison.
- Implement the smallest coherent fix at the owning boundary.
- Run the focused check first, then the broader validation justified by the blast radius.
- Inspect the final diff for accidental scope, generated noise, and weakened safety behavior.

If reproduction is impossible, state that clearly. Do not manufacture a failing test. Source evidence may justify a code-path fix, but do not claim it reproduces or resolves an external incident trigger without runtime evidence.
