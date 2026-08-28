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
