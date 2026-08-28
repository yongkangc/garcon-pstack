---
name: garcon-mode
description: Route a non-trivial engineering task through a small evidence-first workflow for investigation, design, fixes, review, or verification.
---

# Garcon Mode

Use the smallest workflow that reaches the requested outcome.

## Route the task

Read repository instructions first. Then select the matching sibling skill:

- Read `../garcon-investigate/SKILL.md` for explanation, diagnosis without edits, or evidence gathering.
- Read `../garcon-design/SKILL.md` when interfaces, ownership, data shapes, or implementation boundaries must be settled.
- Read `../garcon-fix/SKILL.md` when the requested outcome includes a code change for a defect.
- Read `../garcon-review/SKILL.md` for review-only work.
- Read `../garcon-verify/SKILL.md` when validating an implementation, claim, release, or external state.

Combine workflows only when the task genuinely crosses their boundaries. Do not load every sibling by default.

## Operating rules

- Lead with the current outcome or state.
- Separate confirmed observations, reasoned inferences, and unknowns.
- Prefer the smallest change that fixes the root cause.
- Establish data shape, ownership, and failure behavior before adding abstraction.
- Preserve unrelated user changes and authorization boundaries.
- Use bounded parallel work only for independent questions. Keep one owner for synthesis and verification.
- Verify the real artifact. Compilation, a mock, or an agent report is not runtime proof.
- Stop before external or destructive actions that the user did not authorize.

## Completion contract

Report the outcome, material evidence or changed files, validation performed, and any remaining uncertainty. Do not claim more than the evidence proves.
