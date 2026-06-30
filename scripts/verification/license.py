"""
license.py — BulletLab Arsenal License Checker

Classifies and validates package licenses.
"""

from __future__ import annotations
from pathlib import Path

# Substrings detected in license file text → automatic PASS
_PERMISSIVE_SIGNATURES: list[str] = [
    "mit license",
    "apache license",
    "apache-2.0",
    "bsd 2-clause",
    "bsd 3-clause",
    "isc license",
    "mozilla public license",
    "mpl-2.0",
    "boost software license",      # BSL-1.0
]

# Substrings detected in license file text → Founder Review Required
_REVIEW_SIGNATURES: list[str] = [
    "gnu general public license",
    "gnu lesser general public license",
    "gnu affero general public license",
    "gpl",
    "lgpl",
    "agpl",
]

def classify_license(text: str) -> str:
    """Return 'permissive', 'review', or 'unknown' based on license file text."""
    lower = text.lower()
    for sig in _PERMISSIVE_SIGNATURES:
        if sig in lower:
            return "permissive"
    for sig in _REVIEW_SIGNATURES:
        if sig in lower:
            return "review"
    return "unknown"

def check_license(pkg_dir: Path) -> tuple[list[str], str]:
    """Verify LICENSE exists, is not empty, and classify it.

    Returns (errors, license_class) where license_class is one of:
    'permissive', 'review', 'unknown', 'missing'.
    """
    errors: list[str] = []
    license_path = pkg_dir / "LICENSE"
    if not license_path.is_file():
        errors.append("LICENSE file not found. A valid LICENSE file is mandatory.")
        return errors, "missing"
    text = license_path.read_text(encoding="utf-8", errors="replace").strip()
    if not text:
        errors.append("LICENSE file is empty. A valid LICENSE file is mandatory.")
        return errors, "missing"
    classification = classify_license(text)
    return errors, classification
