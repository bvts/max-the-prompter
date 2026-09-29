---
name: build
description: Implements an approved plan in coherent, verifiable slices while preserving existing architecture and behavior. Use for actual implementation after requirements and constraints are understood.
---
# /build

Read `.agents/skills/max-prompter/SKILL.md`.

Use relevant installed specialist skills instead of duplicating them.

Follow this loop:

1. Inspect the relevant repository context and current state.
2. Implement one coherent slice of the approved plan.
3. Run the verification appropriate to that slice.
4. Inspect the actual result, including failures and generated output.
5. Fix regressions or incomplete behavior before continuing.
6. Integrate the completed slices and verify the final behavior.

Preserve existing functionality unless the approved requirements explicitly change it. Do not hide failures, leave placeholder implementations, or claim completion without evidence.
