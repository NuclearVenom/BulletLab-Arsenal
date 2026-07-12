# Contributing to BulletLab Arsenal

Thank you for contributing. Please read the complete **[Package Specification](docs/robot-package-spec.md)** before starting.

## What Is a Package?

A robot package represents a **robot family** — a collection of related URDF models that share the same mesh assets. A single package can contain one or more models.

## Required Package Structure

<details>
<summary><b>Click to view: Required Package Structure</b></summary>

```text
robots/
└── robot_name/
    ├── metadata.json          REQUIRED
    ├── LICENSE                REQUIRED
    ├── NOTICE.md              REQUIRED
    ├── urdf/                  REQUIRED — all URDF files go here
    │   ├── model_variant_a.urdf
    │   └── model_variant_b.urdf
    ├── mesh/                  REQUIRED — one of these two names
    │   OR
    ├── meshes/
    └── verification/          AUTO-GENERATED — do not create manually
```

</details>

Everything else (README.md, docs/, examples/, textures/, images/) is optional and will not be validated.

## URDF Rules

> [!IMPORTANT]
> - **All URDF files must live inside `urdf/`.**
> - **Do not rename URDFs to `robot.urdf`.** Preserve the real upstream filename (e.g. `husky.urdf`, `Unitree_G1_29DOF.urdf`).
> - **Relative mesh paths only.** No `package://`, no absolute paths, no `http://`.
> - **No `xacro`.** Pre-process `xacro` to plain URDF before submission.
> - Mesh paths in URDF must be relative to the URDF file's own location (e.g. `../meshes/base.stl` if the URDF is in `urdf/` and the mesh is in `meshes/`).

## metadata.json

The metadata file defines every model in the package. Example:

<details>
<summary><b>Click to view: Example metadata.json</b></summary>

```json
{
  "name": "unitree_g1",
  "display_name": "Unitree G1",
  "description": "Unitree Robotics G1 humanoid robot. Available in 29-DOF and 26-DOF configurations.",

  "version": "1.1.0",
  "arsenal_version": "1",

  "source": "https://github.com/unitreerobotics/unitree_ros",
  "license": "BSD-3-Clause",

  "authors": ["Unitree Robotics"],
  "maintainers": ["Your Name"],

  "tags": ["humanoid", "legged", "bipedal"],

  "minimum_bulletlab_version": ">=0.2.0",

  "models": [
    {
      "id": "29dof",
      "display_name": "29 DOF",
      "entrypoint": "urdf/Unitree_G1_29DOF.urdf",
      "default": true
    },
    {
      "id": "26dof",
      "display_name": "26 DOF",
      "entrypoint": "urdf/Unitree_G1_26DOF.urdf"
    }
  ]
}
```

</details>

Rules:
- `name` must match the directory name exactly (lowercase, alphanumeric, underscores).
- `arsenal_version` must be `"1"`.
- `models` must be a non-empty array. Exactly one model must have `"default": true`.
- Every `entrypoint` must begin with `urdf/` and the file must exist on disk.

## LICENSE Policy

> [!CAUTION]
> A `LICENSE` file is mandatory. Packages without a valid, non-empty `LICENSE` file are hard-rejected.

| License type | Result |
|---|---|
| MIT, Apache-2.0, BSD, ISC, MPL | Automatic pass |
| GPL, LGPL, AGPL | Founder Review Required — cannot be auto-merged |
| Custom or unrecognised text | Founder Review Required — cannot be auto-merged |
| Missing or empty file | Hard failure |

If your package requires Founder Review, the verification pipeline will still run, but the pull request cannot be merged until a maintainer approves the license manually.

## NOTICE.md

`NOTICE.md` is mandatory and must contain:

- Original project name
- Original source repository URL
- Original authors (if known)
- Original license
- Description of any modifications made for BulletLab Arsenal
- Redistribution notes

## Verification Pipeline

**Install the Arsenal CLI (once, from the repository root):**
```bash
pip install -e .
```

**Full verification pipeline (mandatory before PR):**
```bash
arsenal verify robots/your_robot_name
```

**Structure check only (no simulation, no PyBullet required):**
```bash
arsenal verify robots/your_robot_name --skip-simulation
```

> [!NOTE]
> If you cannot use `pip install`, the underlying script is still available:
> ```bash
> python scripts/run_verification.py robots/your_robot_name
> ```

After the verification pipeline passes, commit the auto-generated `verification/` directory as part of your pull request. This includes the `verification_report.json`, `robot_summary.md`, and all screenshots.

## Submission Guidelines

> [!WARNING]
> - Do not submit a hand-written `verification/` directory.
> - Do not submit robot statistics (dimensions, joint counts) computed outside BulletLab.

> [!NOTE]
> **Screenshots & Images:**
> It is permitted to share user-provided images or screenshots in the package folder for future users to see. However, during the verification process, auto-generated screenshots will be taken, and these will serve as the official verified images for previews and formal documentation. User-provided images cannot replace these verified auto-generated screenshots.

## Pull Request Checklist

- [ ] Read `docs/robot-package-spec.md`.
- [ ] Package directory is named with lowercase, alphanumeric, and underscores.
- [ ] All URDFs are inside `urdf/`.
- [ ] Mesh directory is named `mesh/` or `meshes/`.
- [ ] URDFs use relative mesh paths (no `package://`, no absolute paths).
- [ ] No `xacro` files — plain URDF only.
- [ ] `metadata.json` is complete: all fields present, `models` array populated, one `"default": true`.
- [ ] `LICENSE` is present, non-empty, and uses a recognised license.
- [ ] `NOTICE.md` is present, non-empty, and accurately attributes the original authors.
- [ ] `arsenal verify robots/your_robot_name` passes and the `verification/` directory has been committed.
