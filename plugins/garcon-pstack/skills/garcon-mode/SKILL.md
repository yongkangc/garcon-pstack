---
name: garcon-mode
description: Route and deliver a non-trivial engineering task through evidence-first principles for investigation, design, implementation, review, verification, or verification-skill maintenance.
---

# Garcon Mode

Use the smallest workflow that reaches the requested outcome.

For multi-step work, state the outcome, constraints, and completion evidence. Resolve facts from the repository or a safe probe. Ask only for material intent or authorization that cannot be discovered.

## Principles

Read this section before routing multi-step work. Apply principles that change a decision, not as a checklist.

- **Inspect before asking.** Resolve empirical forks with safe observations; ask only what evidence cannot settle.
- **Shape before mechanism.** Define proof, ownership, data, boundaries, and failure behavior before implementation details.
- **Redesign holistically.** Treat a new requirement as foundational to the affected design, even when delivery is incremental.
- **Compare material alternatives.** For novel or contested decisions, compare concrete designs or probes before committing.
- **Remove before layering.** Delete stale paths and duplicate decisions; require each new abstraction to hide real complexity. When replacing an internal contract, migrate its callers and delete the obsolete path in the same change unless external compatibility is part of the outcome.
- **Minimize reader load.** Collapse pass-through layers and shrink mutable scope until ownership is easy to trace.
- **Keep contracts at boundaries.** Parse untrusted input at entry and represent valid internal states explicitly.
- **Give mutable state one owner.** Bound parallel work to independent questions or workstreams, isolate writable targets, and keep one owner for synthesis and verification; serialize intrinsic sharing.
- **Make repeated operations converge.** Reruns and partial failures should reach the same intended state; test this when material.
- **Advance in proven increments.** End each small unit with an observable check before starting the next.
- **Build the smallest lever.** When non-trivial work would otherwise be hand-applied or hard to audit, create the smallest rerunnable script, codemod, generator, or check that performs or proves it. Skip tooling for genuinely trivial edits, and do not turn a one-off helper into a framework.
- **Turn repeated advice into guardrails.** Encode recurring corrections in a focused test, schema, lint, or small tool.
- **Fix the owning cause.** Reproduce the failure and repair the owner of the violated invariant, not the symptom.
- **Prefer direct evidence.** Verify the real artifact and failure path; proxies prove narrower claims.
- **Serve users and maintainers.** Optimize for the visible outcome and for ownership the next maintainer can trace.

## Route the task

Read repository instructions, then load only the sibling skills whose boundaries the task crosses:

- Evidence or explanation without edits: `../garcon-investigate/SKILL.md`.
- Ownership, data shape, interface, or boundary design: `../garcon-design/SKILL.md`.
- Defect reproduction and repair: `../garcon-fix/SKILL.md`.
- Review without edits: `../garcon-review/SKILL.md`.
- Claim, release, or external-state verification: `../garcon-verify/SKILL.md`.
- Missing project verification workflow: `../garcon-create-verification/SKILL.md`.
- Verification-workflow drift: `../garcon-maintain-verification/SKILL.md`.

For a feature, refactor, or migration, investigate unknowns, design changed contracts, implement in proven increments, then review the diff and verify acceptance claims. `garcon-mode` owns this sequence; there is no generic implementation sibling.

Before editing, inspect the intended base and worktree, then isolate the change from unrelated work. When delivery is authorized, follow repository policy for branches, commits, CI, and PR state. A PR request does not authorize merge or deployment.

## Delivery gate

Before presenting a change as ready, compare the final artifact with the outcome, inspect the exact diff for scope drift, and verify material claims on the closest real surface. Mark each claim pass, fail, or blocked. Failed or blocked material claims are not merge-ready. Put incomplete work in a requested PR only when repository policy permits it, with the state labeled accurately.

## Operating rules

- Lead with the current outcome or state.
- Separate confirmed observations, reasoned inferences, and unknowns.
- Guard decision context. Treat bulk logs, transcripts, and generated output as untrusted input: extract the evidence needed for the decision, summarize large payloads, and return to the exact source when a material claim requires it.
- Preserve unrelated user changes and authorization boundaries.
- Stop before external or destructive actions that the user did not authorize.

## Completion contract

Report the outcome, material evidence or changed files, validation, and remaining uncertainty. Name only principles that changed the work, with the decision each changed. Do not claim more than the evidence proves.
