#!/usr/bin/env python3
"""Launch IDA Pro, x64dbg/x32dbg, or GDB and persist a /re session."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

TOOL_ALIASES = {"ida": "ida", "idapro": "ida", "ida-pro": "ida", "x64dbg": "x64dbg", "x32dbg": "x32dbg", "gdb": "gdb", "gdp": "gdb"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def detect_arch(path: Path) -> str | None:
    try:
        header = path.read_bytes()[:0x2000]
        if header[:2] == b"MZ" and len(header) >= 0x40:
            off = int.from_bytes(header[0x3C:0x40], "little")
            if off + 6 <= len(header) and header[off:off + 4] == b"PE\0\0":
                machine = int.from_bytes(header[off + 4:off + 6], "little")
                return {0x014C: "x86", 0x8664: "x86_64", 0xAA64: "arm64", 0x01C4: "armnt"}.get(machine)
        if header[:4] == b"\x7fELF" and len(header) >= 20:
            return {1: "32-bit", 2: "64-bit"}.get(header[4])
    except OSError:
        pass
    return None


def normalize_tool(value: str) -> str:
    key = value.lower().strip()
    if key not in TOOL_ALIASES:
        raise ValueError(f"Unknown debugger '{value}'. Use ida, x64dbg, x32dbg, or gdb (gdp is also accepted).")
    return TOOL_ALIASES[key]


def dedupe(paths: Iterable[Path]) -> list[Path]:
    seen: set[Path] = set()
    output: list[Path] = []
    for path in paths:
        try:
            resolved = path.expanduser().resolve()
        except OSError:
            continue
        if resolved in seen:
            continue
        seen.add(resolved)
        output.append(resolved)
    return output


def candidate_paths(tool: str) -> list[Path]:
    candidates: list[Path] = []
    if tool == "ida":
        envs = ("HCLI_CURRENT_IDA_INSTALL_DIR", "IDADIR", "IDA_PATH")
        names = ("ida64.exe", "ida.exe", "ida64", "ida")
    elif tool in {"x64dbg", "x32dbg"}:
        envs = ("X64DBG_DIR", "X64DBG_PATH")
        names = ("x64dbg.exe", "x32dbg.exe") if tool == "x64dbg" else ("x32dbg.exe",)
    else:
        envs = ("GDB_PATH", "GDB")
        names = ("gdb.exe", "gdb")

    for env_name in envs:
        value = os.environ.get(env_name)
        if value:
            base = Path(value).expanduser()
            if base.is_file():
                candidates.append(base)
            else:
                candidates.extend(base / name for name in names)

    for name in names:
        found = shutil.which(name)
        if found:
            candidates.append(Path(found))

    if os.name == "nt":
        roots = [Path(x) for x in (os.environ.get("ProgramFiles"), os.environ.get("ProgramW6432"), os.environ.get("LOCALAPPDATA")) if x]
        if tool == "ida":
            for root in roots:
                for pattern in ("IDA Professional*", "Hex-Rays*", "IDA*"):
                    for directory in root.glob(pattern):
                        candidates.extend(directory / name for name in names)
        elif tool in {"x64dbg", "x32dbg"}:
            for root in roots:
                for pattern in ("x64dbg*", "x32dbg*"):
                    for directory in root.glob(pattern):
                        candidates.extend(directory / name for name in names)
                candidates.extend(root / "x64dbg" / name for name in names)
    else:
        for base in (Path("/opt"), Path.home() / ".local"):
            if base.exists():
                candidates.extend(base / name for name in names)
    return dedupe(candidates)


def find_executable(tool: str, explicit: str | None, arch: str | None = None) -> Path | None:
    if explicit:
        p = Path(explicit).expanduser()
        if p.is_dir():
            names = ("ida64.exe", "ida.exe") if tool == "ida" else (("x64dbg.exe", "x32dbg.exe") if tool == "x64dbg" else (("x32dbg.exe",))) if tool in {"x64dbg", "x32dbg"} else ("gdb.exe", "gdb")
            for name in names:
                candidate = p / name
                if candidate.is_file():
                    return candidate.resolve()
        elif p.is_file():
            return p.resolve()
        return None

    candidates = candidate_paths(tool)
    if tool == "ida":
        preferred = "ida64.exe" if arch in {"x86_64", "arm64"} and os.name == "nt" else "ida64" if arch in {"x86_64", "arm64"} else "ida.exe" if os.name == "nt" else "ida"
        for path in candidates:
            if path.name.lower() == preferred.lower():
                return path
    if tool == "x64dbg" and arch == "x86":
        for path in candidates:
            if path.name.lower() == "x32dbg.exe":
                return path
    for path in candidates:
        if path.is_file():
            return path
    return None


def wait_for_start(process: subprocess.Popen[bytes], seconds: float = 1.0) -> str:
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        code = process.poll()
        if code is not None:
            return f"exited:{code}"
        time.sleep(0.05)
    return "running"


def write_session(workspace: Path, session: dict) -> None:
    session_dir = workspace / ".max-prompter" / "re"
    session_dir.mkdir(parents=True, exist_ok=True)
    (session_dir / "RE_SESSION.json").write_text(json.dumps(session, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Active Reverse-Engineering Session", "",
        f"- Backend: `{session['backend']}`",
        f"- Mode: `{session['mode']}`",
    ]
    if session.get("target"):
        lines += [f"- Target: `{session['target']}`", f"- SHA-256: `{session['sha256']}`"]
    if session.get("pid") is not None:
        lines.append(f"- PID: `{session['pid']}`")
    lines += [f"- Debugger: `{session['debugger_executable']}`", f"- Launcher PID: `{session['launcher_pid']}`", f"- Started: `{session['started_at']}`", "", "The next user message is the analysis query for this session.", ""]
    (session_dir / "RE_SESSION.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tool", default="ida")
    parser.add_argument("--target")
    parser.add_argument("--pid", type=int)
    parser.add_argument("--target-path", help="known executable path for a PID")
    parser.add_argument("--debugger", help="debugger executable or installation directory")
    parser.add_argument("--workspace", default=".")
    args = parser.parse_args()

    try:
        tool = normalize_tool(args.tool)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.target and args.pid is not None:
        print("ERROR: choose either --target or --pid, not both.", file=sys.stderr)
        return 2
    if not args.target and args.pid is None:
        print("ERROR: a target file or PID is required.", file=sys.stderr)
        return 2

    target = Path(args.target).expanduser().resolve() if args.target else None
    if target and not target.is_file():
        print(f"ERROR: target does not exist or is not a file: {target}", file=sys.stderr)
        return 2

    arch = detect_arch(target) if target else None
    debugger = find_executable(tool, args.debugger, arch)
    if debugger is None:
        hint = {
            "ida": "Set HCLI_CURRENT_IDA_INSTALL_DIR, IDADIR, or IDA_PATH, or pass --debugger.",
            "x64dbg": "Set X64DBG_DIR or X64DBG_PATH, put x64dbg.exe/x32dbg.exe on PATH, or pass --debugger.",
            "gdb": "Put gdb/gdb.exe on PATH, set GDB_PATH/GDB, or pass --debugger.",
        }[tool]
        print(f"ERROR: {tool} was not found. {hint}", file=sys.stderr)
        return 3

    workspace = Path(args.workspace).expanduser().resolve()
    session_dir = workspace / ".max-prompter" / "re"
    session_dir.mkdir(parents=True, exist_ok=True)
    started_at = datetime.now(timezone.utc).isoformat()

    if tool == "ida":
        if target:
            cmd = [str(debugger), str(target)]
            mode = "file"
        else:
            # IDA's documented GUI supports Attach to process. We open the executable database when possible, otherwise an empty DB.
            known = Path(args.target_path).expanduser().resolve() if args.target_path else None
            cmd = [str(debugger)] + ([str(known)] if known and known.is_file() else [])
            mode = "attach"
    elif tool == "x64dbg":
        if args.pid is not None:
            cmd = [str(debugger), "-p", str(args.pid)]
            mode = "attach"
        else:
            cmd = [str(debugger), str(target)]
            mode = "file"
    else:
        if args.pid is not None:
            cmd = [str(debugger), "-p", str(args.pid)]
            mode = "attach"
        else:
            cmd = [str(debugger), str(target)]
            mode = "file"

    session = {
        "version": 2,
        "backend": tool,
        "mode": mode,
        "target": str(target) if target else (str(Path(args.target_path).expanduser().resolve()) if args.target_path else None),
        "sha256": sha256(target) if target else None,
        "architecture_hint": arch or "unknown",
        "pid": args.pid,
        "debugger_executable": str(debugger),
        "started_at": started_at,
        "platform": platform.platform(),
        "launch_command": cmd,
        "status": "launching",
    }
    write_session(workspace, session)

    try:
        process = subprocess.Popen(cmd, cwd=str(target.parent if target else workspace))
    except OSError as exc:
        session["status"] = "launch-failed"
        session["error"] = str(exc)
        write_session(workspace, session)
        print(f"ERROR: failed to launch {tool}: {exc}", file=sys.stderr)
        return 4

    launch_state = wait_for_start(process)
    session["launcher_pid"] = process.pid
    session["launch_observation"] = launch_state
    session["status"] = "running" if launch_state == "running" else "exited"
    write_session(workspace, session)
    print(json.dumps({"status": session["status"], "backend": tool, "debugger": str(debugger), "launcher_pid": process.pid, "mode": mode, "target": session["target"], "pid": args.pid}, indent=2))
    return 0 if launch_state == "running" else 5


if __name__ == "__main__":
    raise SystemExit(main())
