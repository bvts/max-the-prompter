#!/usr/bin/env python3
"""Dependency-free validation for the Max Prompter Antigravity plugin."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugin.json"
CODEX_PLUGIN = ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
SKILLS = ROOT / "skills"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    if not PLUGIN.is_file():
        fail("plugin.json is missing")

    try:
        manifest = json.loads(PLUGIN.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"plugin.json is invalid JSON: {exc}")

    if not isinstance(manifest.get("name"), str) or not manifest["name"].strip():
        fail("plugin.json must contain a non-empty name")
    if not isinstance(manifest.get("description"), str) or not manifest["description"].strip():
        fail("plugin.json must contain a non-empty description")

    try:
        codex_manifest = json.loads(CODEX_PLUGIN.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(".codex-plugin/plugin.json is missing")
    except json.JSONDecodeError as exc:
        fail(f".codex-plugin/plugin.json is invalid JSON: {exc}")

    if codex_manifest.get("skills") != "./skills/":
        fail(".codex-plugin/plugin.json must discover the canonical ./skills/ directory")

    try:
        marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(".agents/plugins/marketplace.json is missing")
    except json.JSONDecodeError as exc:
        fail(f".agents/plugins/marketplace.json is invalid JSON: {exc}")

    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or not any(
        isinstance(item, dict) and item.get("name") == "max-the-prompter"
        for item in plugins
    ):
        fail("marketplace must contain the max-the-prompter plugin")

    if not SKILLS.is_dir():
        fail("skills/ directory is missing")

    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    if not skill_dirs:
        fail("skills/ contains no skill directories")

    name_pattern = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    seen = set()

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            fail(f"{skill_dir.relative_to(ROOT)} is missing SKILL.md")
        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            fail(f"{skill_file.relative_to(ROOT)} is missing YAML frontmatter")
        end = text.find("\n---\n", 4)
        if end == -1:
            fail(f"{skill_file.relative_to(ROOT)} has malformed frontmatter")
        frontmatter = text[4:end]
        fields = {}
        for line in frontmatter.splitlines():
            if ":" in line and not line.startswith((" ", "\t")):
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip().strip('"').strip("'")
        name = fields.get("name")
        description = fields.get("description")
        if not name:
            fail(f"{skill_file.relative_to(ROOT)} frontmatter is missing name")
        if not description:
            fail(f"{skill_file.relative_to(ROOT)} frontmatter is missing description")
        if name != skill_dir.name:
            fail(f"{skill_file.relative_to(ROOT)} name '{name}' does not match directory '{skill_dir.name}'")
        if not name_pattern.match(name):
            fail(f"skill name '{name}' is not lowercase-hyphenated")
        if name in seen:
            fail(f"duplicate skill name: {name}")
        seen.add(name)

    required = {
        "max-prompter", "prompt", "constraints", "council", "spec", "plan",
        "build", "design", "audit", "review", "test", "ship", "cleanmemory", "skillinstall", "re"
    }
    missing = sorted(required - seen)
    if missing:
        fail("missing required Max Prompter skills: " + ", ".join(missing))

    print(f"PASS: {len(skill_dirs)} skills validated; plugin manifest is valid.")
    print("PASS: ChatGPT/Codex compatibility manifest and marketplace are valid.")
    print("Skills:", ", ".join(sorted(seen)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
