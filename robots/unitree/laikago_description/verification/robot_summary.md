# Verification Report: Laikago Description

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:28:43.366724+00:00
> **BulletLab version:** 0.2.1

## Description

The laikago_description package

## Model: laikago (`laikago`)

**Entrypoint:** `urdf/laikago.urdf`

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
| Width (X) | 0.5636 |
| Depth (Y) | 0.379 |
| Height (Z)| 0.638 |

**Links:** 21  |  **Joints:** 20  |  **Controllable:** 12

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| FR_hip_joint | revolute | -1.047 | 0.873 | 20.0 | 52.4 |
| FR_hip_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FR_thigh_joint | revolute | -0.524 | 3.927 | 55.0 | 28.6 |
| FR_calf_joint | revolute | -2.775 | -0.611 | 55.0 | 28.6 |
| FR_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_hip_joint | revolute | -0.873 | 1.047 | 20.0 | 52.4 |
| FL_hip_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_thigh_joint | revolute | -0.524 | 3.927 | 55.0 | 28.6 |
| FL_calf_joint | revolute | -2.775 | -0.611 | 55.0 | 28.6 |
| FL_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_hip_joint | revolute | -1.047 | 0.873 | 20.0 | 52.4 |
| RR_hip_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_thigh_joint | revolute | -0.524 | 3.927 | 55.0 | 28.6 |
| RR_calf_joint | revolute | -2.775 | -0.611 | 55.0 | 28.6 |
| RR_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_hip_joint | revolute | -0.873 | 1.047 | 20.0 | 52.4 |
| RL_hip_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_thigh_joint | revolute | -0.524 | 3.927 | 55.0 | 28.6 |
| RL_calf_joint | revolute | -2.775 | -0.611 | 55.0 | 28.6 |
| RL_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/laikago/front.png`
- `screenshots/laikago/rear.png`
- `screenshots/laikago/left.png`
- `screenshots/laikago/right.png`
- `screenshots/laikago/top.png`
- `screenshots/laikago/perspective.png`
- `screenshots/laikago/isometric.png`

## Model: robot (`robot`)

**Entrypoint:** `urdf/robot.urdf`

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
| Width (X) | 0.002 |
| Depth (Y) | 0.002 |
| Height (Z)| 0.002 |

**Links:** 3  |  **Joints:** 2  |  **Controllable:** 0

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| floating_base | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| imu_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/robot/front.png`
- `screenshots/robot/rear.png`
- `screenshots/robot/left.png`
- `screenshots/robot/right.png`
- `screenshots/robot/top.png`
- `screenshots/robot/perspective.png`
- `screenshots/robot/isometric.png`

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._