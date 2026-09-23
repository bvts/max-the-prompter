---
name: ship
description: Prepares and verifies a project for production release, including tests, build, deployment configuration, security, observability, rollback, documentation, and launch checks. Use when the user asks to ship, release, deploy, or prepare production.
---
# /ship

Read `.agents/skills/max-prompter/SKILL.md`.

Prefer installed `shipping-and-launch`, `git-workflow-and-versioning`, `ci-cd-and-automation`, `security-and-hardening`, `observability-and-instrumentation`, `performance-optimization`, `documentation-and-adrs`, and `deprecation-and-migration` skills from `addyosmani/agent-skills` where applicable.

Do not treat a successful local build as sufficient proof of production readiness.

Check:
1. working tree and diff
2. tests and regression coverage
3. production build
4. environment/configuration
5. secrets
6. dependency state
7. migrations and rollback
8. security-sensitive behavior
9. observability/health checks
10. performance-sensitive areas
11. deployment settings
12. smoke tests after deployment when access exists

Use staged rollout/feature flags when the project warrants them.

Final handoff must state:
- what shipped
- what was verified
- deployment target/status
- any known limitations
- rollback path
