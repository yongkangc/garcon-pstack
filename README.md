# garcon-pstack

A small, evidence-first engineering workflow for [OpenAI Codex](https://developers.openai.com/codex/) and [Garcon](https://github.com/cfal/garcon).

`garcon-pstack` packages eight focused skills for investigation, design, defect fixing, review, verification-skill generation, and verification-skill maintenance. It keeps the useful idea behind pstack, a dispatcher backed by rigorous engineering playbooks, while removing runtime-specific assumptions and heavyweight orchestration.

New users should start with [The garcon-pstack guide](docs/guide/README.md). It walks through installation, routing, each workflow, Garcon integration, and copyable recipes.

## Why this exists

[Cursor pstack](https://github.com/cursor/plugins/tree/main/pstack) is a broad workflow system built around Cursor primitives, model panels, agents, playbooks, and automation. [pstack-claude](https://github.com/michael-denyer/pstack-claude) ports much of that system to Claude Code and provides a Codex compatibility layer.

This repository is a clean-room, Codex-native implementation. It is inspired by the public pstack architecture but does not copy its skill text or code.

The smaller scope is intentional:

- Six skills instead of a large skill graph.
- No startup hooks or always-on prompt injection.
- No transcript readers or runtime-specific history paths.
- No model names embedded in workflow instructions.
- No durable orchestration database.
- No dependency on Graphite, GitHub CLI, or MCP servers.

## Skills

| Skill | Purpose |
| --- | --- |
| `garcon-mode` | Route a task to the smallest relevant workflow. |
| `garcon-investigate` | Produce a read-only, evidence-backed explanation. |
| `garcon-design` | Settle data shape, ownership, interfaces, and failure behavior. |
| `garcon-fix` | Reproduce and fix a defect at its root cause. |
| `garcon-review` | Review an exact change for confirmed defects. |
| `garcon-verify` | Test claims against the real artifact. |
| `garcon-create-verification` | Generate a project-local verification skill and feature map. |
| `garcon-maintain-verification` | Keep a verification skill and feature map accurate as the project changes. |

Each skill works independently. `garcon-mode` is the convenient entry point for tasks that need routing.

## Install

Add the repository marketplace and install the plugin:

```shell
codex plugin marketplace add yongkangc/garcon-pstack
codex plugin add garcon-pstack@garcon-pstack
```

Restart Codex after installation if the skill list is already cached.

For local development:

```shell
git clone https://github.com/yongkangc/garcon-pstack.git
cd garcon-pstack
codex plugin marketplace add "$PWD"
codex plugin add garcon-pstack@garcon-pstack
```

## Use with Codex

Invoke a skill explicitly:

```text
$garcon-pstack:garcon-mode investigate why this worker can outlive its owning chat
$garcon-pstack:garcon-review review the current branch against main
$garcon-pstack:garcon-verify verify that the fix closes the original lifecycle gap
```

Codex may also select a skill from its description when the request is a close match.

## Use with Garcon

Garcon discovers Codex skills through the Codex app-server. Its Codex integration accepts leading slash invocations, so use:

```text
/garcon-pstack:garcon-mode investigate why this worker can outlive its owning chat
```

Plugin skills are namespaced by Codex. The `garcon-pstack:` prefix is therefore part of every installed command name.

Garcon persists shared agent skills under its `agents-home` volume in container deployments. Install the plugin inside the same environment that runs Codex so the app-server can discover it.

This plugin does not modify Garcon core, read Garcon's transcript ledger, or control other chats. Cross-chat delegation should continue to use the official [cfal/garcon-skills](https://github.com/cfal/garcon-skills) package.

## Design boundaries

The workflow follows four constraints:

- Facts, inferences, and unknowns stay distinct.
- Repository instructions and user authorization remain authoritative.
- Parallel work is bounded and only used for independent questions.
- Completion claims require evidence from the real artifact.

There are no hooks. Invocation is explicit or based on normal Codex skill discovery. There is no hidden state and no network service.

## Validate

Run the repository validator with Python 3:

```shell
python3 scripts/validate.py
```

It checks plugin metadata, marketplace paths, skill frontmatter, unfinished placeholders, runtime-specific coupling, and common secret patterns.

## Security and privacy

The plugin contains instructions only. It does not transmit data, read credentials, or install executable dependencies.

Do not commit credentials, private URLs, real transcripts, customer data, or internal identifiers. Examples and fixtures must use synthetic values.

## Credits

The dispatcher-and-playbook concept is inspired by [Lauren Tan's pstack](https://github.com/cursor/plugins/tree/main/pstack). The lightweight integration target is [cfal/garcon](https://github.com/cfal/garcon).

This project is independently implemented and released under the MIT License.
