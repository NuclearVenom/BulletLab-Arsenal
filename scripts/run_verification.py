"""
run_verification.py — BulletLab Arsenal Master Verification Orchestrator

This is the single entry point for GitHub Actions and the primary command
contributors run before submitting a pull request.

It orchestrates the full verification pipeline in order:

  1. Registry Validation       — per-package structure, metadata, URDF paths.
  2. Identity Validation       — global uniqueness: package names, model IDs,
                                 entrypoints, install-API namespace.
  3. Robot Verification        — loads every model in simulation, exercises
                                 joints, captures screenshots.
  4. Manifest Generation       — rebuilds category and global manifests.
  5. Final Report Generation   — writes a machine-readable run report.
  6. Summary                   — prints a human-readable table to stdout.

Usage:
  # Verify a single robot package:
  python scripts/run_verification.py robots/reference_bot

  # Verify all robot packages (CI mode):
  python scripts/run_verification.py --all

  # Custom screenshot resolution:
  python scripts/run_verification.py robots/unitree_g1 --width 1920 --height 1080

Exit codes:
  0  — all packages accepted automatically (all layers passed)
  1  — one or more packages failed hard validation or verification
  2  — one or more packages require Founder Review
       (review packages are reported as distinct status; CI treats this as blocking)

The exit code is always non-zero when the package cannot be auto-merged.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPTS_DIR))

from verification.registry import validate_package, PackageResult
from verification.identity import validate_identity, print_identity_report
from verification.robot import verify_robot
from verification.manifest import generate_manifests, validate_manifests
from verification.report import write_master_report
from verification.summary import print_summary

_REPO_ROOT  = _SCRIPTS_DIR.parent
_ROBOTS_DIR = _REPO_ROOT / "robots"


def run_pipeline_for_package(
    pkg_dir: Path,
    screenshot_width: int,
    screenshot_height: int,
) -> dict:
    """Run the per-package pipeline stages (Layer 1 + Layer 3) for a single package.

    Identity Validation (Layer 2) operates across the whole repository and is
    run once by main() before this function is called for each package.

    Returns a pipeline result dict with keys:
      package         — package name
      layer1          — Layer 1 PackageResult fields
      layer2          — Layer 3 verify_robot() report (or None if skipped)
      final_status    — 'PASS' | 'FAIL' | 'FOUNDER_REVIEW'
    """
    pkg_name = pkg_dir.name
    print(f"\n{'#' * 60}")
    print(f"# Package: {pkg_name}")
    print(f"{'#' * 60}")

    # ── Layer 1: Registry Validation ──────────────────────────────────────
    print("\n[Layer 1] Registry Validation")
    l1: PackageResult = validate_package(pkg_dir)

    print(f"  Result: {'PASSED' if l1.passed else 'FAILED'}", end="")
    if l1.review:
        print("  (FOUNDER REVIEW REQUIRED)", end="")
    print(f"\n  License: {l1.license_class}")

    if l1.errors:
        print("  Errors:")
        for e in l1.errors:
            print(f"    - {e}")
    if l1.warnings:
        print("  Warnings:")
        for w in l1.warnings:
            print(f"    - {w}")

    l1_dict = {
        "passed":        l1.passed,
        "review":        l1.review,
        "license_class": l1.license_class,
        "errors":        l1.errors,
        "warnings":      l1.warnings,
    }

    if not l1.passed:
        return {
            "package":      pkg_name,
            "layer1":       l1_dict,
            "layer2":       None,
            "final_status": "FAIL",
        }

    # ── Layer 3: Robot Verification ────────────────────────────────────────
    print("\n[Layer 3] BulletLab Verification")
    l2 = verify_robot(
        package_dir=pkg_dir,
        screenshot_width=screenshot_width,
        screenshot_height=screenshot_height,
    )

    l2_passed  = l2.get("_passed", False)
    l2_overall = l2.get("overall", "FAIL")
    print(f"  Result: {l2_overall}")

    l2_dict = {k: v for k, v in l2.items() if not k.startswith("_")}

    # ── Final status ───────────────────────────────────────────────────────
    if not l2_passed:
        final_status = "FAIL"
    elif l1.review:
        final_status = "FOUNDER_REVIEW"
    else:
        final_status = "PASS"

    return {
        "package":      pkg_name,
        "layer1":       l1_dict,
        "layer2":       l2_dict,
        "final_status": final_status,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "BulletLab Arsenal Master Verification Orchestrator.\n\n"
            "Runs the full pipeline:\n"
            "  1. Registry Validation   (per-package structure & metadata)\n"
            "  2. Identity Validation   (global uniqueness across all packages)\n"
            "  3. Robot Verification    (BulletLab simulation & screenshots)\n"
            "  4. Manifest Generation\n"
            "  5. Final Report & Summary"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "package",
        nargs="?",
        help="Path to a single robot package directory (e.g. robots/reference_bot).",
    )
    group.add_argument(
        "--all",
        action="store_true",
        help="Discover and verify all robot packages under robots/.",
    )
    parser.add_argument("--width",  type=int, default=1920,
                        help="Screenshot width in pixels (default: 1920).")
    parser.add_argument("--height", type=int, default=1080,
                        help="Screenshot height in pixels (default: 1080).")
    parser.add_argument(
        "--skip-simulation",
        action="store_true",
        help=(
            "Skip Layer 3 robot simulation. Useful for rapid structural checks "
            "when BulletLab or PyBullet is not installed in the environment."
        ),
    )

    args = parser.parse_args()

    if args.all:
        if not _ROBOTS_DIR.exists():
            print(f"ERROR: robots/ directory not found at {_ROBOTS_DIR}")
            sys.exit(1)
        pkg_dirs = sorted(d for d in _ROBOTS_DIR.iterdir() if d.is_dir())
        if not pkg_dirs:
            print("No robot packages found under robots/.")
            sys.exit(0)
    else:
        pkg_dirs = [Path(args.package).resolve()]
        if not pkg_dirs[0].is_dir():
            print(f"ERROR: Package directory not found: {pkg_dirs[0]}")
            sys.exit(1)

    print(f"\nBulletLab Arsenal — Full Verification Pipeline")
    print(f"Packages to process: {len(pkg_dirs)}")

    # ── Layer 2: Repository Identity Validation (cross-package, runs once) ─
    print(f"\n{'=' * 70}")
    print("LAYER 2 — REPOSITORY IDENTITY VALIDATION")
    print(f"{'=' * 70}")
    identity_result = validate_identity(_REPO_ROOT)
    print_identity_report(identity_result)

    if not identity_result.passed:
        print(
            "\nPipeline ABORTED: Repository Identity Validation failed.\n"
            "Fix all identity errors before proceeding to robot verification."
        )
        sys.exit(1)

    # ── Layers 1 + 3: Per-package Registry + Robot Verification ───────────
    results: list[dict] = []
    for pkg_dir in pkg_dirs:
        if args.skip_simulation:
            # Run Layer 1 only
            pkg_name = pkg_dir.name
            print(f"\n{'#' * 60}")
            print(f"# Package: {pkg_name}  [simulation skipped]")
            print(f"{'#' * 60}")
            print("\n[Layer 1] Registry Validation")
            from verification.registry import validate_package as _vp
            l1 = _vp(pkg_dir)
            print(f"  Result: {'PASSED' if l1.passed else 'FAILED'}")
            if l1.errors:
                for e in l1.errors:
                    print(f"    - {e}")
            l1_dict = {
                "passed":        l1.passed,
                "review":        l1.review,
                "license_class": l1.license_class,
                "errors":        l1.errors,
                "warnings":      l1.warnings,
            }
            final = "FAIL" if not l1.passed else ("FOUNDER_REVIEW" if l1.review else "PASS")
            results.append({
                "package":      pkg_name,
                "layer1":       l1_dict,
                "layer2":       None,
                "final_status": final,
            })
        else:
            r = run_pipeline_for_package(pkg_dir, args.width, args.height)
            results.append(r)

    # ── Layer 4: Manifest Generation ──────────────────────────────────────
    print(f"\n{'=' * 70}")
    print("LAYER 4 — MANIFEST GENERATION")
    print(f"{'=' * 70}")
    generate_manifests()

    # ── Layer 5: Final Report + Summary ───────────────────────────────────
    write_master_report(results, _REPO_ROOT)
    print_summary(results)

    print(f"\n{'=' * 70}")
    print("MANIFEST INTERNAL VALIDATION")
    print(f"{'=' * 70}")
    manifest_valid = validate_manifests()

    # ── Exit code ──────────────────────────────────────────────────────────
    any_failed = any(r["final_status"] == "FAIL" for r in results)
    any_review = any(r["final_status"] == "FOUNDER_REVIEW" for r in results)

    if any_failed or not manifest_valid:
        print(
            "\nPipeline FAILED. One or more packages did not pass verification, "
            "or manifest validation failed."
        )
        sys.exit(1)

    if any_review:
        print(
            "\nPipeline completed with FOUNDER REVIEW REQUIRED status. "
            "These packages cannot be auto-merged. A maintainer must review "
            "the license before the package can be accepted."
        )
        sys.exit(2)

    print("\nAll packages passed the full verification pipeline.")
    sys.exit(0)


if __name__ == "__main__":
    main()
