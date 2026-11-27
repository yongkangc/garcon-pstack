# Review and verify

Review and verification are related but separate operations.

```text
Review asks: Which confirmed defects are present in this change?
Verification asks: Does the available evidence prove this specific claim?
```

## Review an exact change

Use `garcon-review` with a known head and intended base:

```text
/garcon-pstack:garcon-review review the current branch against main. Focus on lifecycle ownership, false-success paths, and missing regression coverage. Do not edit.
```

A finding should include:

- Severity.
- File and location.
- Triggering path.
- User or system impact.
- Narrow remediation.

Speculation is not a finding. When no confirmed defect is found, the result should say so and name any remaining test gap.

Keep one invariant history for the full review-and-fix cycle. If separate review rounds find two defects against the same invariant, stop patching examples one at a time. Inspect every path that can violate the invariant, add a focused executable guardrail, and then review the complete exact head again.

Verification code needs its own adversarial check. Trace each modeled transition and state key back to the production path it represents, look for nondeterministic inputs, unsound state merging, and properties that can pass without exercising the risky path, then plant or replay a known violation. Until that negative control fails for the expected reason, a green checker proves only that the checker ran.

## Verify a concrete claim

Use `garcon-verify` after implementation or when auditing status:

```text
/garcon-pstack:garcon-verify verify that cancellation now completes exactly once after every retry path. Inspect the exact diff and run the focused lifecycle tests.
```

Verification should classify each material claim as pass, fail, or blocked and identify the evidence used.

## Keep evidence levels separate

These observations are not interchangeable:

```text
Code inspection
Build success
Focused test success
Full suite success
Process health
Readiness
Deployment
Canary behavior
Real traffic behavior
```

Each level proves a different statement. Do not report a deployment from a passing test or real-world behavior from a healthy process.

Next: [Use the skills through Garcon](06-garcon.md).
