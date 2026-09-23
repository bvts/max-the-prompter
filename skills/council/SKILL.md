---
name: council
description: Pressure-tests meaningful decisions through a five-advisor Council using Contrarian, First Principles, Expansionist, Outsider, and Executor perspectives, peer review, and chairman synthesis. Use when the user asks to council, debate, pressure-test, stress-test, validate, or resolve a genuine multi-option decision.
---
# /council — COUNCIL OF FIVE

This skill implements the Council-of-5 methodology supplied for this pack and is compatible with Ole Lehmann's `llm-council` concept.

## Trigger

Strong triggers:
- council this
- run the council
- war room this
- pressure-test this
- stress-test this
- debate this

Strong decision triggers when a real tradeoff exists:
- should I X or Y
- which option
- what would you do
- is this the right move
- validate this
- get multiple perspectives
- I can't decide
- I'm torn between

Do not use for trivial facts or obvious yes/no questions.

## Advisors

1. Contrarian — seek failure modes, missing assumptions, hidden costs.
2. First Principles Thinker — reconstruct the problem from fundamentals.
3. Expansionist — find upside, scale, adjacent opportunity, compounding effects.
4. Outsider — challenge jargon and expert blind spots from fresh context.
5. Executor — test feasibility, sequencing, dependencies, and first action.

## Process

### 1. Enrich context

Inspect only relevant workspace context:
- project instructions
- product/business docs
- constraints
- referenced files
- existing implementation
- prior council artifacts

### 2. Frame the question

Produce a neutral frame containing:
- core decision
- context
- options
- constraints
- stakes
- success criteria
- known unknowns

Do not insert your own conclusion.

### 3. Independent advisors

Use five parallel subagents when available. Each receives only the framed decision and its own perspective. Encourage direct, specific analysis and explicit assumptions.

### 4. Blind peer review

Anonymize outputs as A–E and randomize advisor mapping. Use parallel reviewers when available. Each reviewer identifies:
- strongest response and why
- biggest blind spot
- what all responses missed

### 5. Chairman synthesis

Synthesize:
- Where the Council Agrees
- Where the Council Clashes
- Blind Spots the Council Caught
- The Recommendation
- The One Thing to Do First

For political/electoral matters, keep the synthesis neutral and factual; do not rank candidates, endorse political choices, predict outcomes, or otherwise steer political decisions.

### 6. Artifacts

For full sessions, save:
- `council-report-[timestamp].html`
- `council-transcript-[timestamp].md`

The HTML must be self-contained and easy to scan, with collapsible advisor/review sections and a concise chairman synthesis.

If an installed `llm-council` skill is available, delegate to it instead of duplicating the same workflow.
