---
name: garcon-create-verification
description: Create a project-local verification skill and feature map that drives the real app and preserves observable proof.
---

# Garcon Create Verification

Create a project-local verification skill only after interviewing the repository. Do not ask the user for facts available in source, scripts, manifests, documentation, or a safe local run.

## Repository interview

Determine:

- the primary user-facing surface: web UI, CLI/TUI, desktop app, API, service, or library;
- the documented launch command, readiness signal, port, environment, seed data, and authentication boundary;
- the strongest existing driving harness: browser automation, PTY, HTTP, test fixture, or debug interface;
- observable proof: screenshots, terminal output, HTTP bodies, exit codes, logs, files, database rows, or rendered state;
- whether isolated instances can run beside the user's instance using separate ports, data directories, and profiles.

If the project does not build or start, stop and report the precise blocker. Do not generate instructions from an unverified broken baseline.

## Generated skill

Write a project-local skill with frontmatter and concrete sections:

- **Launch** — exact command, readiness check, isolation settings, and teardown;
- **Doctor** — read-only process, version, ownership, port, and authentication checks;
- **Drive** — real user paths using stable selectors, commands, or API routes;
- **Evidence** — action plus resulting state, side effects, artifact location, and proof standard;
- **Cleanup** — remove only instances and scratch state created by the run; preserve evidence;
- **Helpers** — executable scripts with documented invocation.

Do not leave placeholders, guessed selectors, guessed routes, or undocumented prerequisites.

## Feature map

Create an index and one file per initial user-facing feature, targeting three to five features. Each feature file must state:

- `Sub-features`;
- `How to get to it (user POV)`;
- `Driving it with <harness>`;
- `Gotchas`.

Describe the route from user action to observable end state. Include alternate entry points when they materially differ.

## Proof before handoff

Run the generated instructions end to end for one mapped feature:

- launch an isolated instance;
- run Doctor;
- drive the real user path;
- capture action and outcome evidence;
- clean up only what the run created;
- confirm evidence remains after cleanup.

Fix failed instructions and repeat the cleanup before retrying. A written skill that has not been executed is a draft.

Recommend `garcon-maintain-verification` for later drift checks. Keep product fixes out of this skill; report product regressions separately.
