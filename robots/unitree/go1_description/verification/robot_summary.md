# Verification Report: Go1 Description

> **Overall Status:** FAIL
> **Verified on:** 2026-07-12T08:27:19.031023+00:00
> **BulletLab version:** 0.2.1

## Description

The go1_description package

## Model: go1 (`go1`)

**Entrypoint:** `urdf/go1.urdf`

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
| Width (X) | 0.5166 |
| Depth (Y) | 0.2995 |
| Height (Z)| 0.504 |

**Links:** 46  |  **Joints:** 45  |  **Controllable:** 12

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| floating_base | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| imu_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FR_hip_joint | revolute | -0.863 | 0.863 | 23.7 | 30.1 |
| FR_thigh_joint | revolute | -0.686 | 4.501 | 23.7 | 30.1 |
| FR_calf_joint | revolute | -2.818 | -0.888 | 35.5 | 20.1 |
| FR_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FR_calf_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FR_thigh_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FR_hip_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_hip_joint | revolute | -0.863 | 0.863 | 23.7 | 30.1 |
| FL_thigh_joint | revolute | -0.686 | 4.501 | 23.7 | 30.1 |
| FL_calf_joint | revolute | -2.818 | -0.888 | 35.5 | 20.1 |
| FL_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_calf_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_thigh_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_hip_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_hip_joint | revolute | -0.863 | 0.863 | 23.7 | 30.1 |
| RR_thigh_joint | revolute | -0.686 | 4.501 | 23.7 | 30.1 |
| RR_calf_joint | revolute | -2.818 | -0.888 | 35.5 | 20.1 |
| RR_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_calf_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_thigh_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_hip_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_hip_joint | revolute | -0.863 | 0.863 | 23.7 | 30.1 |
| RL_thigh_joint | revolute | -0.686 | 4.501 | 23.7 | 30.1 |
| RL_calf_joint | revolute | -2.818 | -0.888 | 35.5 | 20.1 |
| RL_foot_fixed | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_calf_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_thigh_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_hip_rotor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| camera_joint_face | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| camera_optical_joint_face | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| camera_joint_chin | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| camera_optical_joint_chin | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| camera_joint_left | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| camera_optical_joint_left | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| camera_laserscan_joint_left | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| camera_joint_right | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| camera_optical_joint_right | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| camera_laserscan_joint_right | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| camera_joint_rearDown | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| camera_optical_joint_rearDown | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| ultraSound_joint_left | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| ultraSound_joint_right | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| ultraSound_joint_face | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/go1/front.png`
- `screenshots/go1/rear.png`
- `screenshots/go1/left.png`
- `screenshots/go1/right.png`
- `screenshots/go1/top.png`
- `screenshots/go1/perspective.png`
- `screenshots/go1/isometric.png`

## Model: robot (`robot`)

**Entrypoint:** `urdf/robot.urdf`

**Status:** FAIL

### Verification Checks

| Check          | Result |
|----------------|--------|
| Loading        | N/A |
| Stability      | N/A |
| Joint Exercise | N/A |

### Dimensions

| Axis      | Size (m) |
|-----------|----------|
| Width (X) | N/A |
| Depth (Y) | N/A |
| Height (Z)| N/A |

**Links:** 0  |  **Joints:** 0  |  **Controllable:** 0

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._