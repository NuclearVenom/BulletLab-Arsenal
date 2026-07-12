# Verification Report: Dex1 1

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:22:12.433392+00:00
> **BulletLab version:** 0.2.1

## Description

Here are the ROS simulation packages for Unitree robots, You can load robots and joint controllers in Gazebo, so you can perform low-level control (control the torque, position and angular velocity) of the robot joints. Please be aware that the Gazebo simulation cannot do high-level control, namely 

## Model: dex1 1 (`dex1_1`)

**Entrypoint:** `urdf/dex1_1.urdf`

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
| Width (X) | 0.0871 |
| Depth (Y) | 0.1533 |
| Height (Z)| 0.13 |

**Links:** 7  |  **Joints:** 6  |  **Controllable:** 2

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| Joint1_1 | prismatic | -0.020 | 0.025 | 20.0 | 0.2 |
| Joint1_2 | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| Joint1_3 | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| Joint2_1 | prismatic | -0.020 | 0.025 | 20.0 | 0.2 |
| Joint2_2 | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| Joint2_3 | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/dex1_1/front.png`
- `screenshots/dex1_1/rear.png`
- `screenshots/dex1_1/left.png`
- `screenshots/dex1_1/right.png`
- `screenshots/dex1_1/top.png`
- `screenshots/dex1_1/perspective.png`
- `screenshots/dex1_1/isometric.png`

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._