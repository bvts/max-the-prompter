---
name: review
description: Runs a structured pre-merge review of changes for correctness, architecture, readability, maintainability, security, performance, tests, and accidental scope creep. Use before merging or finalizing substantial changes.
---
# /review

Read `.agents/skills/max-prompter/SKILL.md`.

Prefer installed `code-review-and-quality`, `code-simplification`, `security-and-hardening`, and `performance-optimization` skills from `addyosmani/agent-skills` when applicable.

Review the actual diff and surrounding code.

Check:
- correctness
- interface contracts
- error handling
- tests
- security
- performance
- accessibility where relevant
- maintainability
- duplication
- naming
- unexpected changes
- documentation impact

Classify findings by severity and provide evidence. Fix critical findings before declaring the work ready.
