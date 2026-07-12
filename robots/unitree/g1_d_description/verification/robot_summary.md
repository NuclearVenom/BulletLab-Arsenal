# Verification Report: G1 D Description

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:25:17.220649+00:00
> **BulletLab version:** 0.2.1

## Description

Here are the ROS simulation packages for Unitree robots, You can load robots and joint controllers in Gazebo, so you can perform low-level control (control the torque, position and angular velocity) of the robot joints. Please be aware that the Gazebo simulation cannot do high-level control, namely 

## Model: g1 d (`g1_d`)

**Entrypoint:** `urdf/g1_d.urdf`

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
| Width (X) | 0.7441 |
| Depth (Y) | 0.529 |
| Height (Z)| 1.3274 |

**Links:** 41  |  **Joints:** 40  |  **Controllable:** 34

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| Left_Wheel_Joint | revolute | -3.142 | 3.142 | 8.0 | 100.0 |
| Right_Wheel_Joint | revolute | -3.142 | 3.142 | 8.0 | 100.0 |
| LZ_ot_Joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| LZ_mt_Joint | prismatic | 0.000 | 0.210 | 500.0 | 0.1 |
| LZ_it_Joint | prismatic | 0.000 | 0.210 | 500.0 | 0.1 |
| Pitching_Joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| Yaw_Joint | revolute | -0.044 | 2.356 | 80.0 | 5.0 |
| torso_Joint | revolute | -2.705 | 2.705 | 30.0 | 5.0 |
| logo_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| head_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_shoulder_pitch_joint | revolute | -3.089 | 2.670 | 25.0 | 37.0 |
| left_shoulder_roll_joint | revolute | -1.588 | 2.252 | 25.0 | 37.0 |
| left_shoulder_yaw_joint | revolute | -2.618 | 2.618 | 25.0 | 37.0 |
| left_elbow_joint | revolute | -1.047 | 2.094 | 25.0 | 37.0 |
| left_wrist_roll_joint | revolute | -1.972 | 1.972 | 25.0 | 37.0 |
| left_wrist_pitch_joint | revolute | -1.614 | 1.614 | 5.0 | 22.0 |
| left_wrist_yaw_joint | revolute | -1.614 | 1.614 | 5.0 | 22.0 |
| left_hand_palm_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_hand_thumb_0_joint | revolute | -1.047 | 1.047 | 2.5 | 6.9 |
| left_hand_thumb_1_joint | revolute | -0.724 | 1.047 | 1.4 | 12.0 |
| left_hand_thumb_2_joint | revolute | 0.000 | 1.745 | 1.4 | 12.0 |
| left_hand_middle_0_joint | revolute | -1.571 | 0.000 | 1.4 | 12.0 |
| left_hand_middle_1_joint | revolute | -1.745 | 0.000 | 1.4 | 12.0 |
| left_hand_index_0_joint | revolute | -1.571 | 0.000 | 1.4 | 12.0 |
| left_hand_index_1_joint | revolute | -1.745 | 0.000 | 1.4 | 12.0 |
| right_shoulder_pitch_joint | revolute | -3.089 | 2.670 | 25.0 | 37.0 |
| right_shoulder_roll_joint | revolute | -2.252 | 1.588 | 25.0 | 37.0 |
| right_shoulder_yaw_joint | revolute | -2.618 | 2.618 | 25.0 | 37.0 |
| right_elbow_joint | revolute | -1.047 | 2.094 | 25.0 | 37.0 |
| right_wrist_roll_joint | revolute | -1.972 | 1.972 | 25.0 | 37.0 |
| right_wrist_pitch_joint | revolute | -1.614 | 1.614 | 5.0 | 22.0 |
| right_wrist_yaw_joint | revolute | -1.614 | 1.614 | 5.0 | 22.0 |
| right_hand_palm_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| right_hand_thumb_0_joint | revolute | -1.047 | 1.047 | 2.5 | 6.9 |
| right_hand_thumb_1_joint | revolute | -1.047 | 0.724 | 1.4 | 12.0 |
| right_hand_thumb_2_joint | revolute | -1.745 | 0.000 | 1.4 | 12.0 |
| right_hand_middle_0_joint | revolute | 0.000 | 1.571 | 1.4 | 12.0 |
| right_hand_middle_1_joint | revolute | 0.000 | 1.745 | 1.4 | 12.0 |
| right_hand_index_0_joint | revolute | 0.000 | 1.571 | 1.4 | 12.0 |
| right_hand_index_1_joint | revolute | 0.000 | 1.745 | 1.4 | 12.0 |

### Screenshots

- `screenshots/g1_d/front.png`
- `screenshots/g1_d/rear.png`
- `screenshots/g1_d/left.png`
- `screenshots/g1_d/right.png`
- `screenshots/g1_d/top.png`
- `screenshots/g1_d/perspective.png`
- `screenshots/g1_d/isometric.png`

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._