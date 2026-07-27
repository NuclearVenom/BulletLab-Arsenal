"""
summary.py - Output summary table for BulletLab Arsenal verification.

Delegates to term.summary_table() for consistent, professional output.
"""
from __future__ import annotations

try:
    from verification import term
except ImportError:
    from . import term  # type: ignore[no-redef]


def print_summary(results: list[dict]) -> None:
    term.summary_table(results)
