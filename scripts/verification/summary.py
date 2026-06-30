"""
summary.py - Output summary table for BulletLab Arsenal verification.
"""

def print_summary(results: list[dict]) -> None:
    if not results:
        return
        
    col = max(len(r["package"]) for r in results) + 2
    print(f"\n{'=' * 70}")
    print("VERIFICATION SUMMARY")
    print(f"{'=' * 70}")
    print(f"  {'Package':<{col}}  {'L1':<6}  {'L2':<6}  {'Final'}")
    print(f"  {'-' * (col + 26)}")
    for r in results:
        l1_s = "PASS" if r["layer1"]["passed"] else "FAIL"
        if r["layer1"]["review"]:
            l1_s = "REVIEW"
        l2_d = r.get("layer2")
        l2_s = l2_d.get("overall", "SKIP") if l2_d else "SKIP"
        print(f"  {r['package']:<{col}}  {l1_s:<6}  {l2_s:<6}  {r['final_status']}")
    print(f"{'=' * 70}")

    total  = len(results)
    passed = sum(1 for r in results if r["final_status"] == "PASS")
    review = sum(1 for r in results if r["final_status"] == "FOUNDER_REVIEW")
    failed = sum(1 for r in results if r["final_status"] == "FAIL")

    print(f"\n  Total: {total}  |  Passed: {passed}  |  "
          f"Founder Review: {review}  |  Failed: {failed}")
