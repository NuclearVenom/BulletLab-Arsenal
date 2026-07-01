"""
identity.py — BulletLab Arsenal Repository Identity Validator

This is the inter-package validation layer that runs after per-package registry
validation (Layer 1) but before robot verification (Layer 2).

Its sole responsibility is to guarantee that every asset in BulletLab Arsenal
has one and only one canonical identity, so that future APIs such as:

    Robot.install("unitree_g1")
    World.install("warehouse")
    Sensor.install("realsense_d435")

can always resolve unambiguously, without requiring users to specify repository
paths or manually resolve naming conflicts.

This module operates on the full set of discovered packages across ALL
categories, not on individual packages.

Checks performed
----------------
1.  Package name format        — valid characters, no whitespace, no reserved names
2.  Package name ↔ folder      — metadata["name"] matches directory name exactly
3.  Category-level uniqueness  — no two packages in the same category share a name
4.  Global namespace           — names are unique across ALL categories
5.  Display name advisory      — warns if two packages share a display_name
6.  Model ID uniqueness        — no duplicate model IDs within a package
7.  Model display_name         — warns if two models in the same package share a display_name
8.  Model entrypoint uniqueness — no two models in the same package share an entrypoint
9.  Entrypoint validity        — path exists, lives inside urdf/, cannot escape the package
10. URDF coverage              — every .urdf in urdf/ belongs to exactly one model
11. Manifest consistency       — generated manifests match the on-disk package set
12. Install namespace simulation — every package resolves to exactly one target
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import NamedTuple

# ── Constants ─────────────────────────────────────────────────────────────────

#: Names that can never be used as a package identifier.
RESERVED_NAMES: frozenset[str] = frozenset({
    # Category directories (would shadow the category itself)
    "robots", "worlds", "sensors", "controllers", "datasets", "benchmarks",
    # Pipeline internals
    "install", "fetch", "verification", "manifest", "metadata", "license",
    # Common filesystem collisions
    "readme", "package", "schema", "scripts", "docs", "src",
    # Reserved for future top-level Arsenal commands / APIs
    "arsenal", "registry", "index", "core",
})

#: Valid package name pattern: lowercase letters, digits, underscores only.
_NAME_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_]*$")

#: All known asset categories.
CATEGORIES: tuple[str, ...] = (
    "robots",
    "worlds",
    "sensors",
    "controllers",
    "datasets",
    "benchmarks",
)


# ── Data types ─────────────────────────────────────────────────────────────────

class PackageInfo(NamedTuple):
    """Lightweight descriptor for a discovered package."""
    name: str              # metadata["name"]
    display_name: str      # metadata["display_name"]
    category: str          # parent category directory name
    pkg_dir: Path          # absolute path to the package directory
    models: list[dict]     # raw model list from metadata.json


@dataclass
class IdentityResult:
    passed: bool = True
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checks: dict[str, str] = field(default_factory=dict)   # check label → PASS/FAIL/WARN

    def fail(self, check: str, message: str) -> None:
        self.passed = False
        self.checks[check] = "FAIL"
        self.errors.append(message)

    def warn(self, check: str, message: str) -> None:
        if check not in self.checks or self.checks[check] == "PASS":
            self.checks[check] = "WARN"
        self.warnings.append(message)

    def ok(self, check: str) -> None:
        if check not in self.checks:
            self.checks[check] = "PASS"


# ── Internal helpers ───────────────────────────────────────────────────────────

def _load_package_info(pkg_dir: Path, category: str) -> PackageInfo | None:
    """Read metadata.json and return a PackageInfo, or None on parse error."""
    meta_path = pkg_dir / "metadata.json"
    if not meta_path.is_file():
        return None
    try:
        with open(meta_path, "r", encoding="utf-8") as fh:
            meta = json.load(fh)
    except (json.JSONDecodeError, OSError):
        return None
    return PackageInfo(
        name=meta.get("name", ""),
        display_name=meta.get("display_name", ""),
        category=category,
        pkg_dir=pkg_dir,
        models=meta.get("models", []),
    )


def _discover_packages(repo_root: Path) -> list[PackageInfo]:
    """Walk every known category and collect PackageInfo for each package."""
    infos: list[PackageInfo] = []
    for cat in CATEGORIES:
        cat_dir = repo_root / cat
        if not cat_dir.is_dir():
            continue
        for item in sorted(cat_dir.iterdir()):
            if not item.is_dir():
                continue
            info = _load_package_info(item, cat)
            if info is not None:
                infos.append(info)
    return infos


# ── Individual check functions ─────────────────────────────────────────────────

def _check_name_format(info: PackageInfo, result: IdentityResult) -> None:
    """Check 1 — Package name format."""
    name = info.name

    if name != name.strip():
        result.fail(
            "Package name format",
            f"[{info.category}/{info.pkg_dir.name}] metadata 'name' has "
            "leading/trailing whitespace.",
        )
        return

    if not name:
        result.fail(
            "Package name format",
            f"[{info.category}/{info.pkg_dir.name}] metadata 'name' is empty.",
        )
        return

    if not _NAME_PATTERN.match(name):
        result.fail(
            "Package name format",
            f"[{info.category}/{info.pkg_dir.name}] metadata 'name' '{name}' "
            "contains invalid characters. Only lowercase letters, digits, and "
            "underscores are allowed; must start with a letter or digit.",
        )
        return

    if name in RESERVED_NAMES:
        result.fail(
            "Package name format",
            f"[{info.category}/{info.pkg_dir.name}] metadata 'name' '{name}' "
            "is a reserved Arsenal name and cannot be used as a package identifier. "
            f"Reserved names: {sorted(RESERVED_NAMES)}",
        )
        return

    result.ok("Package name format")


def _check_name_matches_folder(info: PackageInfo, result: IdentityResult) -> None:
    """Check 2 — metadata["name"] must match the directory name exactly."""
    folder_name = info.pkg_dir.name
    if info.name != folder_name:
        result.fail(
            "Metadata name ↔ folder",
            f"[{info.category}/{folder_name}] metadata 'name' is '{info.name}' "
            f"but the directory is named '{folder_name}'. They must be identical.",
        )
    else:
        result.ok("Metadata name ↔ folder")


def _check_model_identity(info: PackageInfo, result: IdentityResult) -> None:
    """Check 5–7 — Per-package model uniqueness checks."""
    seen_ids: dict[str, int] = {}
    seen_display: dict[str, int] = {}
    seen_entrypoints: dict[str, int] = {}
    pkg_label = f"{info.category}/{info.name}"

    for i, model in enumerate(info.models):
        model_id = model.get("id", "")
        display = model.get("display_name", "")
        entrypoint = model.get("entrypoint", "")

        # Model ID uniqueness
        if model_id in seen_ids:
            result.fail(
                "Model ID uniqueness",
                f"[{pkg_label}] Duplicate model id '{model_id}' "
                f"appears at index {seen_ids[model_id]} and {i}.",
            )
        else:
            seen_ids[model_id] = i
            result.ok("Model ID uniqueness")

        # Model display_name (warning only)
        if display in seen_display:
            result.warn(
                "Model display_name advisory",
                f"[{pkg_label}] Duplicate model display_name '{display}' "
                f"appears at index {seen_display[display]} and {i}.",
            )
        else:
            seen_display[display] = i
            if "Model display_name advisory" not in result.checks:
                result.ok("Model display_name advisory")

        # Model entrypoint uniqueness
        if entrypoint and entrypoint in seen_entrypoints:
            result.fail(
                "Model entrypoint uniqueness",
                f"[{pkg_label}] Duplicate model entrypoint '{entrypoint}' "
                f"appears at index {seen_entrypoints[entrypoint]} and {i}.",
            )
        elif entrypoint:
            seen_entrypoints[entrypoint] = i
            result.ok("Model entrypoint uniqueness")


def _check_entrypoint_validity(info: PackageInfo, result: IdentityResult) -> None:
    """Check 8 — Entrypoint path validation."""
    pkg_label = f"{info.category}/{info.name}"
    pkg_root = info.pkg_dir.resolve()

    for model in info.models:
        ep = model.get("entrypoint", "")
        if not ep:
            result.fail(
                "Entrypoint validity",
                f"[{pkg_label}] Model '{model.get('id', '?')}' has an empty entrypoint.",
            )
            continue

        # Must start with urdf/
        if not ep.startswith("urdf/"):
            result.fail(
                "Entrypoint validity",
                f"[{pkg_label}] Model '{model.get('id', '?')}' entrypoint '{ep}' "
                "must begin with 'urdf/'.",
            )
            continue

        # Resolve path and check it cannot escape the package root
        resolved = (pkg_root / ep).resolve()
        try:
            resolved.relative_to(pkg_root)
        except ValueError:
            result.fail(
                "Entrypoint validity",
                f"[{pkg_label}] Model '{model.get('id', '?')}' entrypoint '{ep}' "
                "resolves outside the package root (path traversal).",
            )
            continue

        # File must exist
        if not resolved.is_file():
            result.fail(
                "Entrypoint validity",
                f"[{pkg_label}] Model '{model.get('id', '?')}' entrypoint '{ep}' "
                "does not exist on disk.",
            )
        else:
            result.ok("Entrypoint validity")


def _check_urdf_coverage(info: PackageInfo, result: IdentityResult) -> None:
    """Check 9 — Every .urdf file in urdf/ must belong to exactly one model."""
    pkg_label = f"{info.category}/{info.name}"
    urdf_dir = info.pkg_dir / "urdf"

    if not urdf_dir.is_dir():
        # urdf/ absence is already caught by registry.py; skip silently here.
        return

    declared_entrypoints: set[str] = set()
    for model in info.models:
        ep = model.get("entrypoint", "")
        if ep.startswith("urdf/"):
            declared_entrypoints.add(ep)

    all_urdfs_on_disk: set[str] = set()
    for urdf_file in urdf_dir.glob("*.urdf"):
        rel = f"urdf/{urdf_file.name}"
        all_urdfs_on_disk.add(rel)

    orphans = all_urdfs_on_disk - declared_entrypoints
    unreachable = declared_entrypoints - all_urdfs_on_disk

    for orphan in sorted(orphans):
        result.fail(
            "URDF coverage",
            f"[{pkg_label}] '{orphan}' exists on disk but is not referenced "
            "by any model entrypoint. Every URDF must belong to exactly one model.",
        )

    for missing in sorted(unreachable):
        result.fail(
            "URDF coverage",
            f"[{pkg_label}] '{missing}' is declared as a model entrypoint but "
            "does not exist on disk.",
        )

    if not orphans and not unreachable:
        result.ok("URDF coverage")


def _check_global_namespace(packages: list[PackageInfo], result: IdentityResult) -> None:
    """Check 3 + 4 — Category-level and global name uniqueness."""
    # Global namespace: names must be unique across ALL categories
    global_name_map: dict[str, list[str]] = defaultdict(list)
    for info in packages:
        if info.name:
            global_name_map[info.name].append(f"{info.category}/{info.name}")

    for name, locations in global_name_map.items():
        if len(locations) == 1:
            result.ok("Global namespace uniqueness")
        else:
            result.fail(
                "Global namespace uniqueness",
                f"Duplicate package identifier '{name}' found in multiple locations:\n"
                + "\n".join(f"    {loc}" for loc in locations),
            )

    # Category-level folder name uniqueness (explicit, even if filesystem prevents it)
    category_map: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    for info in packages:
        folder = info.pkg_dir.name
        category_map[info.category][folder].append(str(info.pkg_dir))

    for cat, folder_map in category_map.items():
        for folder, paths in folder_map.items():
            if len(paths) > 1:
                result.fail(
                    "Category-level uniqueness",
                    f"Duplicate package folder '{folder}' in category '{cat}':\n"
                    + "\n".join(f"    {p}" for p in paths),
                )
            else:
                result.ok("Category-level uniqueness")


def _check_display_name_advisory(packages: list[PackageInfo], result: IdentityResult) -> None:
    """Check — Global display_name advisory (warnings only)."""
    display_map: dict[str, list[str]] = defaultdict(list)
    for info in packages:
        if info.display_name:
            display_map[info.display_name].append(f"{info.category}/{info.name}")

    any_warn = False
    for display, locations in display_map.items():
        if len(locations) > 1:
            any_warn = True
            result.warn(
                "Display name advisory",
                f"Duplicate display_name '{display}' is shared by: "
                + ", ".join(locations)
                + ". This is permitted but may confuse users.",
            )

    if not any_warn:
        result.ok("Display name advisory")


def _check_install_namespace(packages: list[PackageInfo], result: IdentityResult) -> None:
    """Check 10 — Simulate future install API; every name must resolve unambiguously."""
    registry: dict[str, list[str]] = defaultdict(list)
    for info in packages:
        if info.name:
            registry[info.name].append(f"{info.category}/{info.name}")

    ambiguous = False
    for name, destinations in registry.items():
        if len(destinations) > 1:
            ambiguous = True
            result.fail(
                "Install namespace simulation",
                f"Arsenal.install('{name}') is ambiguous — resolves to "
                f"{len(destinations)} packages: {destinations}",
            )

    if not ambiguous:
        result.ok("Install namespace simulation")


def _check_manifest_consistency(
    packages: list[PackageInfo],
    repo_root: Path,
    result: IdentityResult,
) -> None:
    """Check 11 — Validate generated manifests match on-disk state."""
    # Build the expected set of (category, package_name) from live discovery
    expected: set[tuple[str, str]] = {(p.category, p.name) for p in packages if p.name}

    # Check global manifest
    global_manifest_path = repo_root / "arsenal-manifest.json"
    if not global_manifest_path.is_file():
        result.warn(
            "Manifest consistency",
            "arsenal-manifest.json not found. Run the pipeline to generate it.",
        )
        return

    try:
        with open(global_manifest_path, "r", encoding="utf-8") as fh:
            global_manifest = json.load(fh)
    except (json.JSONDecodeError, OSError) as exc:
        result.fail(
            "Manifest consistency",
            f"Could not parse arsenal-manifest.json: {exc}",
        )
        return

    manifest_names: dict[str, list[str]] = defaultdict(list)   # name → categories
    seen_in_manifest: set[tuple[str, str]] = set()

    for cat, pkg_list in global_manifest.get("categories", {}).items():
        if not isinstance(pkg_list, list):
            continue
        seen_pkg_ids_in_cat: set[str] = set()
        for pkg_entry in pkg_list:
            pkg_name = pkg_entry.get("package_name", "")
            if not pkg_name:
                continue

            # Duplicate package in manifest?
            if pkg_name in seen_pkg_ids_in_cat:
                result.fail(
                    "Manifest consistency",
                    f"Package '{pkg_name}' appears more than once in "
                    f"arsenal-manifest.json under category '{cat}'.",
                )
            seen_pkg_ids_in_cat.add(pkg_name)
            manifest_names[pkg_name].append(cat)
            seen_in_manifest.add((cat, pkg_name))

            # Duplicate model IDs within a manifest entry?
            seen_model_ids: set[str] = set()
            for model_entry in pkg_entry.get("models", []):
                mid = model_entry.get("id", "")
                if mid in seen_model_ids:
                    result.fail(
                        "Manifest consistency",
                        f"Model id '{mid}' appears more than once in the manifest "
                        f"entry for '{pkg_name}' in category '{cat}'.",
                    )
                seen_model_ids.add(mid)

    # Packages in manifest but not on disk (stale manifest entries)
    stale = seen_in_manifest - expected
    for cat, name in sorted(stale):
        result.warn(
            "Manifest consistency",
            f"Manifest contains '{cat}/{name}' but no such package exists on disk. "
            "The manifest may be stale — re-run the pipeline to regenerate it.",
        )

    # Packages on disk but missing from manifest
    missing_from_manifest = expected - seen_in_manifest
    for cat, name in sorted(missing_from_manifest):
        result.warn(
            "Manifest consistency",
            f"Package '{cat}/{name}' exists on disk but is absent from the manifest. "
            "Re-run the pipeline to regenerate the manifest.",
        )

    if not stale and not missing_from_manifest:
        result.ok("Manifest consistency")


# ── Public API ─────────────────────────────────────────────────────────────────

def validate_identity(repo_root: Path) -> IdentityResult:
    """Run the full Repository Identity Validation across the entire Arsenal.

    This function is the primary entry point called by run_verification.py.
    It returns an IdentityResult describing all errors and warnings found.
    """
    result = IdentityResult()
    packages = _discover_packages(repo_root)

    if not packages:
        result.ok("Package name format")
        result.ok("Global namespace uniqueness")
        result.ok("Install namespace simulation")
        return result

    # ── Per-package checks ────────────────────────────────────────────────
    for info in packages:
        _check_name_format(info, result)
        _check_name_matches_folder(info, result)
        _check_model_identity(info, result)
        _check_entrypoint_validity(info, result)
        _check_urdf_coverage(info, result)

    # ── Cross-package checks ──────────────────────────────────────────────
    _check_global_namespace(packages, result)
    _check_display_name_advisory(packages, result)
    _check_install_namespace(packages, result)
    _check_manifest_consistency(packages, repo_root, result)

    return result


def print_identity_report(result: IdentityResult) -> None:
    """Print a structured, human-readable identity validation report."""
    status_label = "PASS" if result.passed else "FAIL"
    print(f"\n{'=' * 70}")
    print(f"REPOSITORY IDENTITY VALIDATION  [{status_label}]")
    print(f"{'=' * 70}")

    # Check-level summary
    _ICONS = {"PASS": "✓", "WARN": "⚠", "FAIL": "✗"}
    for check, status in result.checks.items():
        icon = _ICONS.get(status, "?")
        print(f"  {icon} {check}")

    if result.warnings:
        print(f"\n  Warnings ({len(result.warnings)}):")
        for w in result.warnings:
            for line in w.splitlines():
                print(f"    ⚠  {line}")

    if result.errors:
        print(f"\n  Errors ({len(result.errors)}):")
        for e in result.errors:
            for line in e.splitlines():
                print(f"    ✗  {line}")

    print(f"{'=' * 70}")
