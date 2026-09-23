# Reverse Engineering Integration

Max Prompter's `/re` workflow is a general, local-first software-analysis workflow. **IDA Pro is the default backend**, with explicit alternatives for **x64dbg** and **GDB**. The command is not limited to crackmes or `.exe` files.

Use `/re` only for software the user owns, develops, researches, or is otherwise authorized to inspect.

## Backend selection

```text
/re <target>              # IDA Pro by default
/re ida <target>          # explicit IDA Pro
/re x64dbg <target>       # x64dbg / x32dbg as appropriate
/re gdb <target>          # GDB
/re gdp <target>          # GDB alias
```

When no target is supplied, Max can scan active processes and ask the user to choose a PID:

```text
/re
/re x64dbg
/re gdb
/re gdp
```

## Active-process scanning

On Windows, the bundled resolver uses native Tool Help APIs and `QueryFullProcessImageNameW`. This avoids depending on PowerShell or WMI for the basic process list.

The process record contains:

- PID;
- process name;
- executable path when readable;
- architecture when detectable;
- path/access status.

The basic scan deliberately does not collect credentials, environment variables, command lines, or arbitrary process memory.

## Official references

### IDA / Hex-Rays

- Command-line switches: https://docs.hex-rays.com/9.1/user-guide/configuration/command-line-switches
- IDA process attach: https://docs.hex-rays.com/9.0/user-guide/debugger/debugger-tutorials/debugger_windows_local
- IDAPython debugger API: https://python.docs.hex-rays.com/namespaceida__dbg.html
- IDAPython API reference: https://python.docs.hex-rays.com/

### x64dbg

- Command line: https://help.x64dbg.com/en/latest/introduction/Commandline.html
- AttachDebugger: https://help.x64dbg.com/en/latest/commands/debug-control/AttachDebugger.html
- File / Attach workflow: https://help.x64dbg.com/en/latest/gui/menus/File.html
- Script commands: https://help.x64dbg.com/en/latest/commands/script/

### GDB

- Invoking GDB / file and PID selection: https://sourceware.org/gdb/current/onlinedocs/gdb/Invoking-GDB.html
- File options and `-x`: https://sourceware.org/gdb/current/onlinedocs/gdb.html/File-Options.html
- Running-process attach: https://sourceware.org/gdb/current/onlinedocs/gdb.html/Attach.html
- Command files: https://sourceware.org/gdb/current/onlinedocs/gdb.html/Command-Files.html

## Tool behavior

### IDA

For files, Max launches `ida`/`ida64` with the target. For active processes, IDA's documented GUI Attach to process workflow is the fallback when the installed debugger setup cannot perform an automatic attach. IDAPython provides `get_processes()` and `attach_process(pid)` for integrations that are compatible with the installed version.

### x64dbg

The documented CLI supports:

```text
x64dbg.exe target.exe
x64dbg.exe -p PID
```

For x86 targets, `x32dbg.exe` should be used rather than attaching a 64-bit debugger to a 32-bit target. Max detects the target architecture when it can and prefers the appropriate executable.

Max can prepare x64dbg scripts/commands, but it should not claim to have injected arbitrary commands into a running x64dbg instance unless a real bridge/plugin is installed.

### GDB

The documented CLI supports:

```text
gdb target

gdb -p PID
```

GDB command files can be executed with `-x`, and batch mode can be used for repeatable analysis.

## Session artifacts

Each `/re` session stores:

```text
.max-prompter/re/
├── RE_SESSION.json
├── RE_SESSION.md
├── scripts/
└── output/
```

Generated session state should normally be ignored by Git.

## Evidence standard

Prefer conclusions supported by concrete evidence such as:

- addresses;
- function names;
- xrefs;
- strings;
- imports/API calls;
- instructions;
- pseudocode;
- runtime observations;
- process/module information.

Decompiled C-like output is reconstructed pseudocode, not guaranteed original source.
