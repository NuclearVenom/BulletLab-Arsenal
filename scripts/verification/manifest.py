"""
manifest.py — BulletLab Arsenal Manifest Generator & Validator

Generates category-level manifests and the global arsenal-manifest.json file.
Extracts contribution history automatically from Git history.
"""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent.parent
_REPO_ROOT = _SCRIPTS_DIR.parent

CATEGORIES = [
    "robots",
    "worlds",
    "sensors",
    "controllers",
    "datasets",
    "benchmarks",
]

def _get_verified_status(pkg_dir: Path) -> tuple[bool, dict[str, bool]]:
    """Check the verification report to see if the package and models are verified."""
    report_path = pkg_dir / "verification" / "verification_report.json"
    if not report_path.is_file():
        return False, {}

    try:
        with open(report_path, "r", encoding="utf-8") as f:
            report = json.load(f)
    except Exception:
        return False, {}

    package_verified = report.get("overall") == "PASS"
    models_verified = {}
    for model in report.get("models", []):
        model_id = model.get("model_id")
        if model_id:
            models_verified[model_id] = model.get("summary", {}).get("overall") == "PASS"
            
    return package_verified, models_verified


def _get_contributors_from_git(pkg_dir: Path) -> list[dict]:
    """Extract contributor history from Git log for a specific directory."""
    try:
        rel_path = pkg_dir.relative_to(_REPO_ROOT)
        result = subprocess.run(
            ["git", "log", "--reverse", "--format=%an|%ae", "--", str(rel_path)],
            cwd=str(_REPO_ROOT),
            capture_output=True,
            text=True,
            check=True
        )
    except (subprocess.CalledProcessError, ValueError):
        return []

    lines = result.stdout.strip().split("\n")
    if not lines or not lines[0]:
        return []

    contributors = []
    seen = set()

    for i, line in enumerate(lines):
        parts = line.split("|")
        if len(parts) != 2:
            continue
        
        name = parts[0].strip()
        email = parts[1].strip()
        
        lower_name = name.lower()
        if lower_name in seen:
            continue
        
        seen.add(lower_name)
        
        # Try to infer GitHub username from email
        github = None
        if email.endswith("@users.noreply.github.com"):
            prefix = email.split("@")[0]
            if "+" in prefix:
                github = prefix.split("+", 1)[1]
            else:
                github = prefix

        role = "original_submission" if i == 0 else "package_update"
        
        contributors.append({
            "name": name,
            "github": github,
            "role": role
        })

    return contributors


def generate_category_manifest(category_dir: Path) -> dict:
    """Generate the manifest.json for a specific category directory."""
    manifest_path = category_dir / "manifest.json"
    packages = []
    
    if category_dir.exists():
        for meta_path in sorted(category_dir.rglob("metadata.json")):
            item = meta_path.parent
            if not item.is_dir():
                continue
            
            try:
                with open(meta_path, "r", encoding="utf-8") as f:
                    meta = json.load(f)
            except Exception as e:
                print(f"Warning: Could not read metadata for {item.name}: {e}")
                continue

            pkg_name = meta.get("name", item.name)
            pkg_verified, models_verified = _get_verified_status(item)
            
            # Fetch contributors from Git history
            contributors = _get_contributors_from_git(item)
            
            # If no git history (e.g. uncommitted files), fallback to metadata author
            if not contributors:
                authors = meta.get("authors", [])
                if authors:
                    contributors.append({
                        "name": authors[0],
                        "github": None,
                        "role": "original_submission"
                    })

            # Build models
            models = []
            for m in meta.get("models", []):
                model_id = m.get("id", "")
                models.append({
                    "id": model_id,
                    "display_name": m.get("display_name", ""),
                    "entrypoint": m.get("entrypoint", ""),
                    "verified": models_verified.get(model_id, False)
                })

            # Manufacturer detection
            rel_to_cat = item.relative_to(category_dir)
            manufacturer = rel_to_cat.parts[0] if len(rel_to_cat.parts) > 1 else ""

            pkg_entry = {
                "package_name": pkg_name,
                "display_name": meta.get("display_name", ""),
                "description": meta.get("description", ""),
                "version": meta.get("version", ""),
                "license": meta.get("license", ""),
                "verified": pkg_verified,
                "minimum_bulletlab_version": meta.get("minimum_bulletlab_version", ""),
                "source": meta.get("source", ""),
                "tags": meta.get("tags", []),
                "authors": meta.get("authors", []),
                "maintainers": meta.get("maintainers", []),
                "contributors": contributors,
                "models": models
            }
            if manufacturer:
                pkg_entry["manufacturer"] = manufacturer
            packages.append(pkg_entry)

    manifest_data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "bulletlab_arsenal_version": "1",
        "package_count": len(packages),
        "packages": packages
    }

    if category_dir.exists():
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest_data, f, indent=2)
            f.write("\n")
        print(f"Generated manifest for {category_dir.name} with {len(packages)} packages.")
        
    return manifest_data


def generate_global_manifest(category_data: dict[str, dict]) -> None:
    """Generate the global arsenal-manifest.json."""
    global_path = _REPO_ROOT / "arsenal-manifest.json"
    
    total_count = sum(data.get("package_count", 0) for data in category_data.values())
    
    global_data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "bulletlab_arsenal_version": "1",
        "total_package_count": total_count,
        "robot_count": category_data.get("robots", {}).get("package_count", 0),
        "world_count": category_data.get("worlds", {}).get("package_count", 0),
        "sensor_count": category_data.get("sensors", {}).get("package_count", 0),
        "controller_count": category_data.get("controllers", {}).get("package_count", 0),
        "dataset_count": category_data.get("datasets", {}).get("package_count", 0),
        "benchmark_count": category_data.get("benchmarks", {}).get("package_count", 0),
        "categories": {}
    }
    
    for category in CATEGORIES:
        data = category_data.get(category)
        if data:
            global_data["categories"][category] = data.get("packages", [])
            
    with open(global_path, "w", encoding="utf-8") as f:
        json.dump(global_data, f, indent=2)
        f.write("\n")
    print(f"Generated global arsenal-manifest.json with {total_count} total packages.")


def generate_manifests() -> None:
    print("Generating BulletLab Arsenal Manifests...")
    category_data = {}
    for category in CATEGORIES:
        category_dir = _REPO_ROOT / category
        if category_dir.exists():
            data = generate_category_manifest(category_dir)
            category_data[category] = data
            
    generate_global_manifest(category_data)
    print("Manifest generation complete.")

def validate_manifests() -> bool:
    """Validate internal consistency of manifests (stub implementation from original)."""
    # Simply check if the global manifest was written successfully.
    global_path = _REPO_ROOT / "arsenal-manifest.json"
    if not global_path.is_file():
        print("ERROR: Global manifest is missing.")
        return False
    return True
