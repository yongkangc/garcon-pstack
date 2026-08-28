# Route work with `garcon-mode`

`garcon-mode` is a dispatcher. It selects the smallest workflow that can reach the requested outcome.

## Routing model

| Request | Routed skill |
| --- | --- |
| Explain behavior or gather evidence without edits | `garcon-investigate` |
| Settle ownership, data shapes, or interfaces | `garcon-design` |
| Reproduce and fix a defect | `garcon-fix` |
| Look for confirmed defects in a change | `garcon-review` |
| Test whether a claim is actually true | `garcon-verify` |

The dispatcher may combine workflows when the task crosses a real boundary. A defect with an unclear owner might require investigation before fixing. A completed fix should end with verification.

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
2. Establish the current evidence and exact scope.
3. Select and follow the relevant workflow.
4. Preserve unrelated user changes.
5. Verify the real artifact.
6. Report the outcome, evidence, and remaining uncertainty.

`garcon-mode` is not sticky. It does not install a startup hook or silently control future turns. Invoke it for the task that needs it.

Next: [Investigate and design](03-investigate-and-design.md).
