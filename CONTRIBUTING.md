# Contributing to Max Prompter

Thanks for contributing.

## What makes a good contribution?

A strong contribution improves agent outcomes without adding vague verbosity. Prefer changes that add a clear decision rule, verification step, reusable workflow, safety boundary, integration, example, or correction based on authoritative documentation.

## Repository structure

```text
skills/
  <command>/SKILL.md       Agent skill definitions
references/                Integration and routing notes
docs/                      Maintainer-facing documentation
scripts/                   Dependency-free repository checks
.github/                   CI and contribution templates
plugin.json                Antigravity plugin manifest
README.md                  Public documentation
```

## Skill changes

Every skill should:

1. Have a `SKILL.md` with YAML frontmatter.
2. Use a lowercase, hyphen-separated skill name matching its directory.
3. Have a clear, trigger-focused `description`.
4. Define a concrete workflow rather than functioning as a generic reference dump.
5. Include verification/exit criteria where the task warrants them.
6. Avoid inventing tool capabilities, commands, package APIs, or installed dependencies.
7. Prefer repository truth and current authoritative documentation over assumptions.

## Integration changes

When adding or changing an integration:

- link to the primary source;
- state whether the dependency is optional or required;
- avoid copying large upstream skill files into this repository;
- describe fallback behavior when the integration is unavailable;
- re-check current commands/API names before merging.

## Pull requests

Keep each PR focused. Explain:

- what changed;
- why it changed;
- how it was verified;
- whether current documentation was checked;
- whether any command names or install paths changed.

Run the repository validator before opening a PR:

```powershell
python scripts/validate_pack.py
```
