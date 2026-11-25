---
name: garcon-review
description: Review an exact code change for confirmed correctness, safety, and regression defects without editing unless a fix is requested.
---

# Garcon Review

Review the exact head and intended base. Treat review as read-only unless the user also requests fixes.

- Read repository instructions and establish the change's stated intent.
- Inspect the diff, its callers, state transitions, tests, and relevant failure paths.
- Prioritize correctness, data loss, security, concurrency, lifecycle, and false-success risks over style.
- Confirm each finding from the code path. Do not report speculative problems as defects.
- Track the governing invariant for each confirmed finding. If two findings in one review-and-fix cycle violate the same invariant, stop proposing isolated patches: state the invariant, inspect every transition or caller that can violate it, and require one executable model, table-driven test, property, or equivalent focused guardrail before re-review.
- Re-review the complete exact-head diff after a fix. A delta-only review can confirm the repair, but it cannot establish that the full change now satisfies the invariant.
- Use at most a small number of independent reviewers when the surface is large or adversarial review adds value. Synthesize and deduplicate their findings.
- Check whether tests exercise the risky behavior rather than only nearby helpers.

List findings by severity. For each finding, give the location, trigger, impact, and narrow remediation. If there are no confirmed findings, say so and identify any validation gap that remains.
