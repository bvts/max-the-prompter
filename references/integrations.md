# Current Integration Notes

This file is intentionally a lightweight routing reference. Re-check official docs before using exact commands or APIs because third-party tools change.

## Antigravity

Current official documentation describes plugins as directories with `plugin.json`, with skills in `skills/<skill-name>/SKILL.md`. Workspace plugins can live under `.agents/plugins/`; the CLI can install a local plugin with `agy plugin install /path/to/local/plugin`. Current CLI skills can become slash commands from their names.

## Addy Osmani agent-skills

Repository: https://github.com/addyosmani/agent-skills

Current upstream lifecycle concepts include:
- using-agent-skills
- interview-me
- idea-refine
- spec-driven-development
- constraint-driven-development
- planning-and-task-breakdown
- incremental-implementation
- test-driven-development
- context-engineering
- source-driven-development
- doubt-driven-development
- frontend-ui-engineering
- api-and-interface-design
- browser-testing-with-devtools
- debugging-and-error-recovery
- code-review-and-quality
- code-simplification
- security-and-hardening
- performance-optimization
- git-workflow-and-versioning
- ci-cd-and-automation
- deprecation-and-migration
- documentation-and-adrs
- observability-and-instrumentation
- shipping-and-launch

## Impeccable

Docs: https://impeccable.style/docs/

Current documented command families cover design creation, evaluation, refinement, simplification, hardening, and system/context tasks. Use its installed skill as the source of truth.

## Motion

Docs: https://motion.dev/docs/

For React, current docs use the `motion` package and imports from `motion/react`. Verify current framework guidance, reduced-motion behavior, and performance guidance before implementation.

## KokonutUI

Docs: https://kokonutui.com/docs

Current docs describe KokonutUI as a shadcn-compatible React/Tailwind registry. Verify the current registry/configuration and component API before installation.

## Bklit UI

Docs: https://bklit.com/docs

Current docs describe Bklit UI as a shadcn registry focused on charts/data visualization, with a project-aware skill. Verify the current registry, component API, and license boundaries before using Studio assets.

## Principle

This reference is not permission to assume any tool is installed. Discover the workspace, inspect installed skills/plugins, and verify current docs at runtime.
