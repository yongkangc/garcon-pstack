# The garcon-pstack guide

This guide teaches the complete `garcon-pstack` workflow through concrete tasks. The plugin is deliberately small, so the guide focuses on choosing the right skill, stating a finish condition, and evaluating the resulting evidence.

The guide is independently written. It follows the task-oriented spirit of [Cursor pstack's public guide](https://github.com/cursor/plugins/tree/main/pstack/docs/guide) without copying its text or Cursor-specific runtime assumptions.

## Learning path

1. [Install and confirm discovery](01-install.md). Add the marketplace, install the plugin, and check the names Codex exposes.
2. [Route work with `garcon-mode`](02-route-work.md). Give the dispatcher a goal, constraints, and a finish condition.
3. [Investigate and design](03-investigate-and-design.md). Understand the current system and settle ownership before editing.
4. [Fix a defect](04-fix.md). Reproduce, find the violated invariant, implement the smallest fix, and prove it.
5. [Review and verify](05-review-and-verify.md). Separate defect discovery from testing a concrete claim.
6. [Use the skills through Garcon](06-garcon.md). Invoke namespaced skills and keep Garcon's control-plane responsibilities separate.
7. [Recipes and boundaries](07-recipes-and-boundaries.md). Copy focused prompts and avoid the common failure modes.

Read the chapters in order for the first task. After that, each chapter stands alone.

## The shortest useful prompt

State the outcome and the proof you expect:

```text
/garcon-pstack:garcon-mode the export duplicates rows after a retry. Reproduce it, fix the owning invariant, and show the regression test.
```

You do not need to select the workflow yourself. `garcon-mode` routes the request and keeps facts, inferences, and unknowns distinct.

Next: [Install and confirm discovery](01-install.md).
