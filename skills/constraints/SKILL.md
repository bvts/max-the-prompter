---
name: constraints
description: Establishes and enforces a measurable project quality bar, normally persisted as CONSTRAINTS.md. Use when quality standards are missing, inconsistent, or when the user invokes /constraints.
---
# /constraints

Read `.agents/skills/max-prompter/SKILL.md` and establish the project's quality bar.

1. Inspect the repository and existing standards.
2. Preserve stronger existing rules unless the user explicitly changes them.
3. Separate hard constraints from aspirational targets.
4. Define measurable checks for correctness, maintainability, security, accessibility, performance, testing, UX, and deployment as applicable.
5. Place cheap deterministic checks early and expensive checks later.
6. Avoid arbitrary metrics that do not match project risk.
7. Write/update `CONSTRAINTS.md` unless an existing equivalent is clearly authoritative.
8. Make subsequent `/spec`, `/plan`, `/build`, `/review`, `/test`, and `/ship` workflows enforce the constraints.
9. Never satisfy a constraint by disabling or weakening the check that enforces it.
