# Fix a defect at the root cause

`garcon-fix` is for a requested code change tied to a confirmed defect. Its basic path is:

```text
Symptom → reproduction → violated invariant → focused fix → regression test → broader validation
```

## Start with observable behavior

Give the skill a symptom and expected behavior rather than a preferred patch:

```text
/garcon-pstack:garcon-fix cancellation publishes completion twice after a retry. Reproduce it, find the earliest violated invariant, and add a regression test.
```

The workflow should identify the exact failing path before editing. It cycles through an observation, a cause hypothesis, and a check that distinguishes that hypothesis from plausible alternatives. Source evidence can prove that a deterministic code path causes the behavior under its stated preconditions. Source inspection alone cannot prove that an external runtime or incident supplied those preconditions, and correlation does not establish that trigger. A guard that merely hides downstream damage is not a root-cause fix.

When a focused automated check can represent the defect faithfully, capture the failing result before the edit and the passing result afterward. If only a narrower check is available, state exactly what it does and does not prove.

## Preserve the real worktree

The skill inspects existing changes before editing and must preserve unrelated user work. If the worktree is dirty, it should isolate its scope rather than resetting or rewriting other changes.

## Require proportional evidence

The evidence should match the risk:

| Change | Minimum useful evidence |
| --- | --- |
| Pure function defect | Focused regression test and relevant suite |
| Lifecycle or concurrency defect | Deterministic transition test plus owning integration path |
| UI defect | Reproduction on the real surface and post-fix behavior |
| Operational defect | Code checks plus current runtime or deployment evidence when authorized |

Compilation proves only that the program compiled. It does not prove that a race, lifecycle transition, or user-visible behavior is fixed.

## When reproduction is unavailable

The correct result may be incomplete:

```text
Confirmed: the code permits the reported transition.
Unknown: the production trigger could not be reproduced with available data.
Not claimed: the incident is fixed.
```

The workflow must not manufacture a failure or upgrade code inspection into runtime proof.

Next: [Review and verify](05-review-and-verify.md).
