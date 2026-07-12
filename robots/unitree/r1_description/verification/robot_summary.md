# Verification Report: R1 Description

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:29:24.399255+00:00
> **BulletLab version:** 0.2.1

## Description

Here are the ROS simulation packages for Unitree robots, You can load robots and joint controllers in Gazebo, so you can perform low-level control (control the torque, position and angular velocity) of the robot joints. Please be aware that the Gazebo simulation cannot do high-level control, namely 

## Model: R1 (`r1`)

**Entrypoint:** `urdf/R1.urdf`

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
| Width (X) | 0.3751 |
| Depth (Y) | 0.3827 |
| Height (Z)| 1.2362 |

**Links:** 40  |  **Joints:** 39  |  **Controllable:** 26

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| left_hip_pitch_joint | revolute | -2.932 | 2.548 | 60.0 | 18.8 |
| left_hip_roll_joint | revolute | -1.047 | 1.745 | 60.0 | 18.8 |
| left_hip_yaw_joint | revolute | -2.740 | 2.740 | 60.0 | 18.8 |
| left_knee_joint | revolute | -0.175 | 2.426 | 60.0 | 18.8 |
| left_ankle_A_joint | fixed | -0.897 | 1.410 | 33.0 | 33.4 |
| left_ankle_A_rod_joint | fixed | 0.000 | 0.000 | 0.0 | 0.0 |
| left_ankle_B_joint | fixed | -1.400 | 0.923 | 33.0 | 33.4 |
| left_ankle_B_rod_joint | fixed | 0.000 | 0.000 | 0.0 | 0.0 |
| left_ankle_pitch_joint | revolute | -0.873 | 0.576 | 50.0 | 30.0 |
| left_ankle_roll_joint | revolute | -0.262 | 0.262 | 50.0 | 30.0 |
| left_ankle_constraint_A_joint | fixed | 0.000 | 0.000 | 0.0 | 0.0 |
| left_ankle_constraint_B_joint | fixed | 0.000 | 0.000 | 0.0 | 0.0 |
| right_hip_pitch_joint | revolute | -2.932 | 2.548 | 60.0 | 18.8 |
| right_hip_roll_joint | revolute | -1.745 | 1.047 | 60.0 | 18.8 |
| right_hip_yaw_joint | revolute | -2.740 | 2.740 | 60.0 | 18.8 |
| right_knee_joint | revolute | -0.175 | 2.426 | 60.0 | 18.8 |
| right_ankle_A_joint | fixed | -1.410 | 0.897 | 33.0 | 33.4 |
| right_ankle_A_rod_joint | fixed | 0.000 | 0.000 | 0.0 | 0.0 |
| right_ankle_B_joint | fixed | -0.923 | 1.400 | 33.0 | 33.4 |
| right_ankle_B_rod_joint | fixed | 0.000 | 0.000 | 0.0 | 0.0 |
| right_ankle_pitch_joint | revolute | -0.873 | 0.576 | 50.0 | 30.0 |
| right_ankle_roll_joint | revolute | -0.262 | 0.262 | 50.0 | 30.0 |
| right_ankle_constraint_A_joint | fixed | 0.000 | 0.000 | 0.0 | 0.0 |
| right_ankle_constraint_B_joint | fixed | 0.000 | 0.000 | 0.0 | 0.0 |
| imu_in_pelvis_joint | fixed | 0.000 | 0.000 | 0.0 | 0.0 |
| waist_roll_joint | revolute | -0.524 | 0.524 | 60.0 | 18.8 |
| waist_yaw_joint | revolute | -2.618 | 2.618 | 60.0 | 18.8 |
| left_shoulder_pitch_joint | revolute | -3.142 | 2.094 | 60.0 | 18.8 |
| left_shoulder_roll_joint | revolute | -0.227 | 2.478 | 60.0 | 18.8 |
| left_shoulder_yaw_joint | revolute | -1.920 | 1.920 | 33.0 | 33.4 |
| left_elbow_joint | revolute | -0.976 | 2.185 | 33.0 | 33.4 |
| left_wrist_roll_joint | revolute | -1.920 | 1.920 | 33.0 | 33.4 |
| right_shoulder_pitch_joint | revolute | -3.142 | 2.094 | 60.0 | 18.8 |
| right_shoulder_roll_joint | revolute | -2.478 | 0.227 | 60.0 | 18.8 |
| right_shoulder_yaw_joint | revolute | -1.920 | 1.920 | 33.0 | 33.4 |
| right_elbow_joint | revolute | -0.976 | 2.185 | 33.0 | 33.4 |
| right_wrist_roll_joint | revolute | -1.920 | 1.920 | 33.0 | 33.4 |
| head_pitch_joint | revolute | -0.628 | 0.628 | 33.0 | 33.4 |
| head_yaw_joint | revolute | -2.007 | 2.007 | 33.0 | 33.4 |

### Screenshots

- `screenshots/r1/front.png`
- `screenshots/r1/rear.png`
- `screenshots/r1/left.png`
- `screenshots/r1/right.png`
- `screenshots/r1/top.png`
- `screenshots/r1/perspective.png`
- `screenshots/r1/isometric.png`

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._