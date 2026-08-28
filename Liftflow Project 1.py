#!/usr/bin/env python3
"""Compatibility wrapper for the original repository root script.

This forwards execution to the updated analyzer in
`projects/project-01-service-operations-analyzer/service_operations_analyzer.py`.
"""
from pathlib import Path
import runpy
import sys


def main() -> None:
    project_script = (
        Path(__file__).resolve().parent
        / "projects"
        / "project-01-service-operations-analyzer"
        / "service_operations_analyzer.py"
    )
    if not project_script.exists():
        raise FileNotFoundError(f"Analyzer not found at {project_script}")

    # Run the target script as __main__ so it behaves like a top-level script
    runpy.run_path(str(project_script), run_name="__main__")


if __name__ == "__main__":
    main()