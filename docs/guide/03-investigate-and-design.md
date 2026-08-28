# Investigate and design before editing

Investigation and design answer different questions.

```text
Investigation: What does the current system do, and what evidence proves it?
Design: What should own the new behavior, and what contract should it expose?
```

## Investigate without changing the repository

Use `garcon-investigate` for architecture explanations, incident diagnosis, history reconstruction, and read-only comparisons.

```text
/garcon-pstack:garcon-investigate trace a request from admission through cancellation. Identify who owns each state transition and cite the relevant files.
```

A useful investigation result separates:

- Confirmed facts observed in code, tests, history, or runtime state.
- Inferences supported by those facts.
- Unknowns that the available evidence cannot settle.

Missing evidence is not evidence that behavior or data does not exist. A good investigation says what was searched and which uncertainty remains.

## Design the owning boundary

Use `garcon-design` when a change crosses interfaces or changes ownership.

```text
/garcon-pstack:garcon-design design durable cancellation ownership. Show the current and proposed data flow, failure behavior, and verification boundary.
```

The design should settle:

- The authoritative data shape.
- Which component owns mutation and persistence.
- The public interface and its callers.
- Invalid states and boundary validation.
- Retry, concurrency, idempotency, and partial-failure behavior.
- Migration and observable verification.

Compare alternatives only when the decision changes the system materially. Small changes do not need an architecture tournament.

## Combine them deliberately

When the current design is unclear, investigate first and then design against the evidence:

```text
/garcon-pstack:garcon-mode determine who currently owns cancellation, then design the smallest change that makes retries converge safely. Stop after the design.
```

The final sentence prevents an explanatory task from silently turning into implementation.

Next: [Fix a defect](04-fix.md).
