"""
term.py — BulletLab Arsenal terminal UI helpers

Provides a clean, professional terminal presentation layer for the
verification pipeline.  All output in the pipeline should flow through
this module so that styling is consistent and can be upgraded in one place.

Rich is an optional dependency.  When it is not installed the module falls
back to plain print() output so that CI with minimal dependencies continues
to work without modification.
"""

from __future__ import annotations

import sys
from contextlib import contextmanager
from typing import Any, Generator, Iterable

# ── Rich availability ─────────────────────────────────────────────────────────

_RICH = False
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    from rich import box
    from rich.progress import (
        Progress,
        SpinnerColumn,
        BarColumn,
        MofNCompleteColumn,
        TextColumn,
        TimeElapsedColumn,
    )
    _RICH = True
    _console = Console(highlight=False)
    _err_console = Console(stderr=True, highlight=False)
except ImportError:
    _console = None          # type: ignore[assignment]
    _err_console = None      # type: ignore[assignment]

# ── Colour tokens (ANSI fallback when Rich is absent) ────────────────────────

_C = {
    "reset":  "\033[0m",
    "bold":   "\033[1m",
    "dim":    "\033[2m",
    "green":  "\033[32m",
    "yellow": "\033[33m",
    "red":    "\033[31m",
    "cyan":   "\033[36m",
    "blue":   "\033[34m",
}

def _ansi(code: str, text: str) -> str:
    """Wrap text in an ANSI escape if stdout supports colour."""
    if not sys.stdout.isatty():
        return text
    return f"{_C[code]}{text}{_C['reset']}"


# ── Public API ────────────────────────────────────────────────────────────────

def rule(char: str = "─", width: int = 70) -> None:
    """Print a horizontal rule."""
    if _RICH:
        _console.rule(style="dim")
    else:
        print(char * width)


def header(title: str, width: int = 70) -> None:
    """Print a bold section heading with surrounding rules."""
    if _RICH:
        _console.print()
        _console.rule(f"[bold]{title}[/bold]")
    else:
        print()
        print("=" * width)
        print(title)
        print("=" * width)


def subheader(title: str, width: int = 70) -> None:
    """Print a secondary heading."""
    if _RICH:
        _console.print(f"\n[bold cyan]{title}[/bold cyan]")
        _console.rule(style="dim cyan")
    else:
        print(f"\n{title}")
        print("─" * width)


def package_banner(name: str) -> None:
    """Print the per-package heading block."""
    if _RICH:
        _console.print()
        _console.print(
            Panel(
                f"[bold white]{name}[/bold white]",
                expand=False,
                border_style="bright_blue",
                padding=(0, 2),
            )
        )
    else:
        bar = "#" * 60
        print(f"\n{bar}")
        print(f"  Package: {name}")
        print(bar)


def status_line(label: str, passed: bool, review: bool = False,
                detail: str = "") -> None:
    """Print a PASS / FAIL / REVIEW status line."""
    if review:
        badge = "[yellow]REVIEW[/yellow]" if _RICH else _ansi("yellow", "REVIEW")
    elif passed:
        badge = "[bold green]PASS[/bold green]" if _RICH else _ansi("green", "PASS")
    else:
        badge = "[bold red]FAIL[/bold red]" if _RICH else _ansi("red", "FAIL")

    suffix = f"  {detail}" if detail else ""
    if _RICH:
        _console.print(f"  {label}: {badge}{suffix}")
    else:
        plain_badge = "REVIEW" if review else ("PASS" if passed else "FAIL")
        print(f"  {label}: {plain_badge}{suffix}")


def info(msg: str) -> None:
    """Print a neutral info line."""
    if _RICH:
        _console.print(f"  [dim]{msg}[/dim]")
    else:
        print(f"  {msg}")


def error(msg: str, *, indent: int = 4) -> None:
    """Print an error line."""
    prefix = " " * indent
    if _RICH:
        _console.print(f"{prefix}[red]✗[/red]  {msg}")
    else:
        print(f"{prefix}✗  {msg}")


def warn(msg: str, *, indent: int = 4) -> None:
    """Print a warning line."""
    prefix = " " * indent
    if _RICH:
        _console.print(f"{prefix}[yellow]⚠[/yellow]  {msg}")
    else:
        print(f"{prefix}⚠  {msg}")


def check_line(label: str, status: str) -> None:
    """Print an identity-check line with icon (PASS/WARN/FAIL)."""
    icons = {
        "PASS": ("✓", "green"),
        "WARN": ("⚠", "yellow"),
        "FAIL": ("✗", "red"),
    }
    icon_char, colour = icons.get(status, ("?", "dim"))
    if _RICH:
        _console.print(f"  [{colour}]{icon_char}[/{colour}]  {label}")
    else:
        print(f"  {icon_char}  {label}")


def backend_notice(lines: list[str]) -> None:
    """Print a clearly visible advisory notice (used for fallback warnings)."""
    if _RICH:
        body = "\n".join(lines)
        _console.print(
            Panel(
                f"[yellow]{body}[/yellow]",
                title="[bold yellow]Advisory[/bold yellow]",
                border_style="yellow",
                expand=False,
                padding=(0, 2),
            )
        )
    else:
        border = "!" * 70
        print(border)
        for line in lines:
            print(f"  {line}")
        print(border)


def step(label: str) -> None:
    """Print a pipeline step label."""
    if _RICH:
        _console.print(f"\n[bold]{label}[/bold]")
    else:
        print(f"\n{label}")


def detail(key: str, value: Any, width: int = 12) -> None:
    """Print a key: value detail line."""
    if _RICH:
        _console.print(f"  [dim]{key:{width}}[/dim] {value}")
    else:
        print(f"  {key:{width}} {value}")


def blank() -> None:
    """Print a blank line."""
    print()


def summary_table(results: list[dict]) -> None:
    """Print the final verification summary table."""
    if not results:
        return

    if _RICH:
        tbl = Table(
            box=box.SIMPLE_HEAD,
            show_footer=False,
            highlight=False,
            border_style="dim",
        )
        tbl.add_column("Package", style="bold", no_wrap=True)
        tbl.add_column("Layer 1", justify="center", width=8)
        tbl.add_column("Layer 3", justify="center", width=8)
        tbl.add_column("Final",   justify="center", width=14)

        _STATUS_STYLE = {
            "PASS":           "[bold green]PASS[/bold green]",
            "FAIL":           "[bold red]FAIL[/bold red]",
            "FOUNDER_REVIEW": "[yellow]REVIEW[/yellow]",
            "REVIEW":         "[yellow]REVIEW[/yellow]",
            "SKIP":           "[dim]SKIP[/dim]",
        }

        for r in results:
            l1_s = "REVIEW" if r["layer1"]["review"] else (
                "PASS" if r["layer1"]["passed"] else "FAIL"
            )
            l2_d = r.get("layer2")
            l2_s = l2_d.get("overall", "SKIP") if l2_d else "SKIP"
            final = r["final_status"]
            tbl.add_row(
                r["package"],
                _STATUS_STYLE.get(l1_s, l1_s),
                _STATUS_STYLE.get(l2_s, l2_s),
                _STATUS_STYLE.get(final, final),
            )

        _console.print()
        _console.rule("[bold]Verification Summary[/bold]")
        _console.print(tbl)
    else:
        col = max(len(r["package"]) for r in results) + 2
        print(f"\n{'=' * 70}")
        print("VERIFICATION SUMMARY")
        print(f"{'=' * 70}")
        print(f"  {'Package':<{col}}  {'L1':<8}  {'L3':<8}  Final")
        print(f"  {'-' * (col + 28)}")
        for r in results:
            l1_s = "REVIEW" if r["layer1"]["review"] else (
                "PASS" if r["layer1"]["passed"] else "FAIL"
            )
            l2_d = r.get("layer2")
            l2_s = l2_d.get("overall", "SKIP") if l2_d else "SKIP"
            print(f"  {r['package']:<{col}}  {l1_s:<8}  {l2_s:<8}  {r['final_status']}")
        print(f"{'=' * 70}")

    total  = len(results)
    passed = sum(1 for r in results if r["final_status"] == "PASS")
    review = sum(1 for r in results if r["final_status"] == "FOUNDER_REVIEW")
    failed = sum(1 for r in results if r["final_status"] == "FAIL")

    if _RICH:
        _console.print(
            f"  [bold]Total:[/bold] {total}  "
            f"[green]Passed:[/green] {passed}  "
            f"[yellow]Review:[/yellow] {review}  "
            f"[red]Failed:[/red] {failed}"
        )
    else:
        print(f"\n  Total: {total}  |  Passed: {passed}  |  "
              f"Founder Review: {review}  |  Failed: {failed}")


@contextmanager
def progress_context(
    description: str,
    total: int | None = None,
) -> Generator[Any, None, None]:
    """
    Context manager that yields a callable ``advance(n=1)`` to increment
    a progress bar.  Falls back to a simple counter when Rich is absent.

    Usage::

        with progress_context("Verifying packages", total=len(pkgs)) as advance:
            for pkg in pkgs:
                process(pkg)
                advance()
    """
    if _RICH and total is not None and total > 1:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=40),
            MofNCompleteColumn(),
            TimeElapsedColumn(),
            console=_console,
            transient=False,
        ) as prog:
            task = prog.add_task(description, total=total)
            def _advance(n: int = 1) -> None:
                prog.advance(task, n)
            yield _advance
    else:
        # Plain fallback — just yield a no-op advancer
        def _advance(n: int = 1) -> None:  # type: ignore[misc]
            pass
        yield _advance


def identity_report(result: Any) -> None:
    """
    Print a structured identity validation report from an IdentityResult.
    This replaces the ``print_identity_report`` function in identity.py.
    """
    status_label = "PASS" if result.passed else "FAIL"
    passed = result.passed

    if _RICH:
        colour = "green" if passed else "red"
        _console.print()
        _console.rule(
            f"[bold]Repository Identity Validation  "
            f"[{colour}]{status_label}[/{colour}][/bold]"
        )
    else:
        print(f"\n{'=' * 70}")
        print(f"REPOSITORY IDENTITY VALIDATION  [{status_label}]")
        print(f"{'=' * 70}")

    for check_name, check_status in result.checks.items():
        check_line(check_name, check_status)

    if result.warnings:
        if _RICH:
            _console.print(f"\n  [yellow]Warnings ({len(result.warnings)}):[/yellow]")
        else:
            print(f"\n  Warnings ({len(result.warnings)}):")
        for w in result.warnings:
            for line in w.splitlines():
                warn(line)

    if result.errors:
        if _RICH:
            _console.print(f"\n  [red]Errors ({len(result.errors)}):[/red]")
        else:
            print(f"\n  Errors ({len(result.errors)}):")
        for e in result.errors:
            for line in e.splitlines():
                error(line)

    if _RICH:
        _console.rule(style="dim")
    else:
        print(f"{'=' * 70}")
