"""
arsenal_tools — BulletLab Arsenal CLI Package

This package is the installable Python distribution for BulletLab Arsenal.
After `pip install -e .` from the repository root, the ``arsenal`` command
becomes available system-wide.

Developer : Ranasurya Ghosh
Repository: https://github.com/NuclearVenom/BulletLab-Arsenal
"""

from __future__ import annotations

__all__ = [
    "__version__",
    "__author__",
    "SCHEMA_VERSION",
    "ARSENAL_VERSION",
]

# Increment when the CLI itself changes in a backward-incompatible way.
__version__: str = "1.1.0"

# BulletLab Arsenal schema / metadata format version.
SCHEMA_VERSION: str = "1"

# BulletLab Arsenal repository format version (matches arsenal_version in metadata.json).
ARSENAL_VERSION: str = "1"

__author__: str = "Ranasurya Ghosh"
