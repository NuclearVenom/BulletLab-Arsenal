"""
report.py - Master report JSON generator
"""
import json
from datetime import datetime, timezone
from pathlib import Path

def write_master_report(results: list[dict], repo_root: Path) -> None:
    report = {
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "total": len(results),
        "passed": sum(1 for r in results if r["final_status"] == "PASS"),
        "founder_review": sum(1 for r in results if r["final_status"] == "FOUNDER_REVIEW"),
        "failed": sum(1 for r in results if r["final_status"] == "FAIL"),
        "packages": results,
    }
    report_path = repo_root / "verification_run_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"\n  Master report: {report_path}")
