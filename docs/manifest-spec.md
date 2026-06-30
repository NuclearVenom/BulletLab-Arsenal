# BulletLab Arsenal Manifest Specification

Version 1

---

## Overview

BulletLab Arsenal features a fully automated, machine-readable manifest system. The manifest makes the repository instantly searchable by BulletLab, AI assistants, GitHub tools, humans, and future package managers.

> [!WARNING]
> **Contributors must NEVER edit manifest files manually.**
> Manifests are automatically rebuilt by the master verification pipeline (`scripts/run_verification.py`). If you manually edit a manifest file, your changes will be overwritten or rejected.

---

## Manifest Types

There are two levels of manifests:

1. **Category Manifests** (e.g., `robots/manifest.json`, `worlds/manifest.json`)
   - Summarises all valid packages within a specific asset category.
   - Contains detailed metadata, verification status, and contribution history for each package.
   
2. **Global Manifest** (`arsenal-manifest.json`)
   - Located at the repository root.
   - Summarises the entire repository, providing global counts and an aggregated view of all category manifests.

---

## Contributor History Preservation

The manifest system automatically tracks contribution history. 
When the verification pipeline regenerates a manifest, it queries the Git log for each package directory to identify who has modified it.

- **Original Submissions:** The author of the first commit modifying a package is assigned the role `"original_submission"`.
- **Package Updates:** Any subsequent authors who modify the package are appended to the manifest with the role `"package_update"`.

Because this is based entirely on the repository's Git history, you do not need to list GitHub usernames in your package's `metadata.json`. The pipeline handles this automatically.

---

## Category Manifest Format

Each category directory contains a `manifest.json` file. It is designed to be compact, excluding heavy objects like screenshot arrays or verbose verification logs.

**Example Structure:**

```json
{
  "generated_at": "2026-06-27T12:00:00+00:00",
  "bulletlab_arsenal_version": "1",
  "package_count": 1,
  "packages": [
    {
      "package_name": "unitree_g1",
      "display_name": "Unitree G1",
      "description": "...",
      "version": "1.0.0",
      "license": "BSD-3-Clause",
      "verified": true,
      "minimum_bulletlab_version": ">=0.2.0",
      "source": "...",
      "tags": ["humanoid", "legged"],
      "authors": ["Unitree Robotics"],
      "maintainers": ["Your Name"],
      "contributors": [
        {
          "name": "Ranasurya Ghosh",
          "github": "NuclearVenom",
          "role": "original_submission"
        }
      ],
      "models": [
        {
          "id": "29dof",
          "display_name": "29 DOF",
          "entrypoint": "urdf/Unitree_G1_29DOF.urdf",
          "verified": true
        }
      ]
    }
  ]
}
```

---

## Global Manifest Format

The `arsenal-manifest.json` file at the repository root aggregates statistics and content across all categories.

**Example Structure:**

```json
{
  "generated_at": "2026-06-27T12:00:00+00:00",
  "bulletlab_arsenal_version": "1",
  "total_package_count": 25,
  "robot_count": 15,
  "world_count": 5,
  "sensor_count": 3,
  "controller_count": 2,
  "dataset_count": 0,
  "benchmark_count": 0,
  "categories": {
    "robots": [ ... package objects ... ],
    "worlds": [ ... package objects ... ]
  }
}
```

---

## Validation

The master verification script (`scripts/run_verification.py`) builds and ensures the integrity of the generated manifests. It verifies that:
- Manifests exist for every populated category.
- The global manifest exists and is valid.
- Every package on disk matches exactly one entry in the manifest (no missing packages, no orphaned manifest entries).
- There are no duplicate package names.

The master verification script (`scripts/run_verification.py`) rebuilds manifests from scratch. It does not expect contributors to sync manifests; instead, it enforces the single source of truth at the pipeline level.
