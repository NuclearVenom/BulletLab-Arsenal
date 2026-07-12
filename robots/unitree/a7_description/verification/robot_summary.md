# Verification Report: A7 Description

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:21:12.209451+00:00
> **BulletLab version:** 0.2.1

## Description

Here are the ROS simulation packages for Unitree robots, You can load robots and joint controllers in Gazebo, so you can perform low-level control (control the torque, position and angular velocity) of the robot joints. Please be aware that the Gazebo simulation cannot do high-level control, namely 

## Model: A7 (`a7`)

**Entrypoint:** `urdf/A7.urdf`

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
| Width (X) | 0.5147 |
| Depth (Y) | 0.3827 |
| Height (Z)| 0.5019 |

**Links:** 18  |  **Joints:** 17  |  **Controllable:** 17

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| waist_yaw_joint | revolute | -2.618 | 2.618 | 60.0 | 18.7 |
| left_shoulder_pitch_joint | revolute | -3.142 | 2.094 | 60.0 | 18.7 |
| left_shoulder_roll_joint | revolute | -0.227 | 2.478 | 60.0 | 18.7 |
| left_shoulder_yaw_joint | revolute | -1.920 | 1.920 | 33.0 | 52.4 |
| left_elbow_joint | revolute | -0.976 | 2.185 | 33.0 | 52.4 |
| left_wrist_roll_joint | revolute | -1.920 | 1.920 | 33.0 | 52.4 |
| left_wrist_pitch_joint | revolute | -1.614 | 1.614 | 10.0 | 37.7 |
| left_wrist_yaw_joint | revolute | -1.614 | 1.614 | 10.0 | 37.7 |
| right_shoulder_pitch_joint | revolute | -3.142 | 2.094 | 60.0 | 18.7 |
| right_shoulder_roll_joint | revolute | -2.478 | 0.227 | 60.0 | 18.7 |
| right_shoulder_yaw_joint | revolute | -1.920 | 1.920 | 33.0 | 52.4 |
| right_elbow_joint | revolute | -0.976 | 2.185 | 33.0 | 52.4 |
| right_wrist_roll_joint | revolute | -1.920 | 1.920 | 33.0 | 52.4 |
| right_wrist_pitch_joint | revolute | -1.614 | 1.614 | 10.0 | 37.7 |
| right_wrist_yaw_joint | revolute | -1.614 | 1.614 | 10.0 | 37.7 |
| head_pitch_joint | revolute | -0.628 | 0.628 | 33.0 | 52.4 |
| head_yaw_joint | revolute | -2.007 | 2.007 | 0.9 | 11.0 |

### Screenshots

- `screenshots/a7/front.png`
- `screenshots/a7/rear.png`
- `screenshots/a7/left.png`
- `screenshots/a7/right.png`
- `screenshots/a7/top.png`
- `screenshots/a7/perspective.png`
- `screenshots/a7/isometric.png`

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._