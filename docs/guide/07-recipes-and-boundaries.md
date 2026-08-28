# Recipes and boundaries

These prompts use synthetic examples and can be adapted to a real repository.

## Understand a subsystem

```text
/garcon-pstack:garcon-investigate trace how a queued request becomes an active run. Cite the entry points, state owner, persistence boundary, and cancellation path. Separate facts from inferences.
```

## Design a lifecycle change

```text
/garcon-pstack:garcon-design design idempotent retry ownership. Compare the current and proposed data flow, define invalid states, and specify tests for partial failure. Stop before implementation.
```

## Fix a defect

```text
/garcon-pstack:garcon-fix the worker can outlive its owner after startup failure. Reproduce the lifecycle gap, fix it at the owning boundary, and run the focused regression test.
```

## Review without editing

```text
/garcon-pstack:garcon-review review this branch against main for correctness and regression defects. Report only confirmed findings and do not modify files.
```

## Verify a claim

```text
/garcon-pstack:garcon-verify verify that every admitted worker now has exactly one cleanup owner. Inspect the actual diff and test all admission failure paths.
```

## Let the dispatcher choose

```text
/garcon-pstack:garcon-mode determine why retries duplicate completion, fix the root cause if confirmed, and show exactly what the tests prove.
```

## Common pitfalls

- Using `/garcon-fix` instead of the installed `/garcon-pstack:garcon-fix` namespace.
- Describing a preferred patch without explaining the observed problem.
- Omitting the finish condition and accepting a vague completion claim.
- Asking a review-only workflow to edit the branch.
- Treating a build, health check, deployment, and live evidence as equivalent.
- Running several agents over the same writable files without isolation.
- Adding private transcripts, credentials, host details, or internal identifiers to prompts intended for public artifacts.

## Native pstack mapping

`garcon-pstack` is intentionally not command-compatible with Cursor pstack. The nearest conceptual mappings are:

| Cursor pstack | garcon-pstack |
| --- | --- |
| `/poteto-mode` | `/garcon-pstack:garcon-mode` |
| Investigation and `/how` | `/garcon-pstack:garcon-investigate` |
| `/architect` | `/garcon-pstack:garcon-design` |
| Bug-fix playbook | `/garcon-pstack:garcon-fix` |
| `/interrogate` | `/garcon-pstack:garcon-review` |
| Prove-it-works principle | `/garcon-pstack:garcon-verify` |

The smaller plugin does not reproduce Cursor's sticky mode, model panels, cloud agents, PR orchestration, or transcript-driven memory. Codex and Garcon keep ownership of their native runtime behavior.

Return to [The garcon-pstack guide](README.md).
