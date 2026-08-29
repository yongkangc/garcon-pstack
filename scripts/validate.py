#!/usr/bin/env python3
"""Validates the public garcon-pstack package with no external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "garcon-pstack"
SKILLS = PLUGIN / "skills"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot parse {path.relative_to(ROOT)}: {exc}")


def validate_manifests() -> None:
    manifest_path = PLUGIN / ".codex-plugin" / "plugin.json"
    manifest = load_json(manifest_path)
    if not isinstance(manifest, dict):
        fail("plugin manifest must be an object")
    if manifest.get("name") != "garcon-pstack":
        fail("plugin name must be garcon-pstack")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
        fail("plugin version must be strict semantic versioning")
    if manifest.get("skills") != "./skills/":
        fail("plugin skills path must be ./skills/")

    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    if not isinstance(marketplace, dict) or marketplace.get("name") != "garcon-pstack":
        fail("marketplace name must be garcon-pstack")
    entries = marketplace.get("plugins")
    if not isinstance(entries, list) or len(entries) != 1:
        fail("marketplace must contain exactly one plugin")
    entry = entries[0]
    if not isinstance(entry, dict) or entry.get("name") != "garcon-pstack":
        fail("marketplace plugin name must be garcon-pstack")
    source = entry.get("source")
    if not isinstance(source, dict) or source.get("path") != "./plugins/garcon-pstack":
        fail("marketplace source must point to ./plugins/garcon-pstack")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"missing YAML frontmatter in {path.relative_to(ROOT)}")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def validate_skills() -> None:
    expected = {
        "garcon-mode",
        "garcon-investigate",
        "garcon-design",
        "garcon-fix",
        "garcon-review",
        "garcon-verify",
        "garcon-create-verification",
        "garcon-maintain-verification",
    }
    actual = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    if actual != expected:
        fail(f"skill set differs from the intended minimum: {sorted(actual)}")
    for name in sorted(expected):
        skill_path = SKILLS / name / "SKILL.md"
        fields = parse_frontmatter(skill_path)
        if fields.get("name") != name:
            fail(f"skill name does not match directory: {name}")
        description = fields.get("description", "")
        if len(description) < 30:
            fail(f"skill description is too short: {name}")
        metadata = SKILLS / name / "agents" / "openai.yaml"
        if not metadata.is_file():
            fail(f"missing agents/openai.yaml: {name}")
        if f"${name}" not in metadata.read_text(encoding="utf-8"):
            fail(f"default prompt must mention ${name}")


def validate_public_content() -> None:
    text_files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path != Path(__file__)
        and path.suffix in {"", ".md", ".json", ".yaml", ".yml", ".py"}
    ]
    forbidden = {
        "unfinished placeholder": re.compile(r"\[(?:TODO|FIXME):", re.IGNORECASE),
        "private home path": re.compile(r"/home/[A-Za-z0-9._-]+/"),
        "private key": re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
        "GitHub token": re.compile(r"gh[opsu]_[A-Za-z0-9]{20,}"),
        "OpenAI key": re.compile(r"sk-[A-Za-z0-9]{20,}"),
        "Claude runtime path": re.compile(r"~?/\.claude(?:/|\b)"),
        "Cursor runtime path": re.compile(r"~?/\.cursor(?:/|\b)"),
    }
    for path in text_files:
        content = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in forbidden.items():
            if pattern.search(content):
                fail(f"{label} found in {path.relative_to(ROOT)}")


def validate_markdown_links() -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        content = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(content):
            target = raw_target.strip().split("#", 1)[0]
            if not target or target.startswith(("https://", "http://", "mailto:", "codex://")):
                continue
            resolved = (path.parent / unquote(target)).resolve()
            if not resolved.exists():
                fail(f"broken relative link in {path.relative_to(ROOT)}: {raw_target}")


def main() -> None:
    validate_manifests()
    validate_skills()
    validate_public_content()
    validate_markdown_links()
    print("garcon-pstack validation passed")


if __name__ == "__main__":
    main()
