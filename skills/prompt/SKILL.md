---
name: prompt
description: Generates an execution-ready implementation prompt from a user request or project context using the Max Prompter workflow. Use when the user asks for a detailed, comprehensive, long, or production-grade prompt.
---
# /prompt

Read `.agents/skills/max-prompter/SKILL.md` and apply its full workflow.

Goal: produce the best execution-ready prompt for the current request.

Rules:
- Inspect relevant repository context first.
- Discover installed skills and delegate to them where appropriate.
- Use current official documentation for unstable dependencies and commands.
- For UI work, apply the visual specialization and inspect current UI-library/tooling docs.
- For meaningful decisions, use `/council` or an installed `llm-council` skill.
- Make requirements concrete and testable.
- Include architecture, file/module boundaries, edge cases, acceptance criteria, verification, and definition of done when relevant.
- Do not fill space with repetition.
- When the user explicitly wants a massive prompt, use maximal detail rather than a shallow summary.
