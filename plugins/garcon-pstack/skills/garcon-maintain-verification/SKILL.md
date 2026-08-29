---
name: garcon-maintain-verification
description: Keep a project verification skill and feature map accurate through source review and real-user checks.
---

# Garcon Maintain Verification

Maintain an existing project-local verification skill and its feature map. Edit only that verification skill's directory and owned harness helpers. Do not modify product code during this workflow.

## Outcomes

Return exactly one outcome:

- **clean** — every mapped feature received source and live coverage with no worthwhile correction;
- **changed** — proven documentation, harness, or feature-map corrections were made;
- **blocked** — coverage or a safe correction could not finish, with the concrete blocker.

## Locate and index

Find the verification skill whose body has Launch, Doctor, Drive, Evidence, Cleanup, and a feature map. If none exists, stop and recommend `garcon-create-verification`. Read the feature-map index and enumerate its sibling files. Repair missing, duplicate, extra, or dead entries before deeper review.

## Source pass

Review each feature against current source, routes, commands, manifests, and documentation. For every feature, record:

- the user-facing behavior;
- source entry points;
- prerequisites and isolation requirements;
- one concrete live recipe;
- confirmed drift or none.

Use parallel read-only reviewers only for independent feature files. They must not drive the app or edit files. Reconcile their findings before the live pass.

## Live pass

Exercise every mapped feature at least once using the skill's own Launch and Drive instructions. For each fresh session or after surprising behavior:

- run Doctor before driving;
- use a known-good isolated instance;
- capture action and resulting-state evidence;
- preserve evidence through cleanup;
- clean up every instance or scratch artifact created by the run.

If the map describes working behavior that the harness cannot drive, fix the harness under the skill directory and re-drive it. If the app behavior is broken, report a product regression instead of weakening the map to hide it.

## Ship or stop

Re-read every changed file. Make at most one focused PR containing proven verification-skill, feature-map, or owned-harness corrections. Do not include product changes, generated run notes, credentials, private URLs, real transcripts, or host-specific secrets. For clean or blocked outcomes, do not create a PR.
