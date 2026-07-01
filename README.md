# BulletLab Arsenal

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

**BulletLab Arsenal** is the official curated collection of verified robotics assets for the [BulletLab](https://github.com/NuclearVenom/BulletLab) robotics framework.

## Project Vision

BulletLab Arsenal is a long-term robotics package ecosystem. Its purpose is to provide high-quality, open-source, and standardised robot packages that load correctly in BulletLab out of the box. BulletLab Arsenal aims to become for robotics assets what PyPI is for Python packages.

Every package is automatically verified by loading it in a headless physics simulation, exercising every joint, rendering reproducible screenshots, and generating a detailed verification report. The pipeline is the sole authority for package statistics and imagery.

## Why BulletLab Arsenal?

Historically, setting up simulated robotics environments has been a fragmented and frustrating experience. Researchers and developers frequently encounter:

- **Inconsistent Repository Layouts:** Every robot project structures its files differently.
- **Missing or Broken Meshes:** URDFs point to files that don't exist or use absolute paths from the author's local machine.
- **ROS-Specific Assumptions:** Dependencies on `package://` URI resolution that break in standalone physics engines.
- **Incompatible Assets:** Inertias, joint limits, or mass values that cause simulators to explode upon loading.

**BulletLab Arsenal solves this.** We provide curated, strictly verified, and self-contained robotics packages that are guaranteed to load and work consistently inside BulletLab out of the box. If a package is in Arsenal, it works.

## Package Design

A robot package represents a **robot family**, not necessarily a single robot model. A single package may contain multiple URDF variants that share the same mesh assets.

For example, a `unitree_g1` package could contain:

<details>
<summary><b>View Example: unitree_g1</b></summary>

```text
unitree_g1/
├── metadata.json
├── LICENSE
├── NOTICE.md
├── urdf/
│   ├── Unitree_G1_29DOF.urdf
│   └── Unitree_G1_26DOF.urdf
├── meshes/
└── verification/        <-- AUTO-GENERATED
```

</details>

The `metadata.json` file defines every installable model in the package.

## Repository Structure

<details>
<summary><b>View Repository Structure</b></summary>

```text
bulletlab-arsenal/
│
├── arsenal-manifest.json    # Global machine-readable manifest
├── docs/                    # Specifications and technical documentation
├── schemas/                 # JSON Schemas for metadata validation
│   ├── latest/              # Always points to the newest stable version
│   └── v1/                  # Version 1 schemas
├── scripts/                 # All validation and verification tools
│
├── robots/                  # Curated robot packages
│   ├── manifest.json        # Generated category manifest
│   └── reference_bot/       # Canonical reference package
│
├── worlds/                  # (Future) Simulated environments
├── sensors/                 # (Future) Sensor plugins
├── controllers/             # (Future) Controllers
├── datasets/                # (Future) Datasets
└── benchmarks/              # (Future) Benchmarks
```

</details>

## Three-Layer Verification Pipeline

All packages go through a mandatory three-layer quality pipeline.

### Layer 1 — Registry Validation

**Module:** `scripts/verification/registry.py`

**Question answered:** Is this package correctly structured?

- All required files and directories are present.
- `metadata.json` is valid and complete.
- Every model entrypoint exists on disk.
- The `LICENSE` file exists, is not empty, and is classified.
- `NOTICE.md` exists and is not empty.
- All URDF mesh paths are relative and the referenced files exist.

**License classification:**
- **Permissive** (MIT, Apache-2.0, BSD, ISC, MPL): automatic pass.
- **Copyleft** (GPL, LGPL, AGPL) or **unknown**: triggers **Founder Review Required**. The package is not auto-merged; a maintainer reviews it manually.
- **Missing or empty LICENSE**: hard failure.

### Layer 2 — Repository Identity Validation

**Module:** `scripts/verification/identity.py`

**Question answered:** Does every package and model have a unique, unambiguous identity across the entire repository?

This layer runs once across the entire Arsenal before any simulation begins. It ensures that future install APIs like `Robot.install("unitree_g1")` always resolve to exactly one package, with no ambiguity.

- Every package name is globally unique across all categories (robots, worlds, sensors, etc.).
- Package names are validated against a reserved-name deny-list.
- Every model `id`, `display_name`, and `entrypoint` is unique within its package.
- Every `.urdf` file in `urdf/` belongs to exactly one model entrypoint.
- Install-API namespace simulation confirms zero naming conflicts.

### Layer 3 — BulletLab Verification

**Module:** `scripts/verification/robot.py`

**Question answered:** Does every model in this package actually work in BulletLab?

For each model defined in `metadata.json`:
- The URDF is loaded in a headless PyBullet simulation.
- The robot AABB is computed and the robot is repositioned cleanly at Z = 0.
- All links and joints are extracted and enumerated.
- Every movable joint is exercised through its full range of motion.
- A short stability simulation is run to detect NaN or exploding geometry.
- 7 reproducible screenshots are rendered from fixed camera angles.
- A `verification_report.json` and `robot_summary.md` are written inside the package's `verification/` directory.

> [!IMPORTANT]
> **The verification system is the sole source of truth for official previews and robot statistics.** While contributors are welcome to include their own images or screenshots in the package folder for users to see, these cannot replace the official auto-generated screenshots. Do not submit pre-computed robot statistics.

### Machine-Readable Manifests

BulletLab Arsenal features an automatically generated machine-readable manifest system designed to make the repository instantly searchable by BulletLab, AI assistants, GitHub tools, and future package managers.

- **Category Manifests:** Each asset category (e.g., `robots/manifest.json`) contains a summarized, searchable inventory of all valid packages in that category, including models, tags, and contribution history.
- **Global Manifest:** A single `arsenal-manifest.json` at the repository root summarizes the entire repository.

> [!WARNING]
> **Contributors must NEVER edit manifest files manually.** Manifests are generated entirely by the master verification pipeline. If you submit a pull request with manual edits to `manifest.json` or `arsenal-manifest.json`, your changes will be overwritten or rejected. The verification pipeline preserves your contribution history automatically.

## Running the Pipeline

The master verification script (`scripts/run_verification.py`) is the official orchestrator and the only public entry point for verification.

**Verify a single package:**
```bash
python scripts/run_verification.py robots/reference_bot
```

**Verify all packages (CI mode):**
```bash
python scripts/run_verification.py --all
```

**Structure check only (no simulation):**
```bash
python scripts/run_verification.py robots/reference_bot --skip-simulation
```

## Documentation

- **[Package Specification](docs/robot-package-spec.md)**: The complete technical standard every package must meet.
- **[Manifest Specification](docs/manifest-spec.md)**: Details on the machine-readable manifest system format and generation.
- **[Contribution Guide](CONTRIBUTING.md)**: How to port a robot, structure a package, and submit a pull request.

## Roadmap

Please read our long-term vision in [ROADMAP.md](ROADMAP.md).

## Licensing

The BulletLab Arsenal framework, schemas, and scripts are licensed under the [MIT License](./LICENSE).

> [!NOTE]
> Individual robot packages under `robots/` may carry their own licenses. Always check the `LICENSE` and `NOTICE.md` file inside each package directory before use. Only permissive open-source licenses are accepted without manual review.
