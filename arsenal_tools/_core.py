"""
arsenal_tools._core — BulletLab Arsenal CLI Core Utilities

Shared infrastructure used by the CLI:

  - Repository root detection (CWD-based AND package-path-based)
  - sys.path bootstrap for the scripts/verification package
  - Package counting (no duplication: wraps identity.CATEGORIES)
  - Global manifest loading

Nothing in this module implements validation logic.  It only discovers
repository context and wires Python's import system so the CLI can import
the existing verification modules.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Sentinel files / directories used to locate the repository root.
# ---------------------------------------------------------------------------
_ROOT_SENTINELS: tuple[str, ...] = (
    "arsenal-manifest.json",
    "scripts",
    "robots",
)


def find_repo_root(start: Optional[Path] = None) -> Optional[Path]:
    """Walk upward from *start* (or the current directory) to find the
    BulletLab Arsenal repository root.

    The root is identified by the simultaneous presence of all
    ``_ROOT_SENTINELS``.  Returns ``None`` if the root cannot be located.
    """
    candidate = (start or Path.cwd()).resolve()

    # Limit search depth to avoid traversing to filesystem root on bad inputs.
    for _ in range(16):
        if all((candidate / s).exists() for s in _ROOT_SENTINELS):
            return candidate
        parent = candidate.parent
        if parent == candidate:
            break
        candidate = parent

    return None


def find_repo_root_for_package(pkg_path: Path) -> Optional[Path]:
    """Try to locate the Arsenal repository root given a package path.

    Searches in this order:
      1. Walk upward from the *resolved package directory* itself.
      2. Walk upward from the current working directory.

    This allows ``arsenal verify /some/other/project/output/robot_pkg`` to
    work when the package lives outside the Arsenal clone, by also trying the
    CWD as a fallback — and vice versa.

    Returns ``None`` only if neither search finds a valid root.
    """
    # Search from package path first.
    root = find_repo_root(pkg_path.resolve())
    if root is not None:
        return root
    # Fallback: search from CWD.
    return find_repo_root(Path.cwd())


def ensure_scripts_on_path(repo_root: Path) -> None:
    """Insert ``<repo_root>/scripts`` onto sys.path so that
    ``import verification.*`` resolves to the existing modules.

    This is the same mechanism used by ``scripts/run_verification.py``
    itself; keeping it identical ensures one code path.
    """
    scripts_dir = str(repo_root / "scripts")
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)


# ---------------------------------------------------------------------------
# Category constants (keep in sync with verification/identity.py).
# ---------------------------------------------------------------------------
CATEGORIES: tuple[str, ...] = (
    "robots",
    "worlds",
    "sensors",
    "controllers",
    "datasets",
    "benchmarks",
)


def count_packages(repo_root: Path) -> dict[str, int]:
    """Return a mapping of category → package count by scanning the
    repository directories.  Only directories containing a ``metadata.json``
    file are counted as valid packages.

    This reuses the same discovery logic as ``verification/identity.py``
    without importing that module (to keep _core import-safe before
    ensure_scripts_on_path is called).
    """
    counts: dict[str, int] = {cat: 0 for cat in CATEGORIES}
    for cat in CATEGORIES:
        cat_dir = repo_root / cat
        if not cat_dir.is_dir():
            continue
        for item in cat_dir.iterdir():
            if item.is_dir() and (item / "metadata.json").is_file():
                counts[cat] += 1
    return counts


def load_global_manifest(repo_root: Path) -> Optional[dict]:
    """Load and return ``arsenal-manifest.json`` from the repository root.

    Returns ``None`` if the file does not exist or cannot be parsed.
    """
    manifest_path = repo_root / "arsenal-manifest.json"
    if not manifest_path.is_file():
        return None
    try:
        with open(manifest_path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (json.JSONDecodeError, OSError):
        return None


def total_model_count(repo_root: Path) -> int:
    """Count total models across all packages by reading every metadata.json."""
    total = 0
    for cat in CATEGORIES:
        cat_dir = repo_root / cat
        if not cat_dir.is_dir():
            continue
        for item in cat_dir.iterdir():
            meta_path = item / "metadata.json"
            if item.is_dir() and meta_path.is_file():
                try:
                    with open(meta_path, "r", encoding="utf-8") as fh:
                        meta = json.load(fh)
                    total += len(meta.get("models", []))
                except (json.JSONDecodeError, OSError):
                    pass
    return total
