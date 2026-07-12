"""
arsenal_tools.cli — BulletLab Arsenal Official Command-Line Interface

Entry point registered as the ``arsenal`` console script by pyproject.toml.

All validation and verification logic lives in ``scripts/verification/``.
This module is a *thin interface* — it resolves context, imports the existing
functions, and maps CLI arguments to them.  There is intentionally no
duplicated logic here.

Usage
-----
    arsenal --version
    arsenal --help
    arsenal verify <path> [--skip-simulation] [--width W] [--height H]
    arsenal verify-all    [--skip-simulation] [--width W] [--height H]
    arsenal validate      [<path> | --all]
    arsenal manifest
    arsenal info

Exit codes
----------
    0  All packages accepted automatically (all layers passed).
    1  One or more packages failed hard validation / verification,
       or a manifest error occurred.
    2  One or more packages require Founder Review (cannot auto-merge).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import arsenal_tools
from arsenal_tools._core import (
    CATEGORIES,
    count_packages,
    ensure_scripts_on_path,
    find_repo_root,
    find_repo_root_for_package,
    load_global_manifest,
    total_model_count,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_SEP_WIDE  = "=" * 70
_SEP_DASH  = "-" * 70

# The directory that contains *this* file is the installed arsenal_tools
# package.  The Arsenal repository's scripts/ sits one level above it when
# installed with pip install -e .
_INSTALLED_PKG_DIR = Path(__file__).resolve().parent
_ARSENAL_REPO_ROOT_HINT = _INSTALLED_PKG_DIR.parent  # repo root in editable install


def _resolve_repo_root() -> Path:
    """Locate the repository root from CWD, or exit with an informative message."""
    # Also try from the installed package location (editable install resolves to repo root).
    root = find_repo_root() or find_repo_root(_ARSENAL_REPO_ROOT_HINT)
    if root is None:
        print(
            "error: cannot locate the BulletLab Arsenal repository root.\n"
            "Run this command from inside a cloned BulletLab Arsenal repository,\n"
            "or ensure 'arsenal-manifest.json', 'scripts/', and 'robots/' are present.",
            file=sys.stderr,
        )
        sys.exit(1)
    return root


def _find_repo_root_best_effort(pkg_path: Path) -> Path | None:
    """Try every known location to find the Arsenal repo root.

    Search order:
      1. Walk up from the *package path* (handles packages nested inside an
         Arsenal clone under a non-standard category directory).
      2. Walk up from CWD (normal use case — user is inside the clone).
      3. Walk up from the installed package directory (editable install).

    Returns ``None`` if no root is found — the caller enters portable mode.
    """
    return (
        find_repo_root_for_package(pkg_path)
        or find_repo_root(_ARSENAL_REPO_ROOT_HINT)
    )


def _bootstrap(repo_root: Path) -> None:
    """Put scripts/ on sys.path so verification modules import cleanly."""
    ensure_scripts_on_path(repo_root)


# ---------------------------------------------------------------------------
# Command implementations
# ---------------------------------------------------------------------------

def cmd_verify(args: argparse.Namespace) -> None:
    """Full verification pipeline for a single package.

    Operates in two modes depending on whether an Arsenal repository root
    can be found:

    FULL MODE (Arsenal repo detected)
      Runs the complete 5-layer pipeline:
        Layer 1  Registry Validation
        Layer 2  Repository Identity Validation (cross-package)
        Layer 3  BulletLab Simulation & Screenshots
        Layer 4  Manifest Generation
        Layer 5  Report & Summary

    PORTABLE MODE (no Arsenal repo found — e.g. called from another project)
      Runs the per-package layers that work on any standalone package:
        Layer 1  Registry Validation
        Layer 3  BulletLab Simulation & Screenshots
      Skips Layers 2, 4, and 5 (they require the full repo structure).
      All output is written inside the package's own verification/ directory.
    """
    pkg_path = Path(args.path).resolve()
    if not pkg_path.is_dir():
        print(f"error: package directory not found: {pkg_path}", file=sys.stderr)
        sys.exit(1)

    # Try to find the Arsenal repo root from every possible angle.
    repo_root = _find_repo_root_best_effort(pkg_path)
    portable  = repo_root is None

    if portable:
        # Bootstrap verification imports from the installed arsenal_tools
        # package's sibling scripts/ directory (editable install layout).
        _bootstrap(_ARSENAL_REPO_ROOT_HINT)
    else:
        _bootstrap(repo_root)

    # Deferred imports (must come after bootstrap so sys.path is ready).
    from verification.registry import validate_package

    # ── PORTABLE MODE ──────────────────────────────────────────────────────
    if portable:
        print(f"\n{'─' * 70}")
        print("BulletLab Arsenal — Portable Package Verification")
        print(f"{'─' * 70}")
        print(f"  Package   : {pkg_path}")
        print(f"  Mode      : PORTABLE  (no Arsenal repository found in search path)")
        print(f"  Skipping  : Layer 2 (identity), Layer 4 (manifest), Layer 5 (report)")
        print(f"  Output    : {pkg_path / 'verification'}/")
        print(f"{'─' * 70}")

        pkg_name = pkg_path.name

        # Layer 1
        print(f"\n{'#' * 60}")
        print(f"# Package: {pkg_name}")
        print(f"{'#' * 60}")
        print("\n[Layer 1] Registry Validation")
        l1 = validate_package(pkg_path)
        print(f"  Result : {'PASSED' if l1.passed else 'FAILED'}", end="")
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

        if not l1.passed:
            print("\nLayer 1 FAILED. Fix all errors before simulation.", file=sys.stderr)
            sys.exit(1)

        # Layer 3
        if not args.skip_simulation:
            from verification.robot import verify_robot
            print(f"\n[Layer 3] BulletLab Verification")
            try:
                l2 = verify_robot(
                    package_dir=pkg_path,
                    screenshot_width=args.width,
                    screenshot_height=args.height,
                )
            except RuntimeError as exc:
                print(f"\nerror: {exc}", file=sys.stderr)
                sys.exit(1)
            l2_overall = l2.get("overall", "FAIL")
            l2_passed  = l2.get("_passed", False)
            print(f"  Result : {l2_overall}")

            print(f"\n{'─' * 70}")
            if l1.review:
                print("Status: FOUNDER REVIEW REQUIRED (license)")
                sys.exit(2)
            if l2_passed:
                print("Portable verification PASSED. "
                      "Screenshots and report are inside the package's verification/ directory.")
                sys.exit(0)
            else:
                print("Portable verification FAILED (simulation).", file=sys.stderr)
                sys.exit(1)
        else:
            print(f"\n{'─' * 70}")
            if l1.review:
                print("Status: FOUNDER REVIEW REQUIRED (license)")
                sys.exit(2)
            print("Layer 1 PASSED. Simulation skipped (--skip-simulation).")
            sys.exit(0)

    # ── FULL MODE ──────────────────────────────────────────────────────────
    from verification.identity import validate_identity, print_identity_report
    from verification.manifest import generate_manifests, validate_manifests
    from verification.report   import write_master_report
    from verification.summary  import print_summary

    print(f"\nBulletLab Arsenal — Full Verification Pipeline")
    print(f"  Package   : {pkg_path}")
    print(f"  Repository: {repo_root}")

    # Layer 2: Identity (cross-package, runs once across full repo)
    print(f"\n{_SEP_WIDE}")
    print("LAYER 2 — REPOSITORY IDENTITY VALIDATION")
    print(_SEP_WIDE)
    identity_result = validate_identity(repo_root)
    print_identity_report(identity_result)

    if not identity_result.passed:
        print(
            "\nPipeline ABORTED: Repository Identity Validation failed.\n"
            "Fix all identity errors before proceeding to robot verification.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Layers 1 + 3: Per-package pipeline
    if args.skip_simulation:
        pkg_name = pkg_path.name
        print(f"\n{'#' * 60}")
        print(f"# Package: {pkg_name}  [simulation skipped]")
        print(f"{'#' * 60}")
        print("\n[Layer 1] Registry Validation")
        l1 = validate_package(pkg_path)
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
        results = [{"package": pkg_name, "layer1": l1_dict, "layer2": None, "final_status": final}]
    else:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "_run_verification",
            repo_root / "scripts" / "run_verification.py",
        )
        mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
        spec.loader.exec_module(mod)                 # type: ignore[union-attr]
        try:
            result = mod.run_pipeline_for_package(
                pkg_path,
                args.width,
                args.height,
            )
        except RuntimeError as exc:
            print(f"\nerror: {exc}", file=sys.stderr)
            sys.exit(1)
        results = [result]

    any_failed = any(r["final_status"] == "FAIL"            for r in results)
    any_review = any(r["final_status"] == "FOUNDER_REVIEW"  for r in results)

    # Layer 4: Manifest
    print(f"\n{_SEP_WIDE}")
    if any_failed:
        print("LAYER 4 — MANIFEST GENERATION SKIPPED")
        print(_SEP_WIDE)
        manifest_valid = True
    else:
        print("LAYER 4 — MANIFEST GENERATION")
        print(_SEP_WIDE)
        generate_manifests()

    # Layer 5: Report + Summary
    write_master_report(results, repo_root)
    print_summary(results)

    if not any_failed:
        print(f"\n{_SEP_WIDE}")
        print("MANIFEST INTERNAL VALIDATION")
        print(_SEP_WIDE)
        manifest_valid = validate_manifests()

    if any_failed or not manifest_valid:
        print(
            "\nPipeline FAILED. One or more packages did not pass verification, "
            "or manifest validation failed.",
            file=sys.stderr,
        )
        sys.exit(1)

    if any_review:
        print(
            "\nPipeline completed with FOUNDER REVIEW REQUIRED status. "
            "These packages cannot be auto-merged. A maintainer must review "
            "the license before the package can be accepted."
        )
        sys.exit(2)

    print("\nPackage passed the full verification pipeline.")
    sys.exit(0)


def cmd_verify_all(args: argparse.Namespace) -> None:
    """Full verification pipeline for every package in the repository."""
    repo_root = _resolve_repo_root()
    _bootstrap(repo_root)

    # Delegate entirely to the existing orchestrator module.
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "_run_verification",
        repo_root / "scripts" / "run_verification.py",
    )
    mod = importlib.util.module_from_spec(spec)               # type: ignore[arg-type]
    spec.loader.exec_module(mod)                              # type: ignore[union-attr]

    robots_dir = repo_root / "robots"
    if not robots_dir.exists():
        print("error: robots/ directory not found.", file=sys.stderr)
        sys.exit(1)

    pkg_dirs = sorted(d for d in robots_dir.iterdir() if d.is_dir())
    if not pkg_dirs:
        print("No robot packages found under robots/.")
        sys.exit(0)

    from verification.identity   import validate_identity, print_identity_report
    from verification.manifest   import generate_manifests, validate_manifests
    from verification.report     import write_master_report
    from verification.summary    import print_summary

    print(f"\nBulletLab Arsenal — Full Verification Pipeline (ALL)")
    print(f"Packages to process: {len(pkg_dirs)}")

    print(f"\n{_SEP_WIDE}")
    print("LAYER 2 — REPOSITORY IDENTITY VALIDATION")
    print(_SEP_WIDE)
    identity_result = validate_identity(repo_root)
    print_identity_report(identity_result)

    if not identity_result.passed:
        print(
            "\nPipeline ABORTED: Repository Identity Validation failed.",
            file=sys.stderr,
        )
        sys.exit(1)

    results: list[dict] = []
    for pkg_dir in pkg_dirs:
        if args.skip_simulation:
            from verification.registry import validate_package
            pkg_name = pkg_dir.name
            print(f"\n{'#' * 60}")
            print(f"# Package: {pkg_name}  [simulation skipped]")
            print(f"{'#' * 60}")
            l1 = validate_package(pkg_dir)
            print(f"  Result: {'PASSED' if l1.passed else 'FAILED'}")
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
            results.append({"package": pkg_name, "layer1": l1_dict, "layer2": None, "final_status": final})
        else:
            r = mod.run_pipeline_for_package(pkg_dir, args.width, args.height)
            results.append(r)

    print(f"\n{_SEP_WIDE}")
    print("LAYER 4 — MANIFEST GENERATION")
    print(_SEP_WIDE)
    generate_manifests()

    write_master_report(results, repo_root)
    print_summary(results)

    print(f"\n{_SEP_WIDE}")
    print("MANIFEST INTERNAL VALIDATION")
    print(_SEP_WIDE)
    manifest_valid = validate_manifests()

    any_failed = any(r["final_status"] == "FAIL"            for r in results)
    any_review = any(r["final_status"] == "FOUNDER_REVIEW"  for r in results)

    if any_failed or not manifest_valid:
        print("\nPipeline FAILED.", file=sys.stderr)
        sys.exit(1)

    if any_review:
        print(
            "\nPipeline completed with FOUNDER REVIEW REQUIRED status. "
            "A maintainer must review flagged packages before they can be merged."
        )
        sys.exit(2)

    print("\nAll packages passed the full verification pipeline.")
    sys.exit(0)


def cmd_validate(args: argparse.Namespace) -> None:
    """Identity + registry validation only — no simulation."""
    repo_root = _resolve_repo_root()
    _bootstrap(repo_root)

    from verification.identity import validate_identity, print_identity_report
    from verification.registry import validate_package

    print(f"\nBulletLab Arsenal — Validation (no simulation)")
    print(f"Repository: {repo_root}")

    # Always run identity validation across the full repo.
    print(f"\n{_SEP_WIDE}")
    print("LAYER 2 — REPOSITORY IDENTITY VALIDATION")
    print(_SEP_WIDE)
    identity_result = validate_identity(repo_root)
    print_identity_report(identity_result)

    # Per-package registry validation.
    if args.all:
        robots_dir = repo_root / "robots"
        pkg_dirs = sorted(d for d in robots_dir.iterdir() if d.is_dir()) if robots_dir.is_dir() else []
    elif args.path:
        pkg_path = Path(args.path).resolve()
        if not pkg_path.is_dir():
            print(f"error: package directory not found: {pkg_path}", file=sys.stderr)
            sys.exit(1)
        pkg_dirs = [pkg_path]
    else:
        pkg_dirs = []

    any_failed = not identity_result.passed
    for pkg_dir in pkg_dirs:
        print(f"\n[Layer 1] Registry Validation — {pkg_dir.name}")
        l1 = validate_package(pkg_dir)
        status = "PASSED" if l1.passed else "FAILED"
        if l1.review:
            status = "FOUNDER REVIEW"
        print(f"  Result : {status}")
        print(f"  License: {l1.license_class}")
        for e in l1.errors:
            print(f"  ERROR  : {e}")
        for w in l1.warnings:
            print(f"  WARN   : {w}")
        if not l1.passed:
            any_failed = True

    if any_failed:
        sys.exit(1)
    sys.exit(0)


def cmd_manifest(_args: argparse.Namespace) -> None:
    """Regenerate all manifests (category + global)."""
    repo_root = _resolve_repo_root()
    _bootstrap(repo_root)

    from verification.manifest import generate_manifests, validate_manifests

    print(f"\nBulletLab Arsenal — Manifest Generation")
    print(f"Repository: {repo_root}\n")
    generate_manifests()

    print(f"\n{_SEP_WIDE}")
    print("MANIFEST INTERNAL VALIDATION")
    print(_SEP_WIDE)
    ok = validate_manifests()
    if not ok:
        print("error: manifest validation failed after generation.", file=sys.stderr)
        sys.exit(1)

    print("Manifests regenerated and validated successfully.")
    sys.exit(0)


def cmd_info(_args: argparse.Namespace) -> None:
    """Display BulletLab Arsenal installation and repository context."""
    repo_root = find_repo_root() or find_repo_root(_ARSENAL_REPO_ROOT_HINT)

    print(f"\n{'─' * 50}")
    print("  BulletLab Arsenal")
    print(f"{'─' * 50}")
    print(f"  Arsenal Version   : {arsenal_tools.ARSENAL_VERSION}")
    print(f"  CLI Version       : {arsenal_tools.__version__}")
    print(f"  Schema Version    : {arsenal_tools.SCHEMA_VERSION}")
    print(f"  Developer         : {arsenal_tools.__author__}")

    if repo_root is None:
        print(f"\n  Repository Root   : (not found — run from inside the repository)")
        print(f"{'─' * 50}\n")
        sys.exit(0)

    print(f"\n  Repository Root   : {repo_root}")

    # Manifest status
    manifest = load_global_manifest(repo_root)
    if manifest:
        generated_at = manifest.get("generated_at", "unknown")
        total = manifest.get("total_package_count", "?")
        print(f"  Manifest Status   : present  (generated {generated_at})")
        print(f"  Manifest Packages : {total}")
    else:
        print(f"  Manifest Status   : missing  (run: arsenal manifest)")

    # Live package counts
    counts = count_packages(repo_root)
    total_pkgs  = sum(counts.values())
    total_models = total_model_count(repo_root)

    print(f"\n  Packages by category:")
    max_cat = max(len(c) for c in CATEGORIES)
    for cat in CATEGORIES:
        n = counts[cat]
        bar = ("·" * n) if n else "(none)"
        print(f"    {cat:<{max_cat}}  {n:>3}  {bar}")

    print(f"\n  Total packages    : {total_pkgs}")
    print(f"  Total models      : {total_models}")
    print(f"{'─' * 50}\n")
    sys.exit(0)


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="arsenal",
        description=(
            "BulletLab Arsenal — Official CLI\n\n"
            "The BulletLab Arsenal CLI is the installable command-line interface\n"
            "for the BulletLab robotics asset ecosystem.  It provides one-command\n"
            "access to the full verification pipeline, manifest regeneration, and\n"
            "repository status reporting.\n\n"
            "Quick start:\n"
            "  git clone https://github.com/NuclearVenom/BulletLab-Arsenal\n"
            "  cd BulletLab-Arsenal\n"
            "  pip install -e .\n"
            "  arsenal verify robots/reference_bot"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exit codes:\n"
            "  0  All packages accepted automatically.\n"
            "  1  One or more packages failed hard validation or verification.\n"
            "  2  One or more packages require Founder Review.\n\n"
            "Documentation: https://github.com/NuclearVenom/BulletLab-Arsenal"
        ),
    )
    parser.add_argument(
        "--version", "-V",
        action="version",
        version=f"arsenal {arsenal_tools.__version__} (BulletLab Arsenal {arsenal_tools.ARSENAL_VERSION})",
    )

    subparsers = parser.add_subparsers(dest="command", metavar="<command>")

    # ── verify ────────────────────────────────────────────────────────────
    verify_p = subparsers.add_parser(
        "verify",
        help="Run the verification pipeline on a single package.",
        description=(
            "Run the BulletLab Arsenal verification pipeline on a single robot\n"
            "package.  Works in two modes:\n\n"
            "FULL MODE  (run from inside an Arsenal repository clone)\n"
            "  Layer 1  Registry Validation   (structure, metadata, URDF)\n"
            "  Layer 2  Identity Validation    (global uniqueness across repo)\n"
            "  Layer 3  BulletLab Simulation   (loads URDF, exercises joints)\n"
            "  Layer 4  Manifest Generation\n"
            "  Layer 5  Report & Summary\n\n"
            "PORTABLE MODE  (run from anywhere — no Arsenal repo required)\n"
            "  Layer 1  Registry Validation\n"
            "  Layer 3  BulletLab Simulation & Screenshots\n"
            "  Output is written inside the package's own verification/ directory.\n"
            "  Layers 2, 4, and 5 are skipped (they require the full repo).\n\n"
            "Examples:\n"
            "  arsenal verify robots/reference_bot\n"
            "  arsenal verify C:\\path\\to\\robot_package\n"
            "  arsenal verify output/my_robot          # from any project\n"
            "  arsenal verify robots/reference_bot --skip-simulation"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    verify_p.add_argument(
        "path",
        help="Path to the robot package directory (e.g. robots/reference_bot).",
    )
    verify_p.add_argument(
        "--skip-simulation",
        action="store_true",
        help=(
            "Skip Layer 3 robot simulation.  Useful for rapid structural checks\n"
            "when BulletLab or PyBullet is not installed in the environment."
        ),
    )
    verify_p.add_argument("--width",  type=int, default=1920,
                          help="Screenshot width in pixels (default: 1920).")
    verify_p.add_argument("--height", type=int, default=1080,
                          help="Screenshot height in pixels (default: 1080).")
    verify_p.set_defaults(func=cmd_verify)

    # ── verify-all ────────────────────────────────────────────────────────
    verify_all_p = subparsers.add_parser(
        "verify-all",
        help="Run the full verification pipeline on every package in the repository.",
        description=(
            "Discover and verify every robot package under robots/.  This is\n"
            "the command GitHub Actions CI uses on every pull request.\n\n"
            "Example:\n"
            "  arsenal verify-all\n"
            "  arsenal verify-all --skip-simulation"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    verify_all_p.add_argument(
        "--skip-simulation",
        action="store_true",
        help="Skip Layer 3 robot simulation for all packages.",
    )
    verify_all_p.add_argument("--width",  type=int, default=1920,
                              help="Screenshot width in pixels (default: 1920).")
    verify_all_p.add_argument("--height", type=int, default=1080,
                              help="Screenshot height in pixels (default: 1080).")
    verify_all_p.set_defaults(func=cmd_verify_all)

    # ── validate ──────────────────────────────────────────────────────────
    validate_p = subparsers.add_parser(
        "validate",
        help="Run identity + registry validation only (no simulation).",
        description=(
            "Run Layer 1 (registry) and Layer 2 (identity) validation without\n"
            "launching any physics simulation.  Fast and dependency-free.\n\n"
            "Examples:\n"
            "  arsenal validate robots/reference_bot\n"
            "  arsenal validate --all"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    validate_group = validate_p.add_mutually_exclusive_group()
    validate_group.add_argument(
        "path",
        nargs="?",
        help="Path to a single robot package directory.",
    )
    validate_group.add_argument(
        "--all",
        action="store_true",
        help="Validate every robot package in the repository.",
    )
    validate_p.set_defaults(func=cmd_validate)

    # ── manifest ──────────────────────────────────────────────────────────
    manifest_p = subparsers.add_parser(
        "manifest",
        help="Regenerate all manifests (category + global arsenal-manifest.json).",
        description=(
            "Regenerate every category manifest (robots/manifest.json, etc.) and\n"
            "the global arsenal-manifest.json.  The manifests are machine-readable\n"
            "and must never be edited manually.\n\n"
            "Example:\n"
            "  arsenal manifest"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    manifest_p.set_defaults(func=cmd_manifest)

    # ── info ──────────────────────────────────────────────────────────────
    info_p = subparsers.add_parser(
        "info",
        help="Display Arsenal version, repository context, and package counts.",
        description=(
            "Print concise information about the current BulletLab Arsenal\n"
            "installation and the detected repository:\n\n"
            "  - Arsenal version and CLI version\n"
            "  - Schema version\n"
            "  - Developer\n"
            "  - Detected repository root\n"
            "  - Manifest status and generation timestamp\n"
            "  - Package counts by category\n"
            "  - Total package and model count\n\n"
            "Example:\n"
            "  arsenal info"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    info_p.set_defaults(func=cmd_info)

    return parser


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Console script entry point registered by pyproject.toml."""
    parser = _build_parser()
    args   = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    # Dispatch to the appropriate command function.
    args.func(args)


if __name__ == "__main__":
    main()
