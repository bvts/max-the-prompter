# Max Prompter Command Reference

All commands in this repository are implemented as Antigravity skills. In Antigravity, type `/` and select a loaded skill by name when it is available. The exact visibility of a command depends on whether the plugin is loaded and whether another skill uses the same name.

## Command matrix

| Command | Primary job | Use it when | Main output |
|---|---|---|---|
| `/max-prompter` | Full orchestration | You want Max to decide the appropriate workflow and depth | Detailed prompt, routing, constraints, verification plan |
| `/prompt` | Prompt generation | You primarily need a high-detail implementation prompt | Execution-ready implementation prompt |
| `/constraints` | Quality bar | You need explicit project invariants and standards | `CONSTRAINTS.md` and quality rules |
| `/council` | Decision pressure test | There are multiple credible options and meaningful stakes | Council analysis/synthesis |
| `/spec` | Requirements contract | The build needs a formal definition before code | Specification artifact |
| `/plan` | Execution planning | Requirements are known and need to become tasks | Dependency-ordered plan |
| `/build` | Implementation | The project is ready to be changed | Code changes plus verification |
| `/design` | Visual/UX work | The project has a UI or visual system | Design direction and implementation plan |
| `/audit` | Broad inspection | You want to discover what may still be wrong | Findings with evidence and severity |
| `/review` | Adversarial review | A change is ready for pre-merge/pre-release review | Review findings and disposition |
| `/test` | Proof | You need to establish that behavior is correct | Tests, results, and remaining gaps |
| `/ship` | Production gate | The project is ready to release/deploy/package | Release readiness and handoff |
| `/cleanmemory` | Cross-project context reset | Unrelated project memory/context may interfere | Clean context boundary + archive |
| `/skillinstall` | Workspace skill installer | You want to add a skill to this project | `skills/<name>/` + discovery wrapper |
| `/re` | Reverse engineering | You want to inspect authorized local software with IDA Pro, x64dbg, or GDB | RE session metadata + selected debugger session |

## `/max-prompter`

Use when you have a rough project idea, a complex feature request, or a request that could benefit from full orchestration.

Example:

```text
/max-prompter
Build a local-first desktop application that indexes a large file collection and lets users search, preview, tag, and safely export files.
```

Expected behavior:

1. Inspect the workspace.
2. Classify the project.
3. Discover relevant installed skills.
4. Identify unknowns and meaningful decisions.
5. Decide whether Council is warranted.
6. Select the appropriate specialist workflows.
7. Produce the correct prompt depth.
8. Establish constraints and verification.
9. Finish with acceptance criteria and a definition of done.

## `/prompt`

Use when the desired deliverable is the prompt itself.

Example:

```text
/prompt
Build a production-ready marketplace for downloadable digital assets.
```

The command should produce more than a paraphrase. It should expose architecture, implementation decisions, file/module boundaries, flows, edge cases, failure modes, tests, and acceptance criteria.

## `/constraints`

Use when the project needs a durable quality contract.

Example:

```text
/constraints
Set a production-grade bar. Never overwrite user files silently and require verification for every destructive filesystem operation.
```

The skill may create or update:

```text
CONSTRAINTS.md
```

A constraint should be testable whenever practical.

## `/council`

Use only for a genuine decision with uncertainty, competing options, or meaningful consequences.

Example:

```text
/council
Should this application use a local SQLite database or a remote Postgres service?
```

The workflow is:

```text
Context enrichment
      ↓
Decision framing
      ↓
5 independent advisors
      ↓
Anonymous peer review
      ↓
Chairman synthesis
```

Advisors:

- Contrarian
- First Principles Thinker
- Expansionist
- Outsider
- Executor

The Council should not be used for ordinary factual lookups or trivial implementation choices.

## `/spec`

Use when requirements need to become an implementation contract.

A strong spec covers:

- goals and non-goals;
- users and use cases;
- functional requirements;
- system behavior;
- architecture;
- data model;
- interfaces;
- security;
- performance;
- accessibility;
- errors and recovery;
- testing;
- acceptance criteria;
- edge cases;
- release considerations.

## `/plan`

Use after the problem is understood and the implementation needs sequencing.

The plan should contain:

- atomic tasks;
- dependencies;
- affected files/modules;
- prerequisites;
- verification for each meaningful step;
- integration points;
- rollback/recovery notes;
- completion criteria.

## `/build`

Use for actual implementation.

Preferred loop:

```text
inspect → implement → verify → inspect results → fix → continue → integrate → verify
```

The agent should use relevant installed specialist skills instead of duplicating them.

## `/design`

Use for UI/UX work.

The workflow should establish a coherent system rather than a collection of isolated pretty screens:

- information hierarchy;
- layout system;
- spacing;
- typography;
- color roles;
- component rules;
- interaction states;
- responsive behavior;
- motion principles;
- accessibility;
- rendered verification.

Optional integrations include Impeccable, Motion, KokonutUI, Bklit UI, and project-native component libraries when each is appropriate.

## `/audit`

Use when you want to discover remaining weaknesses.

Possible dimensions:

- correctness;
- architecture;
- data integrity;
- filesystem safety;
- security;
- accessibility;
- performance;
- UI/UX;
- browser/runtime behavior;
- dependencies;
- deployment;
- observability.

Findings should contain evidence and a clear remediation path.

## `/review`

Use before merging or shipping.

The review should challenge:

- requirement coverage;
- regressions;
- architecture;
- security;
- maintainability;
- performance;
- tests;
- unnecessary complexity.

## `/test`

Use when you need proof.

Depending on the project, select from:

- unit tests;
- integration tests;
- component tests;
- contract/API tests;
- browser tests;
- end-to-end tests;
- regression tests;
- migration tests;
- smoke tests;
- static analysis;
- type checks;
- production builds.

The objective is sufficient evidence, not maximum test count.

## `/ship`

Use at the production boundary.

Check as applicable:

```text
source/diff
→ tests
→ production build
→ configuration
→ secrets
→ dependencies
→ migrations
→ security
→ observability
→ performance
→ deployment
→ smoke verification
→ rollback readiness
```

The command must not treat “it builds locally” as the entire release decision.

## `/cleanmemory`

Use when you want Max Prompter to stop carrying context from unrelated projects into the current workspace. It resets Max-owned project-context artifacts and establishes a clean context boundary without touching ordinary project source files. It does not delete provider-side conversation history or hidden model memory.

Example:

```text
/cleanmemory
```

The command archives clearly Max-owned cross-project context rather than hard-deleting it, then writes `.max-prompter/CLEAN_CONTEXT.md`.

## `/skillinstall`

Use to install a skill into the **current workspace only**.

With a repository:

```text
/skillinstall frontend-ui/https://github.com/author/repo.git
```

Without a repository:

```text
/skillinstall frontend-ui
```

When no source is provided, the skill searches for an authoritative repository before installing. The canonical location is:

```text
skills/frontend-ui/
```

The command also creates a small Antigravity discovery wrapper under:

```text
.agents/skills/frontend-ui/SKILL.md
```

This keeps the user-requested `skills/` folder organized while still connecting the installed skill to Antigravity's native workspace skill discovery path.

Third-party skills are inspected before installation. Arbitrary install scripts, hooks, MCP servers, and secret-access requests are not executed merely to install a Markdown skill.


## Suggested command chains

### Greenfield

```text
/prompt
  ↓
/constraints
  ↓
/spec
  ↓
/plan
  ↓
/design    ← when visual
  ↓
/build
  ↓
/test
  ↓
/review
  ↓
/ship
```

### Architecture decision

```text
/council
  ↓
/spec
  ↓
/plan
```

### Existing codebase

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

### UI refinement

```text
/design
  ↓
Impeccable workflow if installed
  ↓
/test
  ↓
/audit
```

The chain is a recommended pattern, not a requirement to run every command.


## `/re`

`/re` is the universal reverse-engineering entry point. **IDA Pro is the default backend.** It also supports explicit `x64dbg` and `gdb` backends. `gdp` is accepted as a GDB alias. The target can be a local file or an active process.

```text
/re myapp.exe
/re C:\work\sample.dll
/re x64dbg myapp.exe
/re gdb ./server
/re gdp ./server
```

When no target is supplied, `/re` can scan active programs:

```text
/re
/re x64dbg
/re gdb
/re gdp
```

The Windows process scanner uses native process APIs and reports PID, name, readable executable path, architecture when detectable, and access limitations. If multiple processes match, the user must choose; Max never guesses.

The resolver helper is:

```text
python scripts/re/resolve_target.py --list-processes
python scripts/re/resolve_target.py --process-query "myapp"
python scripts/re/resolve_target.py --pid 1234
```

The debugger launcher is:

```text
python scripts/re/launch_debugger.py --tool ida --target "C:\\work\\sample.exe"
python scripts/re/launch_debugger.py --tool x64dbg --target "C:\\work\\sample.exe"
python scripts/re/launch_debugger.py --tool gdb --target "./server"
python scripts/re/launch_debugger.py --tool x64dbg --pid 1234
python scripts/re/launch_debugger.py --tool gdb --pid 1234
```

For static batch automation, `scripts/re/run_analysis.py` supports IDA and GDB. GDB command files use documented `-x`; IDA uses documented script startup where supported. x64dbg is launched/attached through its documented CLI, while command/script execution is kept explicit rather than pretending Max has an undocumented remote command channel.

The active session is stored at:

```text
.max-prompter/re/RE_SESSION.json
.max-prompter/re/RE_SESSION.md
```

The next natural-language message is the analysis request. For example:

```text
/re x64dbg myapp.exe

Find the code path that handles the invalid configuration case and explain what happens after the failure.
```

Use `/re` only for software the user is authorized to analyze. Do not silently download unknown targets or claim a debugger/analysis step succeeded when it did not.
