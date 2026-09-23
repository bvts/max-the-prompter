# Max Prompter for Antigravity

> **A universal prompt architect and project-orchestration skill pack for Google Antigravity.**
>
> Turn rough ideas into detailed implementation prompts, establish a hard quality bar, pressure-test important decisions with a Council of Five, route work through specialist skills, verify the result, and prepare it for production.

[![Validate](https://github.com/Tofu4K/max-the-prompter/actions/workflows/validate.yml/badge.svg)](https://github.com/Tofu4K/max-the-prompter/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> This repository is published at `https://github.com/Tofu4K/max-the-prompter`.

---

## Table of contents

- [What it is](#what-it-is)
- [Core idea](#core-idea)
- [How it works](#how-it-works)
- [Commands](#commands)
- [The normal workflow](#the-normal-workflow)
- [Council of Five](#council-of-five)
- [Universal project support](#universal-project-support)
- [UI and design specialization](#ui-and-design-specialization)
- [Third-party skill routing](#third-party-skill-routing)
- [Prompt detail levels](#prompt-detail-levels)
- [Quality and verification](#quality-and-verification)
- [Context isolation](#context-isolation)
- [Workspace skill installation](#workspace-skill-installation)
- [Reverse engineering](#reverse-engineering)
- [Installation](#installation)
- [Repository structure](#repository-structure)
- [Development](#development)
- [GitHub publication](#github-publication)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)

---

# What it is

Max Prompter is an **Antigravity plugin containing multiple agent skills**.

It is built around a simple problem:

```text
User idea
   ↓
“Build me X”
   ↓
Agent has dozens of hidden decisions to make
   ↓
Inconsistent implementation
```

Max Prompter attempts to make those hidden decisions explicit before implementation.

Instead of turning:

```text
Build me a marketplace.
```

into a slightly longer version of the same sentence, it can turn the request into a structured implementation contract covering:

- project goals;
- non-goals;
- constraints;
- assumptions;
- architecture;
- technology choices;
- repository structure;
- modules/components;
- data models;
- API/interface contracts;
- state management;
- user flows;
- system flows;
- UI/UX behavior;
- accessibility;
- responsive behavior;
- performance;
- security;
- error handling;
- observability;
- testing;
- acceptance criteria;
- edge cases;
- failure/recovery;
- rollout and rollback;
- definition of done.

The objective is **useful specificity**, not arbitrary prompt length.

---

# Core idea

Max Prompter treats an AI coding agent more like an autonomous engineering team member than a text generator.

The system therefore asks five different questions throughout a project:

```text
1. What exactly are we building?
2. What constraints define quality?
3. What decisions need pressure-testing?
4. How should the work actually be implemented?
5. How do we prove it works and ship it safely?
```

That produces the overall lifecycle:

```text
IDEA
 ↓
CONTEXT
 ↓
PROMPT / SPEC
 ↓
CONSTRAINTS
 ↓
DECISIONS
 ↓
PLAN
 ↓
BUILD
 ↓
TEST
 ↓
REVIEW / AUDIT
 ↓
SHIP
```

Not every project needs every stage. Max Prompter chooses based on the actual task.

---

# How it works

## 1. Repository/context discovery

Max Prompter starts with the workspace instead of guessing.

It looks for relevant project truth such as:

```text
README.md
AGENTS.md
CLAUDE.md
GEMINI.md
CONSTRAINTS.md
PRODUCT.md
DESIGN.md
ADR files
package manifests
lockfiles
source directories
tests
CI configuration
deployment configuration
database migrations
existing skills
existing plugins
MCP configuration
previous prompt/spec artifacts
previous Council transcripts
```

It should avoid blindly reading an entire repository. Search for high-signal context first, then inspect the files that materially affect the request.

## 2. Task classification

The same prompt architecture is not appropriate for every project.

Max Prompter first determines whether the work is primarily:

- UI/UX;
- frontend;
- backend/API;
- desktop;
- mobile;
- CLI/tooling;
- data/ML;
- infrastructure;
- automation;
- game/interactive;
- library/SDK;
- documentation;
- mixed architecture.

The project type changes what deserves depth.

## 3. Skill discovery

Before duplicating a workflow, Max Prompter looks for already-installed specialist skills.

Antigravity skills are folders containing `SKILL.md`, with the skill description used for relevance detection and the full instructions loaded when a skill is activated. Current Antigravity documentation describes global skills under `~/.gemini/antigravity/skills/` and workspace skills under `<workspace>/.agents/skills/`. See the official documentation: https://www.antigravity.google/docs/ide/skills/ .

Plugins are bundles that can contain skills, rules, MCP configuration, and hooks. Current Antigravity documentation describes `plugin.json` at the plugin root with skills under `skills/<skill-name>/SKILL.md`, plus workspace and global plugin locations. See: https://www.antigravity.google/docs/plugins .

## 4. Prompt architecture

The main Max prompt uses a deep structure rather than repetitive prose.

A large project may include:

```text
A. Executive brief
B. Operating mode
C. Context package
D. Goals
E. Non-goals
F. Functional requirements
G. User/system flows
H. Architecture
I. Technology decisions
J. Directory/file plan
K. Data model
L. API/interface contracts
M. State management
N. UI/UX system
O. Accessibility
P. Responsiveness
Q. Performance
R. Security
S. Error handling
T. Observability
U. Test strategy
V. Implementation plan
W. Acceptance criteria
X. Edge-case matrix
Y. Failure/rollback plan
Z. Definition of done
```

Not every section is mandatory. The prompt adapts to the project.

## 5. Verification

Max Prompter treats implementation as incomplete when important behavior has not been proven.

Proof can mean:

- automated tests;
- type checks;
- builds;
- browser verification;
- API contract checks;
- migration tests;
- filesystem safety checks;
- security review;
- performance measurement;
- rendered UI inspection;
- smoke tests;
- deployment verification.

---

# Commands

The plugin ships these 15 skill commands:

```text
/max-prompter
/prompt
/constraints
/council
/spec
/plan
/build
/design
/audit
/review
/test
/ship
/cleanmemory
/skillinstall
/re
```

A detailed command reference is available in [`docs/COMMANDS.md`](docs/COMMANDS.md).

## `/max-prompter`

The main universal orchestrator.

Use it when you want Max to decide the appropriate amount of discovery, prompt depth, specialization, verification, and release preparation.

```text
/max-prompter
Build me a full-stack marketplace for digital products.
```

The orchestrator should inspect the project, classify the task, discover skills, identify decisions, choose a workflow, and produce an execution-ready result.

## `/prompt`

The prompt-generation command.

```text
/prompt
Build a production-ready desktop app that catalogs local files and provides safe batch operations.
```

Its job is to expand the user's idea into an implementation-ready prompt instead of immediately rushing into code.

## `/constraints`

Sets the project's quality bar.

```text
/constraints
Make the project production-grade and preserve user data above all else.
```

For appropriate projects, the workflow can create or update:

```text
CONSTRAINTS.md
```

Constraints should be observable or testable whenever practical.

## `/council`

Runs the five-advisor pressure-testing process for meaningful decisions.

```text
/council
Should the application be local-first or cloud-first?
```

See [Council of Five](#council-of-five).

## `/spec`

Turns an idea or feature into a formal specification.

```text
/spec
Define the complete specification for the local-first file manager feature.
```

## `/plan`

Turns the specification into dependency-ordered implementation tasks.

```text
/plan
```

The plan should identify affected files/modules and how each meaningful step is verified.

## `/build`

Executes implementation incrementally.

```text
/build
```

Preferred loop:

```text
Inspect
 ↓
Implement coherent slice
 ↓
Verify
 ↓
Read the result
 ↓
Fix
 ↓
Continue
 ↓
Integrate
 ↓
Verify final behavior
```

## `/design`

Runs the visual/UI specialization when appropriate.

```text
/design
```

It should first understand the project's design system and existing components, then choose suitable tools.

## `/audit`

Searches for things that may still be wrong.

```text
/audit
```

It can cover architecture, correctness, security, accessibility, performance, UX, runtime behavior, dependencies, deployment, and observability.

## `/review`

Performs a structured adversarial review.

```text
/review
```

The goal is to challenge the implementation rather than rubber-stamp it.

## `/test`

Builds the appropriate proof strategy and runs available checks.

```text
/test
```

The exact tests depend on the project.

## `/ship`

Performs the production/release gate.

```text
/ship
```

The skill checks the things that can break between “works locally” and “safe to release”.

---

# The normal workflow

## Greenfield project

```text
User idea
   ↓
/prompt
   ↓
/constraints
   ↓
/spec
   ↓
/plan
   ↓
/design   ← if visual
   ↓
/build
   ↓
/test
   ↓
/review
   ↓
/ship
```

## Architecture decision

```text
/council
   ↓
/spec
   ↓
/plan
```

## Existing project

```text
/audit
   ↓
/plan
   ↓
/build
   ↓
/test
   ↓
/review
```

## UI refinement

```text
/design
   ↓
Impeccable workflow if installed
   ↓
/test
   ↓
/audit
```

These are workflows, not mandatory rituals. The agent should avoid running unnecessary stages.

---

# Council of Five

Max Prompter includes a fallback implementation based on the **Council of Five / `llm-council` methodology supplied for this project**.

The purpose is not to ask five agents for five answers and pick the most common answer.

Instead:

```text
Decision
 ↓
Context enrichment
 ↓
Neutral framing
 ↓
5 independent analyses
 ↓
Anonymization
 ↓
5 independent peer reviews
 ↓
Chairman synthesis
```

## The five advisors

### 1. The Contrarian

Looks for fatal flaws, missing assumptions, failure modes, hidden costs, and reasons the proposed path could fail.

### 2. The First Principles Thinker

Strips away assumptions, asks what problem actually needs solving, and rebuilds the reasoning from fundamentals.

### 3. The Expansionist

Looks for upside, adjacent opportunities, underestimated potential, and what happens if the project succeeds beyond expectations.

### 4. The Outsider

Uses only the information actually available and looks for jargon, confusing framing, and assumptions an informed insider may no longer notice.

### 5. The Executor

Cares about feasibility, sequencing, operational friction, effort, dependencies, and the first concrete action.

## Context enrichment

Before convening the Council, the skill can inspect:

- project instructions;
- product docs;
- constraints;
- relevant source files;
- existing data;
- previous Council transcripts;
- files explicitly referenced by the user.

It should keep discovery focused and avoid wasting time scanning unrelated content.

## Advisor phase

All five advisors should be run independently and, where subagent execution is available, in parallel.

Each advisor receives:

- its identity/thinking style;
- the framed decision;
- relevant context;
- a direct instruction to represent its lens strongly rather than trying to synthesize the other perspectives.

## Peer-review phase

The five responses are anonymized to `Response A` through `Response E` and reviewed independently.

Each reviewer addresses:

1. Which response is strongest and why?
2. Which has the largest blind spot and what is missing?
3. What did all responses miss?

The Council should not reveal advisor identities during the anonymous review round.

## Chairman phase

The final synthesis should preserve genuine disagreement instead of flattening it.

The supplied methodology uses:

```text
Where the Council Agrees
Where the Council Clashes
Blind Spots the Council Caught
The Recommendation
The One Thing to Do First
```

When filesystem/artifact capabilities permit, the workflow can also produce a visual report and a full transcript.

## Do not run the Council for trivial questions

Examples that do not need Council:

```text
What is 12 × 8?

What file extension does JSON use?

Which folder contains this existing file?
```

The Council is for decisions where multiple perspectives genuinely add value.

If the original `llm-council` skill is installed, Max Prompter should prefer the installed implementation rather than running a duplicate workflow.

---

# Universal project support

Max Prompter adapts its emphasis to the project instead of forcing a website-shaped architecture everywhere.

## Web apps and websites

Emphasize:

- information architecture;
- UI system;
- responsive behavior;
- accessibility;
- browser verification;
- performance;
- data/API boundaries;
- SEO when relevant;
- deployment.

## Desktop apps

Emphasize:

- native OS behavior;
- filesystem permissions;
- local data integrity;
- packaging;
- update strategy;
- crash recovery;
- platform-specific behavior.

## Mobile apps

Emphasize:

- platform conventions;
- navigation;
- permissions;
- offline/online transitions;
- device constraints;
- accessibility;
- app-store packaging/release requirements where relevant.

## APIs and backend systems

Emphasize:

- contracts;
- validation;
- authorization;
- data integrity;
- migrations;
- retries;
- rate limits;
- observability;
- failure semantics;
- tests.

## CLI and developer tooling

Emphasize:

- arguments;
- flags;
- exit codes;
- stdout/stderr;
- interactive/non-interactive behavior;
- configuration;
- shell safety;
- packaging;
- cross-platform behavior.

## Data and ML

Emphasize:

- schemas;
- lineage;
- reproducibility;
- evaluation;
- leakage prevention;
- input validation;
- resource usage;
- model/data monitoring.

## Games and interactive projects

Emphasize:

- state machines;
- input systems;
- game loop behavior;
- assets;
- performance;
- persistence;
- deterministic testing where useful;
- platform/input differences.

## Infrastructure and DevOps

Emphasize:

- idempotency;
- environments;
- secrets;
- least privilege;
- monitoring;
- rollback;
- disaster recovery;
- cost controls;
- CI/CD.

---

# UI and design specialization

Max Prompter has an intentionally strong UI workflow, but UI libraries are **optional tools**, not mandatory dependencies.

## Design-first principle

Do not jump straight from “build this site” to isolated components.

First establish:

```text
product intent
 ↓
information hierarchy
 ↓
visual direction
 ↓
typography
 ↓
spacing/grid
 ↓
color roles
 ↓
surfaces
 ↓
component grammar
 ↓
interaction states
 ↓
responsive rules
 ↓
motion principles
```

Then implement.

## Impeccable

When the relevant Impeccable skill is installed, use it for design creation, visual critique, refinement, simplification, hardening, context extraction, and similar UI workflows.

Do not hard-code exact third-party command names into a project prompt without checking the currently installed skill/documentation.

Primary docs:

https://impeccable.style/docs/

## Motion

For React projects, Motion is an optional choice for meaningful interaction and animation.

Current Motion documentation uses the `motion` package and imports such as:

```text
motion/react
```

Motion also documents reduced-motion support. Max Prompter therefore treats accessibility as part of the animation decision rather than as an afterthought.

Primary docs:

- https://motion.dev/docs/react
- https://motion.dev/docs/react-use-reduced-motion

## KokonutUI

For projects already using or compatible with React/Tailwind/shadcn-style tooling, KokonutUI can be considered as a component source.

The agent should inspect:

- current component architecture;
- existing primitives;
- project aliases;
- design direction;
- current KokonutUI documentation.

It should not introduce a second competing component system merely because the registry exists.

Primary docs:

https://kokonutui.com/docs

## Bklit UI

For charts and data visualization, Bklit UI can be considered when its current shadcn registry patterns fit the project.

Current documentation describes an `@bklit` registry and a project-aware skill for chart/data-visualization workflows.

Primary docs:

- https://bklit.com/docs/installation
- https://bklit.com/docs/skills

## Tool-selection rule

```text
Need a tool?
  ↓
Does the project already have one?
  ├─ yes → prefer it unless there is a strong reason not to
  └─ no
       ↓
Is a specialist tool clearly appropriate?
  ├─ yes → evaluate it against project constraints
  └─ no → keep the implementation simple
```

**Use the right tool, not every tool.**

---

# Third-party skill routing

## Addy Osmani — `agent-skills`

Max Prompter is designed to **route into** Addy Osmani's `agent-skills` collection when it is installed instead of copying the upstream repository into this pack.

Current upstream documentation describes 25 skills: 24 lifecycle skills plus the `using-agent-skills` meta-skill. The collection covers requirements/definition, specification, constraints, planning, implementation, testing, source-driven development, doubt-driven development, frontend UI engineering, API/interface design, browser testing, debugging, review, security, performance, versioning, CI/CD, documentation, observability, migration, and shipping.

Repository:

https://github.com/addyosmani/agent-skills

The exact current inventory and commands should always be taken from the upstream repository rather than this README.

## Why Max Prompter does not copy the upstream skills

Vendoring every upstream skill would:

- freeze outdated instructions;
- create duplication;
- increase synchronization burden;
- create unnecessary licensing/maintenance complexity;
- make the pack larger without making it smarter.

Instead, Max Prompter keeps the orchestration layer and delegates to whatever specialist implementations are currently installed.

## Other integrations

The same rule applies to:

- Ole Lehmann's `llm-council`;
- Impeccable;
- Motion;
- KokonutUI;
- Bklit UI;
- project-native skills;
- additional future specialist skills.

---

# Prompt detail levels

Max Prompter supports progressive depth.

## L1 — Quick

Use for tiny, unambiguous tasks where additional architecture would create noise.

## L2 — Detailed

Use for normal implementation work.

## L3 — Comprehensive

Use for substantial features or systems with several interacting parts.

## L4 — Maximal

Use for large, architecture-heavy, greenfield, multi-system, or high-risk projects where exhaustive detail materially improves execution.

A user can ask explicitly for a **maximal prompt**.

The system should still obey the core rule:

> **Do not increase length by repeating yourself. Increase usefulness by removing ambiguity.**

---

# Quality and verification

## No-placeholder policy

Implementation prompts should avoid vague instructions such as:

```text
TODO: implement later

finish the rest

use a suitable library

add your own logic

insert API here
```

unless the missing item genuinely requires an unresolved user decision.

When the information can be determined responsibly, name the:

- file;
- module;
- interface;
- behavior;
- dependency;
- data shape;
- test;
- acceptance criterion.

## Source-driven verification

Tools and APIs change.

When current information matters, Max Prompter should verify primary sources before embedding a claim in an implementation plan.

Prefer:

1. official product documentation;
2. official repositories;
3. official registries;
4. primary-source examples;
5. strong secondary sources when primary evidence is unavailable.

This applies especially to:

- package APIs;
- CLI commands;
- Antigravity behavior;
- third-party component APIs;
- registries;
- cloud/deployment features;
- framework versions;
- model/tool interfaces.

## Acceptance criteria

A strong project ends with criteria that can actually be checked.

Examples:

```text
Behavior:
Given X, when Y occurs, Z happens.

Quality:
No source file is overwritten unless explicit in-place mode is enabled.

Verification:
The test suite proves X and the production build succeeds.

Failure:
Malformed input results in a recoverable error without corrupting existing data.
```

## Review loop

Max Prompter uses a layered review mindset:

```text
Completeness
 ↓
Consistency
 ↓
Executability
 ↓
Verifiability
 ↓
Maintainability
 ↓
Failure resistance
```

---


# Context isolation

## `/cleanmemory`

`/cleanmemory` is designed for people who move between many projects and do not want old project context to contaminate the current task.

Run:

```text
/cleanmemory
```

The command establishes a clean Max Prompter project-context boundary. It looks only for clearly Max-owned or explicitly cross-project context artifacts, archives them under a timestamped `.max-prompter/archive/` directory, and creates `.max-prompter/CLEAN_CONTEXT.md` for the active workspace.

It deliberately does **not** delete ordinary project files, erase the current chat, or claim to remove provider-side/model memory. It is a workspace-context isolation tool, not a platform conversation-history eraser.

### What stays active

After the reset, Max continues to use:

- the current conversation;
- the current project repository;
- the current project's own `README`, rules, specs, and documentation;
- newly created context during the current project.

Old unrelated project context is not considered active unless the user explicitly restores it.

# Workspace skill installation

## `/skillinstall`

`/skillinstall` gives Max Prompter a dedicated, workspace-only way to add third-party Agent Skills without scattering them throughout the project.

### With a repository

```text
/skillinstall frontend-ui/https://github.com/author/repository.git
```

### With only a skill name

```text
/skillinstall frontend-ui
```

Without a URL, Max searches for the skill and prefers an authoritative/original repository. When multiple plausible repositories exist and the correct source cannot be determined safely, it asks for clarification instead of silently installing an arbitrary fork.

### Installation layout

The canonical installed copy is always:

```text
skills/
└── frontend-ui/
    └── SKILL.md
```

For Antigravity workspace discovery, Max also creates a small wrapper at:

```text
.agents/
└── skills/
    └── frontend-ui/
        └── SKILL.md
```

The wrapper points the agent back to the canonical `skills/frontend-ui/` installation. This keeps the workspace's third-party skills organized in one visible `skills/` directory while remaining compatible with Antigravity's native `.agents/skills/` discovery model.

### Safety model

Skills are instructions for an AI agent, so `/skillinstall` treats third-party sources as untrusted. It validates the requested `SKILL.md`, preserves provenance, and does not execute arbitrary setup scripts, hooks, or MCP servers just to install Markdown instructions. It also never asks the user to expose secrets merely to install a skill.

### Update behavior

When a skill with the same name already exists, Max does not silently overwrite user modifications. It inspects the existing copy and either performs an explicitly requested controlled update or asks the user to choose how to reconcile the versions.


# Reverse engineering

Max Prompter includes `/re` as a general reverse-engineering entry point. It is **not limited to crackmes or `.exe` files**. Use it for authorized analysis of software you own, are developing, are researching, or have explicit permission to inspect.

The normal backend is **IDA Pro**. You can explicitly choose **x64dbg** or **GDB** when you want a different debugger.

## Command forms

```text
/re <program>
/re <path>
/re ida <program>
/re x64dbg <program>
/re gdb <program>
/re gdp <program>
```

`/re gdp` is supported as an alias for `/re gdb`.

Examples:

```text
/re myapp.exe
/re mylibrary.dll
/re C:\work\samples\sample.exe
/re x64dbg myapp.exe
/re gdb ./server
/re gdp ./server
```

### Active programs

You can also use `/re` to look at programs that are already running:

```text
/re
/re x64dbg
/re gdb
/re gdp
```

Max scans the active process list and shows useful fields such as:

- PID;
- process name;
- executable path when Windows allows it to be read;
- architecture when it can be detected;
- access/path limitations.

It does **not** depend on PowerShell or WMI for the Windows process scan. The bundled resolver uses Windows process APIs, which makes the feature more useful on systems where PowerShell/WMI is unavailable or unhealthy.

If several processes match, Max does not guess. You select the correct PID first.

## Choosing the debugger

**IDA Pro is the default.** You do not need to type `ida` unless you want to make the choice explicit.

```text
/re myapp.exe
```

uses IDA.

```text
/re x64dbg myapp.exe
```

uses x64dbg.

```text
/re gdb myapp.exe
```

or

```text
/re gdp myapp.exe
```

uses GDB.

For a running process, the backend can attach using its documented process/PID flow. x64dbg supports `-p PID`; GDB supports `-p PID`; IDA supports its documented Attach to process workflow. citeturn825372search0turn529691search1turn568286search1

## What happens after `/re`

```text
/re request
   ↓
resolve file or scan processes
   ↓
show candidates if ambiguous
   ↓
fingerprint the selected file when available
   ↓
choose the debugger
   ↓
launch / attach
   ↓
verify the debugger process started
   ↓
save the RE session
   ↓
wait for the analysis request
```

The session is stored in:

```text
.max-prompter/re/
├── RE_SESSION.json
├── RE_SESSION.md
├── scripts/
└── output/
```

The session records the backend, target/PID, file hash when available, architecture hint, debugger path, and launch/attach state.

## Follow-up analysis

After opening a session, the next natural-language message becomes the analysis request.

Example:

```text
/re myapp.exe
```

Then:

```text
Find the configuration parser and explain its control flow.
```

Max should use the active session instead of making you repeat the target.

Common analysis tasks include:

- find entry points;
- inspect imports and exports;
- search strings;
- follow references/xrefs;
- identify parsers and validators;
- inspect callers and callees;
- trace data flow;
- reconstruct relevant structures/types;
- explain control flow;
- inspect runtime behavior when debugging is requested.

## IDA automation

IDA supports graphical launch with `ida`/`ida64` and script-driven batch workflows using documented command-line switches. Max can generate project-local IDAPython scripts for repeatable static-analysis tasks. citeturn825372search21turn811308search10

The helper is:

```text
scripts/re/run_analysis.py
```

For a one-shot script, Max can run an appropriate `-A -S<script>` invocation against a file/database. Version-sensitive IDA APIs should be checked against the installed IDA documentation before use.

For active processes, IDA's documented GUI route is **Debugger → Attach to process**. IDAPython also exposes process enumeration and `attach_process(pid)`. citeturn568286search1turn811308search1

## x64dbg workflow

x64dbg is useful when you want Windows-focused interactive debugging.

For a file:

```text
/re x64dbg myapp.exe
```

For a running PID, the bundled launcher uses the documented:

```text
x64dbg.exe -p <PID>
```

x64dbg also documents its `AttachDebugger/attach` command and its requirement that debugger architecture match the debuggee. The launcher prefers `x32dbg.exe` for x86 targets when appropriate and available. citeturn825372search0turn825372search2turn806379search12

Max may generate x64dbg commands/scripts for the active session, but it does not claim to have remotely injected arbitrary commands into x64dbg unless an actual x64dbg bridge/plugin is installed.

## GDB workflow

GDB is useful for targets supported by the installed GDB build.

```text
/re gdb ./program
```

or:

```text
/re gdp ./program
```

GDB can attach to a running PID with `-p`, and it can run command files with `-x`. citeturn529691search1turn169974search0

For repeatable commands, Max can create:

```text
.max-prompter/re/scripts/analysis.gdb
```

and run it through GDB's documented command-file interface.

## Finding the debuggers

The bundled launcher tries explicit paths, environment variables, `PATH`, and reasonable common installation locations.

For IDA it understands:

```text
HCLI_CURRENT_IDA_INSTALL_DIR
IDADIR
IDA_PATH
```

For x64dbg it understands:

```text
X64DBG_DIR
X64DBG_PATH
```

For GDB it understands:

```text
GDB_PATH
GDB
```

You can also pass an explicit debugger path to the helper scripts.

## Failure handling

`/re` should clearly distinguish:

```text
target not found
multiple targets found
process not found
process path unavailable
unknown file format
unsupported architecture
debugger not found
launch failed
debugger exited immediately
attach failed
decompiler unavailable
analysis incomplete
evidence insufficient
complete
```

The workflow never treats `Popen()` returning as proof that a debugger stayed open. The launcher briefly checks whether the child exits immediately and records the observation in the session file.

## Safety and scope

Only analyze software the user is authorized to inspect.

The basic process scan intentionally does not collect passwords, environment variables, browser data, command histories, or arbitrary process memory. A user request to inspect sensitive runtime data should be handled separately and only when it is clearly part of an authorized debugging/research task.

For unknown or potentially unsafe samples, static analysis is preferred and an isolated analysis environment should be used before execution.

## Quick examples

### Default IDA

```text
/re mygame.exe
```

### x64dbg

```text
/re x64dbg mygame.exe
```

### GDB

```text
/re gdb myserver
```

### GDB alias

```text
/re gdp myserver
```

### Active process scan

```text
/re
```

### Active process + x64dbg

```text
/re x64dbg
```

Max lists matching active programs, asks you to select the correct process when needed, and then starts the selected debugger.

---

# Installation

Max Prompter is packaged as an Antigravity plugin.

## Global plugin installation

Current Antigravity documentation places manually installed global plugins under:

```text
~/.gemini/config/plugins/
```

On Windows, that normally resolves to:

```text
C:\Users\<USERNAME>\.gemini\config\plugins\
```

The expected structure is:

```text
C:\Users\<USERNAME>\.gemini\config\plugins\max-prompter-antigravity\
├── plugin.json
├── skills\
│   ├── max-prompter\
│   ├── prompt\
│   ├── constraints\
│   ├── council\
│   ├── spec\
│   ├── plan\
│   ├── build\
│   ├── design\
│   ├── audit\
│   ├── review\
│   ├── test\
│   └── ship\
└── references\
```

Official Antigravity plugin documentation:

https://www.antigravity.google/docs/plugins

### PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME\.gemini\config\plugins" | Out-Null
```

Then clone the repository into that directory after publication:

```powershell
git clone https://github.com/Tofu4K/max-the-prompter.git "$HOME\.gemini\config\plugins\max-prompter-antigravity"
```

Restart Antigravity after installation or an update.

## Workspace plugin installation

For a single project:

```text
<project-root>/.agents/plugins/max-prompter-antigravity/
```

This keeps the plugin scoped to that workspace.

## Standalone skill installation

Antigravity also supports standalone skills under:

```text
<project-root>/.agents/skills/<skill-folder>/
```

or globally under:

```text
~/.gemini/antigravity/skills/<skill-folder>/
```

This repository is intentionally packaged as a plugin because it contains multiple related skills. You do not need to flatten it into standalone skill directories unless you specifically want to use that installation mode.

## Verify the pack before installing

The repository includes a dependency-free validator:

```powershell
python scripts/validate_pack.py
```

Expected result:

```text
PASS: 15 skills validated; plugin manifest is valid.
```

Then restart Antigravity and type `/` to inspect the loaded skills.

---

# Repository structure

```text
max-prompter-antigravity/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── config.yml
│   │   └── feature_request.yml
│   ├── pull_request_template.md
│   └── workflows/
│       └── validate.yml
├── docs/
│   ├── COMMANDS.md
│   ├── MAINTAINER_GUIDE.md
│   └── RELEASE_CHECKLIST.md
├── references/
│   ├── integrations.md
│   └── reverse-engineering.md
├── scripts/
│   ├── re/
│   │   ├── launch_ida.py
│   │   └── resolve_target.py
│   └── validate_pack.py
├── skills/
│   ├── audit/SKILL.md
│   ├── build/SKILL.md
│   ├── constraints/SKILL.md
│   ├── council/SKILL.md
│   ├── design/SKILL.md
│   ├── max-prompter/SKILL.md
│   ├── plan/SKILL.md
│   ├── prompt/SKILL.md
│   ├── review/SKILL.md
│   ├── ship/SKILL.md
│   ├── spec/SKILL.md
│   └── test/SKILL.md
├── .editorconfig
├── .gitattributes
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── plugin.json
├── README.md
└── SECURITY.md
```

The plugin manifest is intentionally minimal: a plugin root needs `plugin.json`, while skills are placed beneath `skills/<skill-name>/SKILL.md`. See the current Antigravity documentation for the full supported plugin surface.

---

# Development

## Validate

```powershell
python scripts/validate_pack.py
```

The validator checks:

- `plugin.json` exists;
- `plugin.json` is valid JSON;
- a description and name exist;
- the `skills/` directory exists;
- every skill has `SKILL.md`;
- frontmatter exists;
- `name` and `description` exist;
- skill names match directory names;
- names follow lowercase-hyphenated conventions;
- skill names are unique.

## Edit a skill

Each skill lives in:

```text
skills/<skill-name>/SKILL.md
```

The frontmatter should look like:

```yaml
---
name: example-skill
description: Guides an agent through a specific workflow and explains when to use it.
---
```

Keep the description specific enough for the agent's relevance detection.

## Add a new command

1. Create `skills/<command>/`.
2. Add `SKILL.md`.
3. Add YAML frontmatter.
4. Define clear trigger and non-trigger conditions.
5. Define a concrete workflow.
6. Add verification/exit criteria.
7. Document the command in `docs/COMMANDS.md`.
8. Document it in the README command list.
9. Run the validator.
10. Update the changelog.

## Integration updates

When an external tool changes:

1. Check the primary documentation.
2. Update only the routing guidance that is actually affected.
3. Do not copy the external repository into this project.
4. State fallback behavior.
5. Validate the repository.
6. Record the change in the changelog.

---

# GitHub publication

The repository is structured to be published directly to GitHub.

## Before the first push

Run:

```powershell
python scripts/validate_pack.py
```

Then inspect:

```text
plugin.json
README.md
skills/
references/
docs/
.github/
LICENSE
SECURITY.md
CONTRIBUTING.md
CHANGELOG.md
```

Make sure no local machine data, credentials, tokens, generated council artifacts, or private project files are present.

## Initialize Git

From the repository root:

```powershell
git init
git add .
git commit -m "feat: initial Max Prompter Antigravity skill pack"
git branch -M main
```

Add the GitHub remote:

```powershell
git remote add origin https://github.com/Tofu4K/max-the-prompter.git
```

Push:

```powershell
git push -u origin main
```

## Recommended repository settings

After creating the repository, configure:

- a clear repository description;
- topics such as `antigravity`, `agent-skills`, `prompt-engineering`, `ai-coding-agent`, and `developer-tools`;
- Issues;
- Discussions if desired;
- the security contact mechanism;
- branch protection if the repository becomes collaborative;
- GitHub Actions;
- release tags and release notes.

## README badge

Once the repository URL is final, replace:

```text
Tofu4K/max-the-prompter
```

in the badge links at the top of this README.

## First release

The repository currently starts with a `0.1.0` changelog entry. Before tagging a release, run the checklist at:

[`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md)

A first release can then be tagged with:

```powershell
git tag v0.1.0
git push origin v0.1.0
```

---

# GitHub Actions

The repository includes:

```text
.github/workflows/validate.yml
```

The workflow runs the same dependency-free validator on pushes and pull requests.

That means a broken skill directory or malformed manifest can be caught before merging.

---

# Contribution rules

Read [`CONTRIBUTING.md`](CONTRIBUTING.md).

The most important contribution principle is:

> Add useful reasoning, not decorative verbosity.

A new section should ideally add a:

- decision;
- constraint;
- verification rule;
- edge case;
- security rule;
- implementation pattern;
- integration;
- source;
- acceptance criterion;
- recovery strategy.

Do not add hundreds of lines merely to make the skill look larger.

---

# Security

Read [`SECURITY.md`](SECURITY.md).

Max Prompter intentionally tells agents to:

- respect workspace boundaries;
- avoid exposing secrets;
- verify destructive operations;
- prefer least privilege;
- preserve user data where applicable;
- distinguish verified facts from assumptions;
- never claim success without evidence.

When a project has security-sensitive behavior, Max Prompter should explicitly route toward security-focused workflows when they are installed.

---

# License

Max Prompter is released under the [MIT License](LICENSE).

---

# Acknowledgements

Max Prompter is an independent orchestration project inspired by open agent-skill conventions and the following ecosystems/workflows:

- Addy Osmani's `agent-skills` engineering workflows: https://github.com/addyosmani/agent-skills
- the Council-of-5 methodology supplied for this project;
- Impeccable: https://impeccable.style/docs/
- Motion: https://motion.dev/docs/react
- KokonutUI: https://kokonutui.com/docs
- Bklit UI: https://bklit.com/docs/skills

This project intentionally links to upstream work instead of copying entire third-party skill repositories. Upstream projects retain their own licenses, trademarks, and documentation.

---

# Maintainer philosophy

Max Prompter should become **more reliable as it grows, not merely longer**.

The maintainers should prefer:

```text
specificity
    > repetition

repository truth
    > generic assumptions

current documentation
    > stale memory

specialist skills
    > duplicated workflows

verification
    > confidence

testable constraints
    > vague quality claims

appropriate tooling
    > tool collecting

clear acceptance criteria
    > “looks good”
```

The pack should remain universal. A new integration should only be promoted to the default routing system when it provides meaningful value across a reasonable class of projects.

---

# One-line description

**Max Prompter turns “build this” into a detailed, constrained, verifiable execution plan that an autonomous coding agent can actually follow.**
