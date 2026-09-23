---
name: cleanmemory
description: Reset Max Prompter's project-context memory boundary so unrelated projects and prior-project notes do not influence the current workspace. Preserve the current chat and current project files. Use when the user wants to start clean or remove cross-project context.
---

# /cleanmemory — CROSS-PROJECT CONTEXT RESET

## Mission

Run a safe context-isolation reset for Max Prompter.

The purpose is to prevent memories, notes, council transcripts, prompts, or cached context from unrelated projects from influencing work in the current project.

This command operates on **Max Prompter's local project-context artifacts and the agent's instructions for the current session**. It does **not** claim to delete model-provider conversation history or hidden platform memory, and it must not attempt to modify the current chat.

## Safety rule

Never delete, rewrite, or move ordinary project source files merely because they look like memory.

Do not touch:

- source code
- assets
- user documents
- databases
- configuration needed by the application
- `.git` history
- the current conversation
- current project requirements/specs unless they are explicitly marked as Max Prompter cross-project context

## Procedure

### 1. Identify the current workspace

Determine the opened workspace root and treat it as the active project.

### 2. Discover Max Prompter context artifacts

Look only for clearly Max-owned or explicitly context-oriented locations, including where present:

```text
.max-prompter/
.max-prompter/memory/
.max-prompter/context/
.max-prompter/cache/
.max-prompter/council/
```

Also inspect obvious Max-generated files whose names explicitly indicate cross-project memory, such as:

```text
max-memory*
max-context*
cross-project-memory*
council-transcript-*
```

Do not broadly delete every file named `memory`, `context`, `notes`, or `history` because those names may belong to the project itself.

### 3. Preserve instead of hard-delete

When Max-owned context artifacts are found, create a timestamped archive directory such as:

```text
.max-prompter/archive/context-reset-YYYYMMDD-HHMMSS/
```

Move only the clearly Max-owned cross-project context artifacts into that archive.

If a safe ownership determination cannot be made, leave the file untouched and report it.

### 4. Establish a clean context boundary

Create or update:

```text
.max-prompter/CLEAN_CONTEXT.md
```

The file must state that the current project is the sole active project context for this session and that unrelated historical project context must not be used unless the user explicitly reintroduces it.

### 5. Continue from the current project

After the reset:

- read the current project's own instructions normally;
- use the current conversation normally;
- use current workspace files normally;
- ignore archived cross-project context unless the user explicitly asks to restore it.

## Required user-facing result

Report:

1. that the cross-project Max context boundary was reset;
2. what Max-owned context was archived, if any;
3. that the current chat and current project files were preserved;
4. that platform/model conversation history was not deleted by this command.

Do not imply that this command can erase hidden model memory or provider-side conversation history.

## Idempotency

Running `/cleanmemory` twice without generating new cross-project context should be safe and should produce little or no additional change.
