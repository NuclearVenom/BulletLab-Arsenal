"""
robot.py — BulletLab Arsenal Layer 2 Robot Verification

This is the second layer of the two-layer quality pipeline.
It answers: "Does every model in this package actually work in BulletLab?"
"""

from __future__ import annotations

import math
import struct
import traceback
import zlib
import json
from datetime import datetime, timezone
from pathlib import Path

_PYBULLET_AVAILABLE = False
try:
    import pybullet as p
    import pybullet_data
    _PYBULLET_AVAILABLE = True
except ImportError:
    pass

_BULLETLAB_AVAILABLE = False
try:
    import bulletlab
    from bulletlab import Simulation, Robot
    BULLETLAB_VERSION = bulletlab.__version__
    _BULLETLAB_AVAILABLE = True
except ImportError:
    BULLETLAB_VERSION = "unknown"

CAMERA_VIEWS: list[tuple[str, float, float]] = [
    ("front",       0.0,   -20.0),
    ("rear",      180.0,   -20.0),
    ("left",       90.0,   -20.0),
    ("right",     270.0,   -20.0),
    ("top",         0.0,   -89.0),
    ("perspective", 45.0,  -30.0),
    ("isometric",  35.26,  -30.0),
]

PLACEMENT_MARGIN  = 0.005
STABILITY_STEPS   = 60

def _write_png(path: Path, rgba_bytes: bytes, width: int, height: int) -> None:
    def chunk(tag: bytes, data: bytes) -> bytes:
        crc = struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        return struct.pack(">I", len(data)) + tag + data + crc

    raw_rows = b""
    row = width * 4
    for y in range(height):
        raw_rows += b"\x00" + rgba_bytes[y * row:(y + 1) * row]

    ihdr = struct.pack(">II", width, height) + bytes([8, 6, 0, 0, 0])
    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", ihdr)
        + chunk(b"IDAT", zlib.compress(raw_rows, 6))
        + chunk(b"IEND", b"")
    )
    path.write_bytes(png)

def _full_aabb(body_id: int, client_id: int) -> tuple[list[float], list[float]]:
    n = p.getNumJoints(body_id, physicsClientId=client_id)
    lo, hi = p.getAABB(body_id, -1, physicsClientId=client_id)
    lo, hi = list(lo), list(hi)
    for i in range(n):
        lmin, lmax = p.getAABB(body_id, i, physicsClientId=client_id)
        for ax in range(3):
            lo[ax] = min(lo[ax], lmin[ax])
            hi[ax] = max(hi[ax], lmax[ax])
    return lo, hi

def _has_nan(vals: list[float]) -> bool:
    return any(math.isnan(v) or math.isinf(v) for v in vals)

def _render(
    client_id: int,
    view_name: str,
    yaw: float,
    pitch: float,
    target: list[float],
    distance: float,
    out_path: Path,
    width: int,
    height: int,
) -> dict:
    view = p.computeViewMatrixFromYawPitchRoll(
        cameraTargetPosition=target,
        distance=distance,
        yaw=yaw, pitch=pitch, roll=0,
        upAxisIndex=2,
        physicsClientId=client_id,
    )
    proj = p.computeProjectionMatrixFOV(
        fov=60.0, aspect=width / height,
        nearVal=0.01, farVal=100.0,
        physicsClientId=client_id,
    )
    _, _, rgba, _, _ = p.getCameraImage(
        width=width, height=height,
        viewMatrix=view, projectionMatrix=proj,
        renderer=p.ER_TINY_RENDERER,
        physicsClientId=client_id,
    )
    rgba_bytes = bytes(rgba) if isinstance(rgba, (list, tuple)) else bytes(rgba)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    _write_png(out_path, rgba_bytes, width, height)
    return {
        "view": view_name,
        "path": str(out_path.name),
        "camera": {
            "distance": round(distance, 4),
            "yaw": yaw, "pitch": pitch,
            "target": [round(v, 4) for v in target],
        },
    }

def _exercise_joint(body_id: int, idx: int, info: dict, client_id: int) -> dict:
    lo, hi = info["lower_limit"], info["upper_limit"]
    if lo == hi:
        return {"joint_name": info["name"], "status": "skipped",
                "reason": "lower_limit == upper_limit"}
    center = (lo + hi) / 2.0
    errs = []
    for target, label in [(lo, "min"), (center, "center"), (hi, "max")]:
        try:
            p.resetJointState(body_id, idx, targetValue=target,
                              physicsClientId=client_id)
            state = p.getJointState(body_id, idx, physicsClientId=client_id)
            if math.isnan(state[0]):
                errs.append(f"NaN at target={label}")
        except Exception as exc:
            errs.append(f"Exception at target={label}: {exc}")
    try:
        p.resetJointState(body_id, idx, targetValue=0.0,
                          physicsClientId=client_id)
    except Exception:
        pass
    return {"joint_name": info["name"],
            "status": "PASS" if not errs else "FAIL",
            "errors": errs}

def _verify_model(
    pkg_dir: Path,
    model: dict,
    screenshots_dir: Path,
    width: int,
    height: int,
) -> dict:
    model_id = model.get("id", "unknown")
    entrypoint = model.get("entrypoint", "")
    urdf_path = pkg_dir / entrypoint

    result: dict = {
        "model_id": model_id,
        "model_display_name": model.get("display_name", model_id),
        "entrypoint": entrypoint,
        "loading": {},
        "placement": {},
        "dimensions_meters": {},
        "links": [],
        "joints": [],
        "joint_exercise": [],
        "stability": {},
        "screenshots": [],
        "summary": {},
    }

    if not urdf_path.is_file():
        result["loading"] = {"status": "FAIL",
                             "error": f"URDF not found: {entrypoint}"}
        result["summary"] = {"overall": "FAIL"}
        return result

    sim = Simulation(mode="direct", gravity=(0.0, 0.0, 0.0),
                     timestep=1.0 / 240.0)
    sim.start()
    client_id = sim.client_id

    try:
        try:
            robot = Robot.load(str(urdf_path), sim=sim,
                               position=(0.0, 0.0, 0.0), name=model_id)
        except Exception as exc:
            result["loading"] = {
                "status": "FAIL",
                "error": str(exc),
                "traceback": traceback.format_exc(),
            }
            result["summary"] = {"overall": "FAIL"}
            return result

        result["loading"] = {"status": "PASS"}
        body_id = robot.body_id

        for _ in range(10):
            p.stepSimulation(physicsClientId=client_id)

        aabb_min, aabb_max = _full_aabb(body_id, client_id)
        if _has_nan(aabb_min + aabb_max):
            result["loading"] = {"status": "FAIL",
                                 "error": "AABB contains NaN immediately after load"}
            result["summary"] = {"overall": "FAIL"}
            return result

        lift = -aabb_min[2] + PLACEMENT_MARGIN
        pos, orn = p.getBasePositionAndOrientation(body_id,
                                                    physicsClientId=client_id)
        new_pos = (pos[0], pos[1], pos[2] + lift)
        p.resetBasePositionAndOrientation(body_id, list(new_pos), list(orn),
                                          physicsClientId=client_id)
        aabb_min, aabb_max = _full_aabb(body_id, client_id)

        wx = round(aabb_max[0] - aabb_min[0], 4)
        dy = round(aabb_max[1] - aabb_min[1], 4)
        hz = round(aabb_max[2] - aabb_min[2], 4)
        cx = (aabb_min[0] + aabb_max[0]) / 2
        cy = (aabb_min[1] + aabb_max[1]) / 2
        cz = (aabb_min[2] + aabb_max[2]) / 2
        target = [cx, cy, cz]
        cam_dist = max(1.0, math.sqrt(wx**2 + dy**2 + hz**2) * 2.5)

        result["placement"] = {
            "final_base_position": list(new_pos),
            "lift_applied_meters": round(lift, 6),
        }
        result["dimensions_meters"] = {
            "width_x": wx, "depth_y": dy, "height_z": hz,
        }

        body_info = p.getBodyInfo(body_id, physicsClientId=client_id)
        base_name = (body_info[0].decode("utf-8")
                     if isinstance(body_info[0], bytes) else str(body_info[0]))
        links = [{"name": base_name, "index": -1, "parent": None}]
        n_joints = p.getNumJoints(body_id, physicsClientId=client_id)
        for i in range(n_joints):
            jinfo = p.getJointInfo(body_id, i, physicsClientId=client_id)
            lname = (jinfo[12].decode("utf-8")
                     if isinstance(jinfo[12], bytes) else str(jinfo[12]))
            pidx = jinfo[16]
            if pidx == -1:
                pname = base_name
            else:
                pinfo = p.getJointInfo(body_id, pidx, physicsClientId=client_id)
                pname = (pinfo[12].decode("utf-8")
                         if isinstance(pinfo[12], bytes) else str(pinfo[12]))
            links.append({"name": lname, "index": i, "parent": pname})
        result["links"] = links

        JTYPE = {
            p.JOINT_REVOLUTE:  "revolute",
            p.JOINT_PRISMATIC: "prismatic",
            p.JOINT_SPHERICAL: "spherical",
            p.JOINT_PLANAR:    "planar",
            p.JOINT_FIXED:     "fixed",
        }
        joints = []
        for i in range(n_joints):
            jinfo = p.getJointInfo(body_id, i, physicsClientId=client_id)
            jname = (jinfo[1].decode("utf-8")
                     if isinstance(jinfo[1], bytes) else str(jinfo[1]))
            joints.append({
                "name": jname, "index": i,
                "type": JTYPE.get(jinfo[2], f"unknown({jinfo[2]})"),
                "lower_limit": float(jinfo[8]),
                "upper_limit": float(jinfo[9]),
                "max_force": float(jinfo[10]),
                "max_velocity": float(jinfo[11]),
            })
        result["joints"] = joints

        ex_results = []
        for ji in joints:
            if ji["type"] in ("revolute", "prismatic"):
                ex_results.append(
                    _exercise_joint(body_id, ji["index"], ji, client_id)
                )
        result["joint_exercise"] = ex_results
        ex_failures = [r for r in ex_results if r.get("status") == "FAIL"]

        ab_min, ab_max = _full_aabb(body_id, client_id)
        for _ in range(STABILITY_STEPS):
            p.stepSimulation(physicsClientId=client_id)
        aa_min, aa_max = _full_aabb(body_id, client_id)
        nan_det = _has_nan(ab_min + ab_max + aa_min + aa_max)
        stability_ok = not nan_det
        result["stability"] = {
            "steps_run": STABILITY_STEPS,
            "nan_detected": nan_det,
            "status": "PASS" if stability_ok else "FAIL",
        }

        model_screens_dir = screenshots_dir / model_id
        screen_records = []
        for view_name, yaw, pitch in CAMERA_VIEWS:
            out_png = model_screens_dir / f"{view_name}.png"
            try:
                rec = _render(client_id, view_name, yaw, pitch, target,
                              cam_dist, out_png, width, height)
                screen_records.append(rec)
            except Exception as exc:
                screen_records.append({"view": view_name, "path": None,
                                       "error": str(exc)})
        result["screenshots"] = screen_records

        loading_ok   = result["loading"]["status"] == "PASS"
        stability_ok2 = result["stability"]["status"] == "PASS"
        exercise_ok  = len(ex_failures) == 0
        overall      = loading_ok and stability_ok2 and exercise_ok

        result["summary"] = {
            "loading":        "PASS" if loading_ok   else "FAIL",
            "stability":      "PASS" if stability_ok2 else "FAIL",
            "joint_exercise": "PASS" if exercise_ok  else "FAIL",
            "overall":        "PASS" if overall       else "FAIL",
        }

    finally:
        sim.stop()

    return result

def verify_robot(
    package_dir: Path,
    screenshot_width: int = 1920,
    screenshot_height: int = 1080,
) -> dict:
    pkg_name = package_dir.name
    metadata_path = package_dir / "metadata.json"
    verification_dir = package_dir / "verification"
    screenshots_dir = verification_dir / "screenshots"

    if not _BULLETLAB_AVAILABLE or not _PYBULLET_AVAILABLE:
        missing = []
        if not _BULLETLAB_AVAILABLE:
            missing.append("bulletlab")
        if not _PYBULLET_AVAILABLE:
            missing.append("pybullet")
        raise RuntimeError(
            f"Layer 3 (BulletLab simulation) requires: {', '.join(missing)}.\n"
            "Install with:  pip install bulletlab pybullet\n"
            "Or skip simulation with:  arsenal verify <path> --skip-simulation"
        )

    if not metadata_path.is_file():
        return {"_passed": False, "package": pkg_name,
                "error": "metadata.json not found."}

    with open(metadata_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    models_spec = metadata.get("models", [])
    if not models_spec:
        return {"_passed": False, "package": pkg_name,
                "error": "metadata.json contains no models."}

    verification_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    package_report: dict = {
        "package": pkg_name,
        "verification_timestamp": datetime.now(timezone.utc).isoformat(),
        "bulletlab_version": BULLETLAB_VERSION,
        "models": [],
    }

    all_passed = True

    for model_spec in models_spec:
        model_result = _verify_model(
            pkg_dir=package_dir,
            model=model_spec,
            screenshots_dir=screenshots_dir,
            width=screenshot_width,
            height=screenshot_height,
        )

        overall = model_result.get("summary", {}).get("overall", "FAIL")
        if overall != "PASS":
            all_passed = False

        package_report["models"].append(model_result)

    package_report["_passed"] = all_passed
    package_report["overall"] = "PASS" if all_passed else "FAIL"

    serialisable = {k: v for k, v in package_report.items()
                    if not k.startswith("_")}

    report_path = verification_dir / "verification_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(serialisable, f, indent=2)

    summary_path = verification_dir / "robot_summary.md"
    _write_summary_md(summary_path, pkg_name, package_report, metadata)

    return package_report

def _write_summary_md(
    path: Path,
    pkg_name: str,
    report: dict,
    metadata: dict,
) -> None:
    overall = report.get("overall", "UNKNOWN")
    display_name = metadata.get("display_name", pkg_name)
    description = metadata.get("description", "")
    timestamp = report.get("verification_timestamp", "unknown")
    bl_ver = report.get("bulletlab_version", "unknown")

    lines = [
        f"# Verification Report: {display_name}",
        "",
        f"> **Overall Status:** {overall}",
        f"> **Verified on:** {timestamp}",
        f"> **BulletLab version:** {bl_ver}",
        "",
        "## Description",
        "",
        description,
        "",
    ]

    for m in report.get("models", []):
        mid = m.get("model_id", "?")
        mdisp = m.get("model_display_name", mid)
        ep = m.get("entrypoint", "?")
        s = m.get("summary", {})
        dims = m.get("dimensions_meters", {})
        links = m.get("links", [])
        joints = m.get("joints", [])

        lines += [
            f"## Model: {mdisp} (`{mid}`)",
            "",
            f"**Entrypoint:** `{ep}`",
            "",
            f"**Status:** {s.get('overall', 'UNKNOWN')}",
            "",
            "### Verification Checks",
            "",
            "| Check          | Result |",
            "|----------------|--------|",
            f"| Loading        | {s.get('loading', 'N/A')} |",
            f"| Stability      | {s.get('stability', 'N/A')} |",
            f"| Joint Exercise | {s.get('joint_exercise', 'N/A')} |",
            "",
            "### Dimensions",
            "",
            "| Axis      | Size (m) |",
            "|-----------|----------|",
            f"| Width (X) | {dims.get('width_x', 'N/A')} |",
            f"| Depth (Y) | {dims.get('depth_y', 'N/A')} |",
            f"| Height (Z)| {dims.get('height_z', 'N/A')} |",
            "",
            f"**Links:** {len(links)}  |  **Joints:** {len(joints)}  "
            f"|  **Controllable:** {sum(1 for j in joints if j['type'] != 'fixed')}",
            "",
            "### Joint Summary",
            "",
            "| Name | Type | Lower | Upper | Max Force | Max Vel |",
            "|------|------|-------|-------|-----------|---------|",
        ]
        for j in joints:
            lines.append(
                f"| {j['name']} | {j['type']} | {j['lower_limit']:.3f} | "
                f"{j['upper_limit']:.3f} | {j['max_force']:.1f} | "
                f"{j['max_velocity']:.1f} |"
            )

        screens = m.get("screenshots", [])
        if screens:
            lines += ["", "### Screenshots", ""]
            for sc in screens:
                mid_sc = m.get("model_id", "unknown")
                if sc.get("path"):
                    lines.append(f"- `screenshots/{mid_sc}/{sc['path']}`")
                else:
                    lines.append(f"- `{sc.get('view','?')}` — render failed")

        lines.append("")

    lines += [
        "---",
        "_This report was generated automatically by BulletLab Arsenal verification. "
        "Do not edit manually._",
    ]

    path.write_text("\n".join(lines), encoding="utf-8")
