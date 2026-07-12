# Verification Report: B1 Description

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:21:30.161567+00:00
> **BulletLab version:** 0.2.1

## Description

The b1_description package

## Model: b1 (`b1`)

**Entrypoint:** `urdf/b1.urdf`

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
| Width (X) | 0.9803 |
| Depth (Y) | 0.4775 |
| Height (Z)| 0.8375 |

**Links:** 36  |  **Joints:** 35  |  **Controllable:** 12

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| floating_base | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| imu_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_side_camera_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| right_side_camera_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| head_camera_1_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| head_camera_2_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| tail_camera_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FR_hip_joint | revolute | -0.750 | 0.750 | 91.0 | 19.7 |
| FR_thigh_joint | revolute | -1.000 | 3.500 | 93.3 | 23.3 |
| FR_calf_joint | revolute | -2.600 | -0.600 | 140.0 | 15.6 |
| FR_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FR_calf_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FR_thigh_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FR_hip_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_hip_joint | revolute | -0.750 | 0.750 | 91.0 | 19.7 |
| FL_thigh_joint | revolute | -1.000 | 3.500 | 93.3 | 23.3 |
| FL_calf_joint | revolute | -2.600 | -0.600 | 140.0 | 15.6 |
| FL_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_calf_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_thigh_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_hip_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_hip_joint | revolute | -0.750 | 0.750 | 91.0 | 19.7 |
| RR_thigh_joint | revolute | -1.000 | 3.500 | 93.3 | 23.3 |
| RR_calf_joint | revolute | -2.600 | -0.600 | 140.0 | 15.6 |
| RR_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_calf_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_thigh_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_hip_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_hip_joint | revolute | -0.750 | 0.750 | 91.0 | 19.7 |
| RL_thigh_joint | revolute | -1.000 | 3.500 | 93.3 | 23.3 |
| RL_calf_joint | revolute | -2.600 | -0.600 | 140.0 | 15.6 |
| RL_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_calf_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_thigh_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_hip_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/b1/front.png`
- `screenshots/b1/rear.png`
- `screenshots/b1/left.png`
- `screenshots/b1/right.png`
- `screenshots/b1/top.png`
- `screenshots/b1/perspective.png`
- `screenshots/b1/isometric.png`

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
| Width (X) | 0.9783 |
| Depth (Y) | 0.3074 |
| Height (Z)| 0.2085 |

**Links:** 8  |  **Joints:** 7  |  **Controllable:** 0

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| floating_base | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| imu_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_side_camera_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| right_side_camera_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| head_camera_1_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| head_camera_2_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| tail_camera_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

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