# Verification Report: Dex3 1

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:23:33.007266+00:00
> **BulletLab version:** 0.2.1

## Description

Here are the ROS simulation packages for Unitree robots, You can load robots and joint controllers in Gazebo, so you can perform low-level control (control the torque, position and angular velocity) of the robot joints. Please be aware that the Gazebo simulation cannot do high-level control, namely 

## Model: dex3 1 l (`dex3_1_l`)

**Entrypoint:** `urdf/dex3_1_l.urdf`

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
| Width (X) | 0.1815 |
| Depth (Y) | 0.1445 |
| Height (Z)| 0.0938 |

**Links:** 8  |  **Joints:** 7  |  **Controllable:** 7

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| left_hand_thumb_0_joint | revolute | -1.047 | 1.047 | 2.5 | 3.1 |
| left_hand_thumb_1_joint | revolute | -0.611 | 1.047 | 1.4 | 12.0 |
| left_hand_thumb_2_joint | revolute | 0.000 | 1.745 | 1.4 | 12.0 |
| left_hand_middle_0_joint | revolute | -1.571 | 0.000 | 1.4 | 12.0 |
| left_hand_middle_1_joint | revolute | -1.745 | 0.000 | 1.4 | 12.0 |
| left_hand_index_0_joint | revolute | -1.571 | 0.000 | 1.4 | 12.0 |
| left_hand_index_1_joint | revolute | -1.745 | 0.000 | 1.4 | 12.0 |

### Screenshots

- `screenshots/dex3_1_l/front.png`
- `screenshots/dex3_1_l/rear.png`
- `screenshots/dex3_1_l/left.png`
- `screenshots/dex3_1_l/right.png`
- `screenshots/dex3_1_l/top.png`
- `screenshots/dex3_1_l/perspective.png`
- `screenshots/dex3_1_l/isometric.png`

## Model: dex3 1 r (`dex3_1_r`)

**Entrypoint:** `urdf/dex3_1_r.urdf`

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
| Width (X) | 0.1815 |
| Depth (Y) | 0.1445 |
| Height (Z)| 0.0938 |

**Links:** 8  |  **Joints:** 7  |  **Controllable:** 7

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| right_hand_thumb_0_joint | revolute | -1.047 | 1.047 | 2.5 | 3.1 |
| right_hand_thumb_1_joint | revolute | -1.047 | 0.611 | 1.4 | 12.0 |
| right_hand_thumb_2_joint | revolute | -1.745 | 0.000 | 1.4 | 12.0 |
| right_hand_middle_0_joint | revolute | 0.000 | 1.571 | 1.4 | 12.0 |
| right_hand_middle_1_joint | revolute | 0.000 | 1.745 | 1.4 | 12.0 |
| right_hand_index_0_joint | revolute | 0.000 | 1.571 | 1.4 | 12.0 |
| right_hand_index_1_joint | revolute | 0.000 | 1.745 | 1.4 | 12.0 |

### Screenshots

- `screenshots/dex3_1_r/front.png`
- `screenshots/dex3_1_r/rear.png`
- `screenshots/dex3_1_r/left.png`
- `screenshots/dex3_1_r/right.png`
- `screenshots/dex3_1_r/top.png`
- `screenshots/dex3_1_r/perspective.png`
- `screenshots/dex3_1_r/isometric.png`

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._