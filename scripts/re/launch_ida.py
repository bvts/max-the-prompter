#!/usr/bin/env python3
"""Backward-compatible IDA launcher wrapper for /re."""
from __future__ import annotations

import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().with_name("launch_debugger.py")

if __name__ == "__main__":
    import runpy
    sys.argv[1:1] = ["--tool", "ida"]
    runpy.run_path(str(SCRIPT), run_name="__main__")
