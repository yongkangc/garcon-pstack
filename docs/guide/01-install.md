# Install and confirm discovery

`garcon-pstack` is a Codex plugin distributed through a GitHub marketplace. Install it in the same environment that runs Codex.

## Install from GitHub

```shell
codex plugin marketplace add yongkangc/garcon-pstack
codex plugin add garcon-pstack@garcon-pstack
```

The first command registers the marketplace. The second installs and enables versioned plugin content from that marketplace.

## Confirm the installation

```shell
codex plugin marketplace list
codex plugin list
```

The expected plugin row is:

```text
garcon-pstack@garcon-pstack  installed, enabled
```

Codex namespaces skills supplied by plugins. The installed skill names therefore include both the plugin and skill:

```text
garcon-pstack:garcon-mode
garcon-pstack:garcon-investigate
garcon-pstack:garcon-design
garcon-pstack:garcon-fix
garcon-pstack:garcon-review
garcon-pstack:garcon-verify
```

## Invoke from Codex

Use the skill picker or mention the namespaced skill:

```text
$garcon-pstack:garcon-mode investigate the retry lifecycle and show where ownership changes
```

## Invoke from Garcon

Garcon accepts a leading slash command and resolves it through Codex skill discovery:

```text
/garcon-pstack:garcon-mode investigate the retry lifecycle and show where ownership changes
```

If a running interface cached the previous skill list, start a new chat or refresh the available commands.

Next: [Route work with `garcon-mode`](02-route-work.md).
