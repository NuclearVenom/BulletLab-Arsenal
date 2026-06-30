# Verification Report: BLem1

> **Overall Status:** PASS
> **Verified on:** 2026-06-29T10:03:06.024328+00:00
> **BulletLab version:** 0.1.4

## Description

BLem1 (BulletLab Example Model 1) is a four-wheeled rover with folding legs and a pan-tilt head.

## Model: BLem1 (`default`)

**Entrypoint:** `urdf/BLem1.urdf`

**Status:** PASS

### Verification Checks

| Check          | Result |
|----------------|--------|
| Loading        | PASS |
| Stability      | PASS |
| Joint Exercise | PASS |

### Dimensions

| Axis      | Size (m) |
|-----------|----------|
| Width (X) | 0.596 |
| Depth (Y) | 0.7228 |
| Height (Z)| 0.6503 |

**Links:** 11  |  **Joints:** 10  |  **Controllable:** 10

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| neck_yaw | revolute | 0.000 | -1.000 | 0.0 | 0.0 |
| head_pitch | revolute | -0.500 | 0.500 | 100.0 | 100.0 |
| front_right_leg | revolute | 0.000 | -1.000 | 0.0 | 0.0 |
| front_right_wheel | revolute | 0.000 | -1.000 | 0.0 | 0.0 |
| front_left_leg | revolute | 0.000 | -1.000 | 0.0 | 0.0 |
| front_left_wheel | revolute | 0.000 | -1.000 | 0.0 | 0.0 |
| rear_right_leg | revolute | 0.000 | -1.000 | 0.0 | 0.0 |
| rear_right_wheel | revolute | 0.000 | -1.000 | 0.0 | 0.0 |
| rear_left_leg | revolute | 0.000 | -1.000 | 0.0 | 0.0 |
| rear_left_wheel | revolute | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/default/front.png`
- `screenshots/default/rear.png`
- `screenshots/default/left.png`
- `screenshots/default/right.png`
- `screenshots/default/top.png`
- `screenshots/default/perspective.png`
- `screenshots/default/isometric.png`

---
_This report was generated automatically by `scripts/verify_robot.py`. Do not edit manually._