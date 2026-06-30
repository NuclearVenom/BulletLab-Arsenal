"""
registry.py — BulletLab Arsenal Layer 1 Registry Validator

This is the first layer of the two-layer quality pipeline.
It answers:  "Is this package correctly structured?"
"""

from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import NamedTuple

from verification.license import check_license


class PackageResult(NamedTuple):
    name: str
    passed: bool         # True = hard pass (no errors); False = hard fail
    review: bool         # True = Founder Review Required
    errors: list[str]
    warnings: list[str]
    license_class: str   # 'permissive', 'review', 'unknown', or 'missing'


def _check_metadata(pkg_dir: Path, pkg_name: str) -> tuple[list[str], list[str], dict]:
    """Validate metadata.json.  Returns (errors, warnings, parsed_meta)."""
    errors: list[str] = []
    warnings: list[str] = []
    meta: dict = {}

    meta_path = pkg_dir / "metadata.json"
    if not meta_path.is_file():
        errors.append("metadata.json not found.")
        return errors, warnings, meta

    try:
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
    except json.JSONDecodeError as exc:
        errors.append(f"metadata.json is not valid JSON: {exc}")
        return errors, warnings, meta

    # Required top-level fields
    required_fields = [
        "name", "display_name", "description", "version", "arsenal_version",
        "source", "license", "authors", "maintainers", "tags",
        "minimum_bulletlab_version", "models",
    ]
    for field in required_fields:
        if field not in meta:
            errors.append(f"metadata.json missing required field: '{field}'")

    # Name must match folder
    if meta.get("name") and meta["name"] != pkg_name:
        errors.append(
            f"metadata.json 'name' field ('{meta['name']}') "
            f"does not match directory name ('{pkg_name}')."
        )

    # arsenal_version must be "1"
    if meta.get("arsenal_version") and meta["arsenal_version"] != "1":
        errors.append(
            f"metadata.json 'arsenal_version' must be '1', "
            f"got '{meta['arsenal_version']}'."
        )

    # models must be a non-empty list
    models = meta.get("models", [])
    if not isinstance(models, list) or len(models) == 0:
        errors.append("metadata.json 'models' must be a non-empty array.")
    else:
        default_count = 0
        for i, model in enumerate(models):
            if not isinstance(model, dict):
                errors.append(f"models[{i}] must be a JSON object.")
                continue
            for mfield in ("id", "display_name", "entrypoint"):
                if mfield not in model:
                    errors.append(f"models[{i}] missing required field: '{mfield}'")
            # entrypoint must be inside urdf/
            ep = model.get("entrypoint", "")
            if ep and not ep.startswith("urdf/"):
                errors.append(
                    f"models[{i}] entrypoint '{ep}' must begin with 'urdf/'."
                )
            # entrypoint file must exist
            if ep:
                ep_path = pkg_dir / ep
                if not ep_path.is_file():
                    errors.append(
                        f"models[{i}] entrypoint '{ep}' does not exist on disk."
                    )
            if model.get("default") is True:
                default_count += 1

        if default_count == 0:
            errors.append("metadata.json 'models': exactly one model must have 'default': true.")
        elif default_count > 1:
            errors.append(
                f"metadata.json 'models': {default_count} models have 'default': true. "
                "Only one is allowed."
            )

    # authors and maintainers must be non-empty arrays of strings
    for arr_field in ("authors", "maintainers"):
        val = meta.get(arr_field, [])
        if not isinstance(val, list) or len(val) == 0:
            errors.append(f"metadata.json '{arr_field}' must be a non-empty array.")

    return errors, warnings, meta


def _check_urdf(pkg_dir: Path, entrypoint: str) -> list[str]:
    """Validate a single URDF entrypoint.  Returns a list of errors."""
    errors: list[str] = []
    urdf_path = pkg_dir / entrypoint

    if not urdf_path.is_file():
        errors.append(f"URDF not found: {entrypoint}")
        return errors

    try:
        content = urdf_path.read_text(encoding="utf-8")
    except Exception as exc:
        errors.append(f"Cannot read URDF '{entrypoint}': {exc}")
        return errors

    if "package://" in content:
        errors.append(
            f"URDF '{entrypoint}' contains 'package://' URIs. "
            "All mesh paths must be relative."
        )

    try:
        tree = ET.parse(str(urdf_path))
        root = tree.getroot()
        for mesh_el in root.findall(".//mesh"):
            filename = mesh_el.get("filename", "")
            if not filename:
                continue
            if filename.startswith("/") or filename.startswith("http"):
                errors.append(
                    f"URDF '{entrypoint}': absolute or external mesh path: '{filename}'"
                )
                continue
            
            # Check supported mesh formats
            lower_name = filename.lower()
            if not (lower_name.endswith(".stl") or lower_name.endswith(".dae") or lower_name.endswith(".obj")):
                errors.append(f"URDF '{entrypoint}': unsupported mesh format '{filename}'. Allowed formats: STL, DAE, OBJ.")

            # Mesh paths are relative to the URDF file's own directory.
            # Resolve from the URDF's parent folder.
            resolved = (urdf_path.parent / filename).resolve()
            if not resolved.is_file():
                errors.append(
                    f"URDF '{entrypoint}': mesh file not found: '{filename}'"
                )
    except ET.ParseError as exc:
        errors.append(f"URDF '{entrypoint}' is not valid XML: {exc}")

    return errors


def _check_notice(pkg_dir: Path) -> list[str]:
    """Verify NOTICE.md exists and is not empty."""
    errors: list[str] = []
    notice_path = pkg_dir / "NOTICE.md"
    if not notice_path.is_file():
        errors.append("NOTICE.md not found.")
        return errors
    if notice_path.stat().st_size == 0:
        errors.append("NOTICE.md is empty.")
    return errors


def validate_package(pkg_dir: Path) -> PackageResult:
    """Run full Layer 1 validation on a single package directory."""
    pkg_name = pkg_dir.name
    errors: list[str] = []
    warnings: list[str] = []
    license_class = "missing"

    # 1. Required mandatory files
    if not (pkg_dir / "metadata.json").is_file():
        errors.append("metadata.json not found.")
    if not (pkg_dir / "NOTICE.md").is_file():
        errors.append("NOTICE.md not found.")

    # 2. LICENSE check
    lic_errors, license_class = check_license(pkg_dir)
    errors.extend(lic_errors)

    # 3. Required directory: urdf/
    urdf_dir = pkg_dir / "urdf"
    if not urdf_dir.is_dir():
        errors.append("Required directory 'urdf/' not found.")
    else:
        # At least one .urdf file must exist
        urdf_files = list(urdf_dir.glob("*.urdf"))
        if not urdf_files:
            errors.append("'urdf/' directory exists but contains no .urdf files.")
        
        # Check for .xacro files in urdf/
        xacro_files = list(urdf_dir.glob("*.xacro"))
        if xacro_files:
            errors.append(f"Found .xacro files in 'urdf/'. Only plain .urdf files are allowed.")
            
    # Check for misplaced .urdf or .xacro files outside urdf/
    for file in pkg_dir.rglob("*.urdf"):
        if file.parent != urdf_dir:
            errors.append(f"Misplaced URDF file: '{file.relative_to(pkg_dir)}'. All URDF files must live inside 'urdf/'.")
    for file in pkg_dir.rglob("*.xacro"):
        if file.parent != urdf_dir:
            errors.append(f"Found .xacro file: '{file.relative_to(pkg_dir)}'. Only plain .urdf files are allowed, and they must live inside 'urdf/'.")

    # 4. Required directory: mesh/ or meshes/
    has_mesh = (pkg_dir / "mesh").is_dir()
    has_meshes = (pkg_dir / "meshes").is_dir()
    if not has_mesh and not has_meshes:
        errors.append(
            "No mesh directory found. Package must contain either 'mesh/' or 'meshes/'."
        )
    if has_mesh and has_meshes:
        warnings.append(
            "Both 'mesh/' and 'meshes/' directories exist. "
            "Only one should be present. The validator will accept this, but "
            "please consolidate to avoid ambiguity."
        )

    # 5. NOTICE.md
    notice_errors = _check_notice(pkg_dir)
    errors.extend(notice_errors)

    # 6. metadata.json
    meta_errors, meta_warnings, meta = _check_metadata(pkg_dir, pkg_name)
    errors.extend(meta_errors)
    warnings.extend(meta_warnings)

    # 7. URDF validation for each model entrypoint
    for model in meta.get("models", []):
        ep = model.get("entrypoint", "")
        if ep:
            urdf_errors = _check_urdf(pkg_dir, ep)
            errors.extend(urdf_errors)

    # Determine review flag
    review = license_class in ("review", "unknown") and not any(
        "LICENSE" in e for e in errors
    )

    passed = len(errors) == 0

    return PackageResult(
        name=pkg_name,
        passed=passed,
        review=review,
        errors=errors,
        warnings=warnings,
        license_class=license_class,
    )
