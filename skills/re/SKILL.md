---
name: re
description: General reverse-engineering and debugging workflow for authorized software. Use with /re <program or path> for the default IDA Pro workflow, /re x64dbg [program or PID] for x64dbg, or /re gdb [program or PID] and /re gdp [program or PID] for GDB. Can scan active processes, resolve files, fingerprint targets, launch the selected tool, persist sessions, generate evidence-backed analysis tasks, and resume follow-up queries without losing the target context.
---

# /re — REVERSE ENGINEERING

## Purpose

`/re` is a universal reverse-engineering entry point. It is not limited to crackmes or `.exe` files. It can work with executables, DLLs/shared libraries, binaries, firmware images, dumps, and other files supported by the selected analysis tool and installed tooling.

The default backend is **IDA Pro**. Two alternate debugger backends are built in:

- `x64dbg` for Windows user-mode debugging.
- `gdb` for targets supported by the installed GDB build.

`gdp` is accepted as an alias for `gdb` because the command form is part of Max Prompter's public command set.

Use `/re` only for software the user owns, has permission to inspect, or is explicitly authorized to analyze. The workflow should favor static analysis first, avoid executing unknown files merely because they were named, and clearly distinguish observations from assumptions.

## Command syntax

### Default IDA Pro

```text
/re <program name>
/re <absolute or relative path>
```

Examples:

```text
/re myapp.exe
/re mylibrary.dll
/re .\samples\program.exe
/re C:\work\samples\firmware.bin
```

### Explicit debugger/backend

```text
/re ida <program or path>
/re x64dbg <program or path>
/re gdb <program or path>
/re gdp <program or path>
```

Examples:

```text
/re x64dbg myapp.exe
/re gdb ./server
/re gdp ./server
/re x64dbg C:\work\sample.dll
```

### Active-process mode

When no target is supplied, or when the named target is not found as a file, scan currently running processes and show matching candidates.

```text
/re
/re x64dbg
/re gdb
/re gdp
```

A user may also explicitly target a PID when invoking the helper scripts:

```text
python scripts/re/resolve_target.py --pid 1234
python scripts/re/launch_debugger.py --tool x64dbg --pid 1234
```

Do not silently select one process when multiple candidates match. Show PID, process name, path when accessible, architecture when known, and access limitations, then let the user choose.

### Resume the active session

```text
/re
```

If `.max-prompter/re/RE_SESSION.json` exists and the user did not provide a new backend or target, treat the session as the current RE context.

## What `/re` does

The high-level workflow is:

```text
/re request
      ↓
parse backend + target intent
      ↓
resolve local file OR scan active processes
      ↓
fingerprint target when a file is available
      ↓
resolve selected debugger
      ↓
launch/attach where supported
      ↓
persist RE session
      ↓
ask for / process the natural-language analysis query
      ↓
produce evidence-backed findings
```

Every stage must have an explicit success/failure state. Never say a debugger was launched when the launcher process immediately exited.

## Backend rules

### IDA Pro — default

Prefer IDA Pro for static analysis, disassembly, cross-references, graph views, type reconstruction, and decompilation when Hex-Rays is installed.

For a local file:

```text
ida64.exe target.exe
```

or the 32-bit equivalent when appropriate. Current Hex-Rays documentation supports graphical launch with `ida input-file` / `ida64 input-file`; batch automation can use `-A` together with `-S` scripts. citeturn825372search21

For a running process, IDA's documented GUI workflow is **Debugger → Attach to process**. IDA's API also exposes `ida_dbg.attach_process(pid)` and process enumeration; the exact debugger module can be version-dependent, so automatic attach should be treated as best-effort and fall back to the documented GUI attach flow if the installed debugger backend cannot be loaded. citeturn568286search1turn811308search1

### x64dbg

Use x64dbg when the user explicitly selects it or when it is otherwise the appropriate Windows debugger.

For a file, the documented command-line form is:

```text
x64dbg.exe target.exe
```

For a running PID:

```text
x64dbg.exe -p 1234
```

The x64dbg documentation explicitly supports both forms. x64dbg also exposes an `AttachDebugger` command inside the debugger for attaching to a running PID. citeturn825372search0turn825372search2

For 32-bit Windows targets, prefer `x32dbg.exe` where required. x64dbg documents that the debugged executable must match the debugger architecture. citeturn825372search10

Do not claim that Max has injected arbitrary commands into x64dbg unless a real x64dbg command/script bridge is available. Max may create a documented x64dbg script or command sequence for the user to load/run in the active debugger.

### GDB

Use the installed GDB build when explicitly selected:

```text
gdb target
```

For a running process:

```text
gdb -p 1234
```

GDB documents both executable selection and PID attachment, subject to the capabilities and permissions of the specific GDB/OS build. citeturn529691search1turn529691search0

GDB also supports command files with `-x` and batch execution with `-batch`, which Max can use for repeatable analysis commands. citeturn169974search0turn169974search4

## Target resolution

Use:

```text
python scripts/re/resolve_target.py --name "<query>"
```

The resolver searches in this order:

1. Explicit path supplied by the user.
2. Workspace-relative path.
3. Exact filename matches in the workspace.
4. A command found on `PATH`.
5. Active processes whose executable name/path matches the query.
6. Active processes with a partial name match when exact matching found nothing.

Never download a missing program automatically.

When more than one file or process matches, show the candidates and require a selection. The helper returns a non-zero exit code for ambiguous/no-match states so the agent does not mistake them for success.

## Active-process scanning

The scan must be Windows-friendly and must not depend on PowerShell or WMI being healthy.

On Windows, the bundled resolver uses the native Tool Help process APIs and attempts to read executable paths using `QueryFullProcessImageNameW`. If a process denies path access, the result still includes its PID/name and marks the path as unavailable.

The scan includes:

- PID;
- process name;
- executable path when readable;
- architecture when detectable;
- access/path-readability status.

Use:

```text
python scripts/re/resolve_target.py --list-processes
```

or filter:

```text
python scripts/re/resolve_target.py --process-query "myapp"
```

Do not expose command-line arguments, environment variables, credentials, window titles, or unrelated process memory as part of the basic scan. Those are outside the scope of process discovery.

## Fingerprinting

For a file target, record:

- absolute path;
- filename;
- size;
- SHA-256;
- file format when recognizable;
- architecture when recognizable;
- selected backend;
- selected debugger executable;
- session timestamp.

For a running-process target, record:

- PID;
- process name;
- executable path when readable;
- architecture when detectable;
- selected backend;
- debugger executable;
- attach/launch observation.

Store the machine-readable record at:

```text
.max-prompter/re/RE_SESSION.json
```

and a human-readable summary at:

```text
.max-prompter/re/RE_SESSION.md
```

Do not store secrets or unrelated chat content in these files.

## Debugger discovery

The launcher is:

```text
python scripts/re/launch_debugger.py --tool <ida|x64dbg|x32dbg|gdb> ...
```

### IDA discovery

Try, in order:

1. explicit `--debugger` path;
2. `HCLI_CURRENT_IDA_INSTALL_DIR`;
3. `IDADIR`;
4. `IDA_PATH`;
5. executable on `PATH`;
6. common install locations.

Prefer `ida64` for 64-bit/ARM64 targets when available.

### x64dbg discovery

Try, in order:

1. explicit `--debugger` path;
2. `X64DBG_DIR`;
3. `X64DBG_PATH`;
4. `x64dbg.exe` / `x32dbg.exe` on `PATH`;
5. common install locations.

For an x86 process, prefer `x32dbg.exe` where available.

### GDB discovery

Try, in order:

1. explicit `--debugger` path;
2. `GDB_PATH`;
3. `GDB`;
4. `gdb.exe` / `gdb` on `PATH`.

Do not assume a particular Windows GDB distribution.

## Launch verification

After starting a debugger, wait briefly and inspect the child process.

Possible outcomes are:

```text
running
exited:<code>
launch-failed
```

If the debugger process exits immediately, mark the session as failed and show the actual recovery path.

Do not equate `Popen()` returning successfully with “debugger is running”.

## Natural-language analysis workflow

After the debugger is ready, the user's next message is treated as the analysis query.

Example:

```text
User: /re myapp.exe
Max: Target resolved and IDA opened. Send the analysis goal.
User: Find the function that validates the configuration file and explain the control flow.
Max: Continue the active RE session for myapp.exe.
```

The agent should translate the query into concrete analysis tasks, then use the selected tool.

### Typical static-analysis tasks

- identify entry point;
- enumerate functions;
- inspect imports and exports;
- search strings;
- follow string/data/code references;
- identify likely parsers and validators;
- inspect callers/callees;
- trace a data flow;
- reconstruct relevant structures/types;
- compare multiple paths;
- identify initialization and teardown;
- inspect exception/error paths;
- explain control flow.

### Decompilation

When Hex-Rays is installed, use decompilation for relevant functions. Treat the result as reconstructed C-like pseudocode, not the original source code.

Do not claim exact source reconstruction unless actual source files/symbols are available.

## Automation bridge

The Max skill can create project-local analysis scripts and invoke documented batch interfaces when supported.

### IDA

For repeatable one-shot analysis, generate an IDAPython script under:

```text
.max-prompter/re/scripts/
```

and run the installed IDA with an appropriate `-A -S<script>` invocation. Check the installed version's documentation whenever an API is version-sensitive. Hex-Rays documents IDAPython debugger, database, and analysis APIs. citeturn811308search1turn811308search10

### GDB

For repeatable commands, write a GDB command file under:

```text
.max-prompter/re/scripts/
```

and use:

```text
gdb -batch -x <commands-file> <target>
```

or the appropriate `-p PID` attach form. GDB documents `-x`/`--command` and `-batch`. citeturn169974search0turn169974search6

### x64dbg

Generate a compatible x64dbg command/script artifact when useful, but do not invent an unsupported command-line injection mechanism. x64dbg documents command/script execution inside the debugger itself. citeturn806379search2turn806379search3

## Dynamic analysis

Dynamic analysis is optional and should only happen when requested or clearly necessary.

For active-process debugging:

1. Confirm the selected PID.
2. Record the process path/architecture when available.
3. Use the selected debugger's documented attach path.
4. Make observations from actual debugger output.
5. Detach rather than terminate when the user's goal is observation and the debugger supports it.

GDB documents `detach` as releasing the process and allowing it to continue. x64dbg also documents an explicit detach action. citeturn529691search0turn825372search20

For untrusted samples, recommend an isolated analysis environment. Never execute an unknown file simply because the user asked to inspect it.

## Evidence rules

Every significant finding should be backed by observable evidence when possible:

- function name/address;
- xref;
- string/reference;
- API/import;
- instruction sequence;
- pseudocode;
- breakpoint/trace observation;
- process/module information.

If the evidence is incomplete, state the uncertainty instead of filling the gap with a guess.

## Session integrity

Before every follow-up query:

1. Read `.max-prompter/re/RE_SESSION.json`.
2. Verify the recorded backend.
3. Verify the recorded target/ PID.
4. If a file target is still present, compare its SHA-256 before assuming it is unchanged.
5. If a process target disappeared, report that it exited.
6. Never silently switch to another process or file.

If a target hash changed, treat it as a new sample and refresh the session.

## Failure handling

Use explicit states:

- `target_not_found`;
- `target_ambiguous`;
- `process_not_found`;
- `process_access_limited`;
- `format_unknown`;
- `debugger_not_found`;
- `launch_failed`;
- `debugger_exited`;
- `attach_failed`;
- `analysis_pending`;
- `decompiler_unavailable`;
- `evidence_insufficient`;
- `complete`.

Never hide a failure behind a success message.

## Output format

For ordinary queries:

```text
## Finding

## Evidence

## Relevant Functions / Modules

## Control or Data Flow

## Decompiled / Disassembled Excerpt

## Uncertainty
```

For an active-process session, also include:

```text
## Process

## PID

## Backend

## Attach Status
```

Do not dump large amounts of raw debugger output when a concise evidence-backed summary is sufficient.

## Integration with Max Prompter

When `/re` is active, use the main Max Prompter skill for orchestration, prompt expansion, constraints, verification, testing, and documentation.

Use installed specialist skills when relevant, especially:

- debugging;
- security analysis;
- testing;
- source-driven development;
- code review;
- performance.

Do not duplicate another installed skill's workflow when the specialist skill already provides it.

## Quick reference

```text
/re app.exe              # default IDA Pro
/re app.dll              # default IDA Pro
/re                        # resume session or scan active processes
/re ida app.exe          # explicit IDA Pro
/re x64dbg app.exe       # x64dbg
/re x64dbg               # choose from active processes / then attach with x64dbg
/re gdb app              # GDB
/re gdb                  # choose from active processes / then attach with GDB
/re gdp app              # GDB alias
/re gdp                  # GDB alias + active-process mode
```

Default rule:

> **Use IDA Pro unless the user explicitly chooses another backend.**
