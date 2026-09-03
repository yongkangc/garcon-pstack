# Route work with `garcon-mode`

`garcon-mode` is a dispatcher. It selects the smallest workflow that can reach the requested outcome.

## Routing model

| Request | Routed skill |
| --- | --- |
| Explain behavior or gather evidence without edits | `garcon-investigate` |
| Settle ownership, data shapes, or interfaces | `garcon-design` |
| Deliver a feature, refactor, or migration | `garcon-mode` composes design, implementation, review, and verification |
| Improve measured performance | `garcon-mode` preserves the measurement harness from baseline through comparison |
| Reproduce and fix a defect | `garcon-fix` |
| Look for confirmed defects in a change | `garcon-review` |
| Test whether a claim is actually true | `garcon-verify` |
| Create a project-specific verification workflow | `garcon-create-verification` |
| Audit an existing verification workflow for drift | `garcon-maintain-verification` |

The dispatcher may combine workflows when the task crosses a real boundary. A defect with an unclear owner might require investigation before fixing. A completed fix should end with verification.

For new behavior, refactoring, or a migration, `garcon-mode` owns the delivery sequence. It investigates only the unknowns, uses `garcon-design` when ownership or contracts change, implements in small checked increments, reviews the exact diff, and verifies the acceptance claims. A failed or blocked material claim is not merge-ready.

Repository policy owns the base branch, worktree isolation, commits, CI, and PR metadata. Asking for a PR authorizes that delivery step, not a merge or deployment.

## Use the principles as steering vocabulary

`garcon-mode` includes a compact set of named principles for decisions that recur across workflows. They cover empirical questions, domain modeling, refactor contracts, measured performance, holistic redesign, alternatives, abstraction, reader load, boundaries, mutable ownership, retries, incremental proof, rerunnable leverage, structural guardrails, root causes, direct evidence, and the user and maintainer experience.

The names are useful only when they change the work. For example, **Inspect before asking** can replace a speculative question with a safe probe. **Give mutable state one owner** can turn two agents editing one branch into isolated worktrees. **Prefer direct evidence** can replace a compile-only completion claim with a real behavior check.

See [Apply the principles](08-principles.md) for the complete vocabulary and examples.

## Give it a contract

A strong prompt contains three things:

- Outcome. What should be true when the task finishes?
- Constraints. Which safety, scope, or compatibility boundaries matter?
- Evidence. What observation would convince you the work is complete?

For example:

```text
/garcon-pstack:garcon-mode make cancellation idempotent without changing the public API. Reproduce the duplicate transition first and finish with a focused regression test.
```

This is stronger than prescribing a list of implementation steps. It gives the agent room to inspect the current design while preserving the boundaries that matter.

## What happens during the task

The workflow should:

1. Read repository instructions.
2. State the outcome, material constraints, and completion evidence.
3. Apply the principles that change a decision.
4. Select and follow the relevant workflow.
5. Preserve unrelated user changes.
6. Review the final diff and verify the real artifact.
7. Report the outcome, evidence, readiness, and remaining uncertainty.

`garcon-mode` is not sticky. It does not install a startup hook or silently control future turns. Invoke it for the task that needs it.

Next: [Investigate and design](03-investigate-and-design.md).
