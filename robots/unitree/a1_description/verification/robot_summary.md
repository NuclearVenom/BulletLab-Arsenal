# Verification Report: A1 Description

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:20:19.657275+00:00
> **BulletLab version:** 0.2.1

## Description

The a1_description package

## Model: a1 (`a1`)

**Entrypoint:** `urdf/a1.urdf`

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
| Width (X) | 0.459 |
| Depth (Y) | 0.3016 |
| Height (Z)| 0.478 |

**Links:** 23  |  **Joints:** 22  |  **Controllable:** 12

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| floating_base | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| imu_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FR_hip_joint | revolute | -0.803 | 0.803 | 33.5 | 21.0 |
| FR_hip_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FR_thigh_joint | revolute | -1.047 | 4.189 | 33.5 | 21.0 |
| FR_calf_joint | revolute | -2.697 | -0.916 | 33.5 | 21.0 |
| FR_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_hip_joint | revolute | -0.803 | 0.803 | 33.5 | 21.0 |
| FL_hip_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_thigh_joint | revolute | -1.047 | 4.189 | 33.5 | 21.0 |
| FL_calf_joint | revolute | -2.697 | -0.916 | 33.5 | 21.0 |
| FL_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_hip_joint | revolute | -0.803 | 0.803 | 33.5 | 21.0 |
| RR_hip_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_thigh_joint | revolute | -1.047 | 4.189 | 33.5 | 21.0 |
| RR_calf_joint | revolute | -2.697 | -0.916 | 33.5 | 21.0 |
| RR_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_hip_joint | revolute | -0.803 | 0.803 | 33.5 | 21.0 |
| RL_hip_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_thigh_joint | revolute | -1.047 | 4.189 | 33.5 | 21.0 |
| RL_calf_joint | revolute | -2.697 | -0.916 | 33.5 | 21.0 |
| RL_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/a1/front.png`
- `screenshots/a1/rear.png`
- `screenshots/a1/left.png`
- `screenshots/a1/right.png`
- `screenshots/a1/top.png`
- `screenshots/a1/perspective.png`
- `screenshots/a1/isometric.png`

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