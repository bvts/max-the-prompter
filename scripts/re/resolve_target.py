#!/usr/bin/env python3
"""Resolve local files and enumerate active processes for /re."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import struct
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable

SKIP_DIRS = {
    ".git", ".hg", ".svn", "node_modules", "__pycache__", ".venv", "venv",
    "dist", "build", "target", "coverage", ".next", ".cache"
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fingerprint(path: Path) -> dict[str, str]:
    try:
        data = path.read_bytes()[:0x2000]
    except OSError:
        return {"format": "unreadable", "architecture": "unknown"}

    fmt = "unknown"
    arch = "unknown"
    if data[:2] == b"MZ" and len(data) >= 0x40:
        fmt = "PE"
        pe_offset = struct.unpack_from("<I", data, 0x3C)[0]
        if pe_offset + 6 <= len(data) and data[pe_offset:pe_offset + 4] == b"PE\0\0":
            machine = struct.unpack_from("<H", data, pe_offset + 4)[0]
            arch = {
                0x014C: "x86",
                0x8664: "x86_64",
                0xAA64: "arm64",
                0x01C4: "armnt",
            }.get(machine, f"machine-0x{machine:04X}")
    elif data[:4] == b"\x7fELF" and len(data) >= 20:
        fmt = "ELF"
        arch = {1: "32-bit", 2: "64-bit"}.get(data[4], "unknown")
    elif len(data) >= 4:
        magic = struct.unpack_from(">I", data, 0)[0]
        if magic in {0xFEEDFACF, 0xCFFAEDFE}:
            fmt, arch = "Mach-O", "64-bit"
        elif magic in {0xFEEDFACE, 0xCEFAEDFE}:
            fmt, arch = "Mach-O", "32-bit"
        elif magic in {0xCAFEBABE, 0xBEBAFECA}:
            fmt, arch = "Mach-O/Fat", "universal"
    return {"format": fmt, "architecture": arch}


def iter_files(root: Path) -> Iterable[Path]:
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for filename in files:
            yield Path(base) / filename


def _windows_process_path(pid: int) -> str | None:
    if os.name != "nt":
        return None
    import ctypes
    from ctypes import wintypes

    PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    kernel32.OpenProcess.restype = wintypes.HANDLE
    kernel32.QueryFullProcessImageNameW.argtypes = [wintypes.HANDLE, wintypes.DWORD, wintypes.LPWSTR, ctypes.POINTER(wintypes.DWORD)]
    kernel32.QueryFullProcessImageNameW.restype = wintypes.BOOL
    kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel32.CloseHandle.restype = wintypes.BOOL

    handle = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
    if not handle:
        return None
    try:
        size = wintypes.DWORD(32768)
        buffer = ctypes.create_unicode_buffer(size.value)
        if kernel32.QueryFullProcessImageNameW(handle, 0, buffer, ctypes.byref(size)):
            return buffer.value
    finally:
        kernel32.CloseHandle(handle)
    return None


def _windows_process_arch(pid: int) -> str:
    if os.name != "nt":
        return "unknown"
    import ctypes
    from ctypes import wintypes

    PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    open_process = kernel32.OpenProcess
    open_process.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    open_process.restype = wintypes.HANDLE
    close_handle = kernel32.CloseHandle
    close_handle.argtypes = [wintypes.HANDLE]
    close_handle.restype = wintypes.BOOL

    is_wow64_process2 = getattr(kernel32, "IsWow64Process2", None)
    if is_wow64_process2:
        is_wow64_process2.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.USHORT), ctypes.POINTER(wintypes.USHORT)]
        is_wow64_process2.restype = wintypes.BOOL
        handle = open_process(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
        if handle:
            try:
                process_machine = wintypes.USHORT()
                native_machine = wintypes.USHORT()
                if is_wow64_process2(handle, ctypes.byref(process_machine), ctypes.byref(native_machine)):
                    machine = process_machine.value or native_machine.value
                    return {
                        0x014C: "x86",
                        0x8664: "x86_64",
                        0xAA64: "arm64",
                        0x01C4: "armnt",
                    }.get(machine, f"machine-0x{machine:04X}")
            finally:
                close_handle(handle)
    return "unknown"


def list_processes() -> list[dict[str, Any]]:
    if os.name == "nt":
        # Toolhelp32 avoids PowerShell/WMI and works on stock Windows 11 installations.
        import ctypes
        from ctypes import wintypes

        TH32CS_SNAPPROCESS = 0x00000002
        INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value
        MAX_PATH = 260

        class PROCESSENTRY32W(ctypes.Structure):
            _fields_ = [
                ("dwSize", wintypes.DWORD), ("cntUsage", wintypes.DWORD), ("th32ProcessID", wintypes.DWORD),
                ("th32DefaultHeapID", ctypes.c_size_t), ("th32ModuleID", wintypes.DWORD),
                ("cntThreads", wintypes.DWORD), ("th32ParentProcessID", wintypes.DWORD),
                ("pcPriClassBase", wintypes.LONG), ("dwFlags", wintypes.DWORD),
                ("szExeFile", wintypes.WCHAR * MAX_PATH),
            ]

        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
        if snapshot == INVALID_HANDLE_VALUE:
            raise OSError(ctypes.get_last_error(), "CreateToolhelp32Snapshot failed")
        try:
            first = kernel32.Process32FirstW
            next_process = kernel32.Process32NextW
            first.argtypes = [wintypes.HANDLE, ctypes.POINTER(PROCESSENTRY32W)]
            first.restype = wintypes.BOOL
            next_process.argtypes = [wintypes.HANDLE, ctypes.POINTER(PROCESSENTRY32W)]
            next_process.restype = wintypes.BOOL
            entry = PROCESSENTRY32W()
            entry.dwSize = ctypes.sizeof(PROCESSENTRY32W)
            results: list[dict[str, Any]] = []
            if first(snapshot, ctypes.byref(entry)):
                while True:
                    pid = int(entry.th32ProcessID)
                    path = _windows_process_path(pid)
                    results.append({
                        "pid": pid,
                        "name": entry.szExeFile,
                        "path": path,
                        "architecture": _windows_process_arch(pid),
                        "access": "path-readable" if path else "limited",
                    })
                    if not next_process(snapshot, ctypes.byref(entry)):
                        break
            return sorted(results, key=lambda item: (item["name"].lower(), item["pid"]))
        finally:
            kernel32.CloseHandle(snapshot)

    ps = shutil.which("ps")
    if not ps:
        return []
    completed = subprocess.run([ps, "-eo", "pid=,comm="], capture_output=True, text=True, check=False)
    results = []
    for line in completed.stdout.splitlines():
        parts = line.strip().split(None, 1)
        if not parts:
            continue
        try:
            pid = int(parts[0])
        except ValueError:
            continue
        name = parts[1] if len(parts) > 1 else ""
        proc_path = None
        proc_link = Path(f"/proc/{pid}/exe")
        try:
            if proc_link.exists():
                proc_path = str(proc_link.resolve())
        except OSError:
            pass
        results.append({"pid": pid, "name": name, "path": proc_path, "architecture": "unknown", "access": "unknown"})
    return results


def resolve_files(name: str, root: Path) -> list[Path]:
    candidate = Path(name).expanduser()
    if candidate.exists() and candidate.is_file():
        return [candidate.resolve()]
    workspace_candidate = (root / name).resolve()
    if workspace_candidate.exists() and workspace_candidate.is_file():
        return [workspace_candidate]
    target_name = candidate.name.lower()
    matches = []
    if root.exists():
        for path in iter_files(root):
            if path.name.lower() == target_name:
                matches.append(path.resolve())
    if matches:
        return sorted(set(matches))
    if os.sep not in name and "/" not in name and "\\" not in name:
        found = shutil.which(name)
        if found:
            return [Path(found).resolve()]
    return []


def match_processes(query: str, processes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    q = query.lower().strip()
    q_stem = Path(q).name
    exact = [p for p in processes if p["name"].lower() == q or Path(p["path"] or "").name.lower() == q_stem]
    if exact:
        return exact
    return [p for p in processes if q in p["name"].lower()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve /re targets and scan active processes")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--name", help="program/file name or path")
    group.add_argument("--pid", type=int, help="running process ID")
    group.add_argument("--list-processes", action="store_true", help="list active processes")
    parser.add_argument("--root", default=".")
    parser.add_argument("--process-query", help="match an active process by name")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()

    if args.list_processes or args.process_query:
        processes = list_processes()
        if args.process_query:
            processes = match_processes(args.process_query, processes)
        print(json.dumps({"count": len(processes), "processes": processes}, indent=2))
        return 0

    if args.pid is not None:
        process = next((p for p in list_processes() if p["pid"] == args.pid), None)
        if process is None:
            print(json.dumps({"error": f"No active process with PID {args.pid}."}, indent=2))
            return 2
        print(json.dumps({"kind": "process", "process": process}, indent=2))
        return 0

    if not args.name:
        parser.error("one of --name, --pid, --process-query, or --list-processes is required")

    file_matches = [
        {
            "kind": "file",
            "path": str(path),
            "filename": path.name,
            "size": path.stat().st_size,
            "sha256": sha256(path),
            **fingerprint(path),
        }
        for path in resolve_files(args.name, root)
    ]

    process_matches = [
        {"kind": "process", **process}
        for process in match_processes(args.name, list_processes())
    ]

    result = {
        "query": args.name,
        "workspace": str(root),
        "file_matches": file_matches,
        "process_matches": process_matches,
        "counts": {"files": len(file_matches), "processes": len(process_matches)},
    }
    print(json.dumps(result, indent=2))
    total = len(file_matches) + len(process_matches)
    return 0 if total == 1 else 2 if total == 0 else 3


if __name__ == "__main__":
    raise SystemExit(main())
