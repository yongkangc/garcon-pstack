# Use garcon-pstack through Garcon

[Garcon](https://github.com/cfal/garcon) hosts Codex sessions and exposes discovered Codex skills as slash commands.

## Install in the Codex environment

The marketplace must be installed wherever the Codex process used by Garcon reads its configuration. In a container deployment, run the installation inside the Garcon container so it reaches the container's Codex home.

Garcon keeps shared skills and each agent's native state in persistent volumes. The plugin itself remains a Codex plugin and does not become part of Garcon core.

## Use the full namespaced command

Garcon resolves the exact names returned by Codex. Plugin skills include their namespace:

```text
/garcon-pstack:garcon-mode
/garcon-pstack:garcon-investigate
/garcon-pstack:garcon-design
/garcon-pstack:garcon-fix
/garcon-pstack:garcon-review
/garcon-pstack:garcon-verify
```

Trailing text becomes the task passed alongside the skill:

```text
/garcon-pstack:garcon-review review the current branch against main and do not edit
```

## Keep ownership boundaries clear

`garcon-pstack` owns engineering workflow guidance. It does not:

- Read or write Garcon's transcript ledger.
- Start, steer, or stop other Garcon chats.
- Persist an orchestration queue.
- Change chat permissions, model, or effort settings.
- Bypass Garcon's execution ownership.

Use [cfal/garcon-skills](https://github.com/cfal/garcon-skills) for explicit cross-chat delegation. Use Garcon itself for session lifecycle, steering, transcript export, handoff, and review.

## Parallel work

The skills permit bounded parallel investigation when questions are independent and the runtime supports it. Garcon may also run separate visible chats. These are different mechanisms:

```text
Codex subagents: one parent owns synthesis inside a turn.
Garcon chats: separate sessions with explicit user-visible ownership.
```

Choose separate Garcon chats when work needs distinct models, permissions, branches, or long-lived ownership.

Next: [Recipes and boundaries](07-recipes-and-boundaries.md).
