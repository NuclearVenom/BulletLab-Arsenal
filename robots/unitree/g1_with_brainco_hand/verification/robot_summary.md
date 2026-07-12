# Verification Report: G1 With Brainco Hand

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:27:02.079538+00:00
> **BulletLab version:** 0.2.1

## Description

Here are the ROS simulation packages for Unitree robots, You can load robots and joint controllers in Gazebo, so you can perform low-level control (control the torque, position and angular velocity) of the robot joints. Please be aware that the Gazebo simulation cannot do high-level control, namely 

## Model: g1 29dof mode 15 brainco hand (`g1_29dof_mode_15_brainco_hand`)

**Entrypoint:** `urdf/g1_29dof_mode_15_brainco_hand.urdf`

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
| Width (X) | 0.5091 |
| Depth (Y) | 0.3692 |
| Height (Z)| 1.3264 |

**Links:** 72  |  **Joints:** 71  |  **Controllable:** 61

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| left_hip_pitch_joint | revolute | -2.531 | 2.880 | 139.0 | 20.0 |
| left_hip_roll_joint | revolute | -0.524 | 2.967 | 139.0 | 20.0 |
| left_hip_yaw_joint | revolute | -2.758 | 2.758 | 88.0 | 32.0 |
| left_knee_joint | revolute | -0.087 | 2.880 | 139.0 | 20.0 |
| left_ankle_pitch_joint | revolute | -0.873 | 0.524 | 35.0 | 30.0 |
| left_ankle_roll_joint | revolute | -0.262 | 0.262 | 35.0 | 30.0 |
| right_hip_pitch_joint | revolute | -2.531 | 2.880 | 139.0 | 20.0 |
| right_hip_roll_joint | revolute | -2.967 | 0.524 | 139.0 | 20.0 |
| right_hip_yaw_joint | revolute | -2.758 | 2.758 | 88.0 | 32.0 |
| right_knee_joint | revolute | -0.087 | 2.880 | 139.0 | 20.0 |
| right_ankle_pitch_joint | revolute | -0.873 | 0.524 | 35.0 | 30.0 |
| right_ankle_roll_joint | revolute | -0.262 | 0.262 | 35.0 | 30.0 |
| waist_yaw_joint | revolute | -2.618 | 2.618 | 88.0 | 32.0 |
| waist_roll_joint | revolute | -0.520 | 0.520 | 35.0 | 30.0 |
| waist_pitch_joint | revolute | -0.520 | 0.520 | 35.0 | 30.0 |
| logo_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| head_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| imu_in_torso_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| d435_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| mid360_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_shoulder_pitch_joint | revolute | -3.089 | 2.670 | 25.0 | 37.0 |
| left_shoulder_roll_joint | revolute | -1.588 | 2.252 | 25.0 | 37.0 |
| left_shoulder_yaw_joint | revolute | -2.618 | 2.618 | 25.0 | 37.0 |
| left_elbow_joint | revolute | -1.047 | 2.094 | 25.0 | 37.0 |
| left_wrist_roll_joint | revolute | -1.972 | 1.972 | 25.0 | 37.0 |
| left_wrist_pitch_joint | revolute | -1.614 | 1.614 | 5.0 | 22.0 |
| left_wrist_yaw_joint | revolute | -1.614 | 1.614 | 5.0 | 22.0 |
| left_base2_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_base_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_thumb_metacarpal_joint | revolute | 0.000 | 1.518 | 0.5 | 2.6 |
| left_thumb_proximal_joint | revolute | 0.000 | 1.047 | 1.1 | 2.5 |
| left_thumb_distal_joint | revolute | 0.000 | 1.047 | 1.1 | 2.5 |
| left_thumb_tip_joint | revolute | 0.000 | 0.000 | 0.0 | 0.0 |
| left_index_proximal_joint | revolute | 0.000 | 1.466 | 2.0 | 2.3 |
| left_index_distal_joint | revolute | 0.000 | 1.693 | 2.0 | 2.3 |
| left_index_tip_joint | revolute | 1.000 | 1.000 | 1.0 | 1.0 |
| left_middle_proximal_joint | revolute | 0.000 | 1.466 | 2.0 | 2.3 |
| left_middle_distal_joint | revolute | 0.000 | 1.693 | 2.0 | 2.3 |
| left_middle_tip_joint | revolute | 1.000 | 1.000 | 1.0 | 1.0 |
| left_ring_proximal_joint | revolute | 0.000 | 1.466 | 2.0 | 2.3 |
| left_ring_distal_joint | revolute | 0.000 | 1.693 | 2.0 | 2.3 |
| left_ring_tip_joint | revolute | 1.000 | 1.000 | 1.0 | 1.0 |
| left_pinky_proximal_joint | revolute | 0.000 | 1.466 | 2.0 | 2.3 |
| left_pinky_distal_joint | revolute | 0.000 | 1.693 | 2.0 | 2.3 |
| left_pinky_tip_joint | revolute | 1.000 | 1.000 | 1.0 | 1.0 |
| right_shoulder_pitch_joint | revolute | -3.089 | 2.670 | 25.0 | 37.0 |
| right_shoulder_roll_joint | revolute | -2.252 | 1.588 | 25.0 | 37.0 |
| right_shoulder_yaw_joint | revolute | -2.618 | 2.618 | 25.0 | 37.0 |
| right_elbow_joint | revolute | -1.047 | 2.094 | 25.0 | 37.0 |
| right_wrist_roll_joint | revolute | -1.972 | 1.972 | 25.0 | 37.0 |
| right_wrist_pitch_joint | revolute | -1.614 | 1.614 | 5.0 | 22.0 |
| right_wrist_yaw_joint | revolute | -1.614 | 1.614 | 5.0 | 22.0 |
| right_base2_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| right_base_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| right_thumb_metacarpal_joint | revolute | 0.000 | 1.518 | 0.5 | 2.6 |
| right_thumb_proximal_joint | revolute | 0.000 | 1.047 | 1.1 | 2.5 |
| right_thumb_distal_joint | revolute | 0.000 | 1.047 | 1.1 | 2.5 |
| right_thumb_tip | revolute | 0.000 | 0.000 | 0.0 | 0.0 |
| right_index_proximal_joint | revolute | 0.000 | 1.466 | 2.0 | 2.3 |
| right_index_distal_joint | revolute | 0.000 | 1.693 | 2.0 | 2.3 |
| right_index_tip_joint | revolute | 0.000 | 0.000 | 0.0 | 0.0 |
| right_middle_proximal_joint | revolute | 0.000 | 1.466 | 2.0 | 2.3 |
| right_middle_distal_joint | revolute | 0.000 | 1.693 | 2.0 | 2.3 |
| right_middle_tip_joint | revolute | 0.000 | 0.000 | 0.0 | 0.0 |
| right_ring_proximal_joint | revolute | 0.000 | 1.466 | 2.0 | 2.3 |
| right_ring_distal_joint | revolute | 0.000 | 1.693 | 2.0 | 2.3 |
| right_ring_tip_joint | revolute | 0.000 | 0.000 | 0.0 | 0.0 |
| right_pinky_proximal_joint | revolute | 0.000 | 1.466 | 2.0 | 2.3 |
| right_pinky_distal_joint | revolute | 0.000 | 1.693 | 2.0 | 2.3 |
| right_pinky_tip_joint | revolute | 0.000 | 0.000 | 0.0 | 0.0 |
| imu_in_pelvis_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/g1_29dof_mode_15_brainco_hand/front.png`
- `screenshots/g1_29dof_mode_15_brainco_hand/rear.png`
- `screenshots/g1_29dof_mode_15_brainco_hand/left.png`
- `screenshots/g1_29dof_mode_15_brainco_hand/right.png`
- `screenshots/g1_29dof_mode_15_brainco_hand/top.png`
- `screenshots/g1_29dof_mode_15_brainco_hand/perspective.png`
- `screenshots/g1_29dof_mode_15_brainco_hand/isometric.png`

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._