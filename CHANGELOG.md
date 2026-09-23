# Changelog

All notable changes to Max Prompter are documented here.

## [0.3.0] - 2026-09-23

### Added

- Expanded `/re` into a general debugger-agnostic reverse-engineering workflow.
- Added explicit backend selection for `ida`, `x64dbg`, `gdb`, and the `gdp` alias.
- Added native Windows active-process scanning without requiring PowerShell or WMI.
- Added PID-aware session records and debugger launch/attach state tracking.
- Added x64dbg/x32dbg discovery and architecture-aware debugger selection.
- Added GDB command-file/batch analysis support through `scripts/re/run_analysis.py`.

### Changed

- Reworked `/re` target resolution so a program name can resolve against both local files and active processes.
- Improved debugger discovery, launch verification, and explicit failure states.
- Removed generated `__pycache__` files from the release package.

## [0.2.1] - 2026-09-23

### Changed

- Expanded `/re` documentation and routing from crackme-focused examples to general authorized software reverse engineering.
- Added examples for executables, shared libraries, and other IDA-supported inputs.
- Clarified that the exact set of analyzable formats depends on the installed IDA edition and version.

## [0.2.0] - 2026-09-23

### Added

- Added the `/re` reverse-engineering skill for authorized local binaries and CTF/crackme workflows.
- Added local target resolution and SHA-256 fingerprinting helpers.
- Added IDA Pro launcher/session helpers with environment-variable and PATH detection.
- Added persistent RE session metadata under `.max-prompter/re/`.
- Updated command documentation, repository structure, and validation for 15 skills.

## [0.1.0] - 2026-09-17

### Added

- Universal `max-prompter` orchestration skill.
- `/prompt`, `/constraints`, `/council`, `/spec`, `/plan`, `/build`, `/design`, `/audit`, `/review`, `/test`, and `/ship` skills.
- Integrated Council-of-5 workflow based on the supplied Ole Lehmann `llm-council` methodology.
- Routing guidance for Addy Osmani's `agent-skills` ecosystem.
- UI/design routing for Impeccable, Motion, KokonutUI, and Bklit UI when appropriate.
- Source-driven verification rules for changing third-party tools and APIs.
- GitHub-ready repository documentation, contribution files, security policy, CI validation, and repository checks.
