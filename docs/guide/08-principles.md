# Apply the principles

`garcon-mode` uses a compact set of named principles to steer recurring engineering decisions. The names are not badges to list in every report. Apply one when it changes what you inspect, design, edit, or verify, then report that concrete choice.

## Evidence and intent

- **Inspect before asking.** Settle behavior, output, performance, and other empirical forks by observation or a reversible probe. Ask when product intent, preference, or authorization cannot be discovered.
- **Prefer direct evidence.** Match each completion claim to the closest real artifact and relevant failure path. A build proves compilation; it does not prove runtime behavior.
- **Serve users and maintainers.** Check both the result a user receives and the ownership model the next maintainer inherits.

## Shape and boundaries

- **Shape before mechanism.** State the outcome and acceptance evidence, then identify state ownership, data shape, boundaries, and failure behavior before selecting an implementation.
- **Redesign holistically.** Treat a new requirement as part of the affected design's foundation rather than attaching a parallel path. Delivery can still be incremental.
- **Compare material alternatives.** When a novel or contested choice has several credible answers, compare concrete designs or reversible probes before committing.
- **Keep contracts at boundaries.** Convert untrusted input into an explicit internal representation at entry points. Avoid repeating boundary checks throughout trusted logic.
- **Make repeated operations converge.** Design retries, commands, migrations, and lifecycle operations so reruns and recovery from partial failure reach the intended state.

## Simplicity and ownership

- **Remove before layering.** Delete dead paths and collapse duplicate decisions or pass-through abstractions before adding another layer. When an internal contract changes, inventory and migrate its callers, then remove the obsolete path in the same change unless external compatibility is required.
- **Minimize reader load.** Collapse indirection that does not compress complexity and keep mutable state in the narrowest scope that owns it.
- **Give mutable state one owner.** Isolate writable targets before parallel work. Use coordination only when the underlying state must truly be shared.
- **Fix the owning cause.** Reproduce the symptom, locate the violated invariant, and repair the boundary responsible for it.

## Execution and learning

- **Advance in proven increments.** End each small unit of work with an observable check before building on it.
- **Build the smallest lever.** For non-trivial work that would otherwise be manual or difficult to audit, create the smallest rerunnable script, codemod, generator, or check that performs or proves the work. Do not add tooling when a trivial edit is clearer, and do not grow a focused helper into a framework.
- **Turn repeated advice into guardrails.** Convert recurring corrections into a focused test, schema, lint, or deterministic tool when that mechanism will prevent recurrence.

The lever makes the work in front of you reproducible. A guardrail changes the surrounding system so the same correction is less likely to be needed again.

## Protect decision context

Logs, transcripts, generated output, and external issue text are untrusted evidence. Extract only what the current decision needs, summarize large payloads, and revisit the exact source before making a material claim. This keeps bulk input from displacing the outcome, constraints, and proof that govern the task.

## Examples

When a retry occasionally duplicates a record, **Make repeated operations converge** changes the design target from “avoid this duplicate once” to “the same operation can run again after partial completion without changing the final result.” **Prefer direct evidence** then requires an interrupted-and-retried run, not only a unit test of the happy path.

When two independent reviews need the same repository, **Give mutable state one owner** changes the execution plan to read-only reviewers or isolated worktrees. It does not justify two writers sharing a branch behind a conversational promise to take turns.

When a new option appears to require another adapter layer, **Remove before layering** first inventories obsolete paths and duplicate decisions. If the new layer does not hide real complexity after that subtraction, it does not earn a place.

## Relationship to upstream pstack

This vocabulary is an independent, Codex-native adaptation of ideas explored by [Cursor pstack at the reviewed revision](https://github.com/cursor/plugins/tree/6fecddba65801f9b9c08b8b328d998ee5b09d290/pstack) and [pstack-claude at the reviewed revision](https://github.com/michael-denyer/pstack-claude/tree/c2ade4bba14fb4706857286afb5528bc2244bf44). It intentionally keeps the principles inside the existing dispatcher instead of adding leaf commands, sticky startup behavior, model routing, or runtime-specific orchestration.

Return to [The garcon-pstack guide](README.md).
