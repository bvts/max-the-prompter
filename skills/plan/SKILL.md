---
name: plan
description: Converts a project specification into dependency-ordered, atomic, verifiable implementation tasks. Use after requirements are known and before substantial implementation.
---
# /plan

Read `.agents/skills/max-prompter/SKILL.md`.

Prefer an installed `planning-and-task-breakdown` skill from `addyosmani/agent-skills` when available.

Create a plan that:
- preserves architecture intent
- orders dependencies correctly
- uses small vertical slices
- identifies files/modules likely to change
- includes acceptance criteria per task
- includes verification per task
- identifies migration/destructive-risk steps
- makes the plan executable by an autonomous coding agent

Do not turn the plan into a list of vague headings. Every task must have a concrete outcome.
