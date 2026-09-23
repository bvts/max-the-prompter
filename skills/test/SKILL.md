---
name: test
description: Proves that a project or change works using the smallest useful combination of unit, integration, component, browser, end-to-end, performance, and security checks. Use to verify implementation rather than merely compile it.
---
# /test

Read `.agents/skills/max-prompter/SKILL.md`.

Prefer installed `test-driven-development`, `browser-testing-with-devtools`, and `debugging-and-error-recovery` skills when applicable.

Choose tests based on risk.

Verify:
- happy path
- important alternate path
- failure path
- regression cases
- integration boundaries
- runtime/browser behavior when relevant

Never hide failures by disabling tests or weakening checks without an explicit, documented reason.

Report exactly what was run and what evidence it produced.
