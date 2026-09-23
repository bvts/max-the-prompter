# Release Checklist

Use this checklist before publishing a Max Prompter release.

## Repository

- [ ] `plugin.json` parses as valid JSON.
- [ ] Every skill directory contains `SKILL.md`.
- [ ] Every skill has valid YAML frontmatter with `name` and `description`.
- [ ] Skill names match their directory names.
- [ ] README installation paths match current Antigravity documentation.
- [ ] No local machine paths, API keys, tokens, or generated artifacts are committed.

## Quality

- [ ] `python scripts/validate_pack.py` passes.
- [ ] All command descriptions match the actual skill files.
- [ ] Integration references point to primary/official sources where available.
- [ ] No upstream skill was copied into the repository without permission.
- [ ] Any unstable command/API claim has a current source.

## GitHub

- [ ] Repository description is set.
- [ ] Topics identify Antigravity, agent-skills, prompt-engineering, and AI coding workflows.
- [ ] License is enabled.
- [ ] Issue templates are enabled.
- [ ] Security contact/process is configured.
- [ ] Default branch is protected if multiple contributors are expected.
- [ ] CI is green.
- [ ] First release notes summarize user-visible changes.

## Release artifact

- [ ] ZIP contains only intended repository files.
- [ ] ZIP can be extracted without changing the directory structure.
- [ ] `plugin.json` is at the plugin root.
- [ ] `skills/` contains the command skills.
- [ ] The installation instructions have been tested from a clean machine/profile when practical.
