# Verification Report: Dex2 5

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:22:27.868964+00:00
> **BulletLab version:** 0.2.1

## Description

Here are the ROS simulation packages for Unitree robots, You can load robots and joint controllers in Gazebo, so you can perform low-level control (control the torque, position and angular velocity) of the robot joints. Please be aware that the Gazebo simulation cannot do high-level control, namely 

## Model: Left Hand (`left_hand`)

**Entrypoint:** `urdf/Left_Hand.urdf`

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
| Width (X) | 0.157 |
| Depth (Y) | 0.1034 |
| Height (Z)| 0.0762 |

**Links:** 11  |  **Joints:** 10  |  **Controllable:** 10

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| left_11_joint | revolute | 0.000 | 0.733 | 2.5 | 6.0 |
| left_12_joint | revolute | 0.000 | 1.833 | 2.5 | 6.0 |
| left_21_joint | revolute | -1.536 | 0.000 | 0.5 | 8.0 |
| left_22_joint | revolute | -1.833 | 0.000 | 0.5 | 8.0 |
| left_31_joint | revolute | -1.536 | 0.000 | 0.5 | 8.0 |
| left_32_joint | revolute | -1.833 | 0.000 | 0.5 | 8.0 |
| left_41_joint | revolute | -1.536 | 0.000 | 0.5 | 8.0 |
| left_42_joint | revolute | -1.833 | 0.000 | 0.5 | 8.0 |
| left_51_joint | revolute | -1.536 | 0.000 | 0.5 | 8.0 |
| left_52_joint | revolute | -1.833 | 0.000 | 0.5 | 8.0 |

### Screenshots

- `screenshots/left_hand/front.png`
- `screenshots/left_hand/rear.png`
- `screenshots/left_hand/left.png`
- `screenshots/left_hand/right.png`
- `screenshots/left_hand/top.png`
- `screenshots/left_hand/perspective.png`
- `screenshots/left_hand/isometric.png`

## Model: Left Hand G1 5010 Wrist (`left_hand_g1_5010_wrist`)

**Entrypoint:** `urdf/Left_Hand_G1_5010_Wrist.urdf`

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
| Width (X) | 0.2185 |
| Depth (Y) | 0.112 |
| Height (Z)| 0.0762 |

**Links:** 12  |  **Joints:** 11  |  **Controllable:** 10

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| left_0_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_11_joint | revolute | 0.000 | 0.733 | 2.5 | 6.0 |
| left_12_joint | revolute | 0.000 | 1.833 | 2.5 | 6.0 |
| left_21_joint | revolute | -1.536 | 0.000 | 0.5 | 8.0 |
| left_22_joint | revolute | -1.833 | 0.000 | 0.5 | 8.0 |
| left_31_joint | revolute | -1.536 | 0.000 | 0.5 | 8.0 |
| left_32_joint | revolute | -1.833 | 0.000 | 0.5 | 8.0 |
| left_41_joint | revolute | -1.536 | 0.000 | 0.5 | 8.0 |
| left_42_joint | revolute | -1.833 | 0.000 | 0.5 | 8.0 |
| left_51_joint | revolute | -1.536 | 0.000 | 0.5 | 8.0 |
| left_52_joint | revolute | -1.833 | 0.000 | 0.5 | 8.0 |

### Screenshots

- `screenshots/left_hand_g1_5010_wrist/front.png`
- `screenshots/left_hand_g1_5010_wrist/rear.png`
- `screenshots/left_hand_g1_5010_wrist/left.png`
- `screenshots/left_hand_g1_5010_wrist/right.png`
- `screenshots/left_hand_g1_5010_wrist/top.png`
- `screenshots/left_hand_g1_5010_wrist/perspective.png`
- `screenshots/left_hand_g1_5010_wrist/isometric.png`

## Model: Right Hand (`right_hand`)

**Entrypoint:** `urdf/Right_Hand.urdf`

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
| Width (X) | 0.157 |
| Depth (Y) | 0.1034 |
| Height (Z)| 0.0762 |

**Links:** 11  |  **Joints:** 10  |  **Controllable:** 10

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| right_11_joint | revolute | -0.733 | 0.000 | 2.5 | 6.0 |
| right_12_joint | revolute | -1.833 | 0.000 | 2.5 | 6.0 |
| right_21_joint | revolute | 0.000 | 1.536 | 0.5 | 8.0 |
| right_22_joint | revolute | 0.000 | 1.833 | 0.5 | 8.0 |
| right_31_joint | revolute | 0.000 | 1.536 | 0.5 | 8.0 |
| right_32_joint | revolute | 0.000 | 1.833 | 0.5 | 8.0 |
| right_41_joint | revolute | 0.000 | 1.536 | 0.5 | 8.0 |
| right_42_joint | revolute | 0.000 | 1.833 | 0.5 | 8.0 |
| right_51_joint | revolute | 0.000 | 1.536 | 0.5 | 8.0 |
| right_52_joint | revolute | 0.000 | 1.833 | 0.5 | 8.0 |

### Screenshots

- `screenshots/right_hand/front.png`
- `screenshots/right_hand/rear.png`
- `screenshots/right_hand/left.png`
- `screenshots/right_hand/right.png`
- `screenshots/right_hand/top.png`
- `screenshots/right_hand/perspective.png`
- `screenshots/right_hand/isometric.png`

## Model: Right Hand G1 5010 Wrist (`right_hand_g1_5010_wrist`)

**Entrypoint:** `urdf/Right_Hand_G1_5010_Wrist.urdf`

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
| Width (X) | 0.2185 |
| Depth (Y) | 0.112 |
| Height (Z)| 0.0762 |

**Links:** 12  |  **Joints:** 11  |  **Controllable:** 10

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| right_0_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| right_11_joint | revolute | -0.733 | 0.000 | 2.5 | 6.0 |
| right_12_joint | revolute | -1.833 | 0.000 | 2.5 | 6.0 |
| right_21_joint | revolute | 0.000 | 1.536 | 0.5 | 8.0 |
| right_22_joint | revolute | 0.000 | 1.833 | 0.5 | 8.0 |
| right_31_joint | revolute | 0.000 | 1.536 | 0.5 | 8.0 |
| right_32_joint | revolute | 0.000 | 1.833 | 0.5 | 8.0 |
| right_41_joint | revolute | 0.000 | 1.536 | 0.5 | 8.0 |
| right_42_joint | revolute | 0.000 | 1.833 | 0.5 | 8.0 |
| right_51_joint | revolute | 0.000 | 1.536 | 0.5 | 8.0 |
| right_52_joint | revolute | 0.000 | 1.833 | 0.5 | 8.0 |

### Screenshots

- `screenshots/right_hand_g1_5010_wrist/front.png`
- `screenshots/right_hand_g1_5010_wrist/rear.png`
- `screenshots/right_hand_g1_5010_wrist/left.png`
- `screenshots/right_hand_g1_5010_wrist/right.png`
- `screenshots/right_hand_g1_5010_wrist/top.png`
- `screenshots/right_hand_g1_5010_wrist/perspective.png`
- `screenshots/right_hand_g1_5010_wrist/isometric.png`

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._