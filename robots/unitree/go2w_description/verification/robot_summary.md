# Verification Report: Go2W Description

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:27:39.019812+00:00
> **BulletLab version:** 0.2.1

## Description

Here are the ROS simulation packages for Unitree robots, You can load robots and joint controllers in Gazebo, so you can perform low-level control (control the torque, position and angular velocity) of the robot joints. Please be aware that the Gazebo simulation cannot do high-level control, namely 

## Model: go2w description (`go2w_description`)

**Entrypoint:** `urdf/go2w_description.urdf`

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
| Width (X) | 0.6354 |
| Depth (Y) | 0.438 |
| Height (Z)| 0.5864 |

**Links:** 33  |  **Joints:** 32  |  **Controllable:** 16

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| Head_upper_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| Head_lower_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_hip_joint | revolute | -1.047 | 1.047 | 23.7 | 30.1 |
| FL_thigh_joint | revolute | -1.571 | 3.491 | 23.7 | 30.1 |
| FL_calf_joint | revolute | -2.723 | -0.838 | 35.5 | 20.1 |
| FL_calflower_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_calflower1_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_foot_motor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FL_foot_joint | revolute | 0.000 | -1.000 | 23.7 | 30.1 |
| FR_hip_joint | revolute | -1.047 | 1.047 | 23.7 | 30.1 |
| FR_thigh_joint | revolute | -1.571 | 3.491 | 23.7 | 30.1 |
| FR_calf_joint | revolute | -2.723 | -0.838 | 35.5 | 20.1 |
| FR_calflower_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FR_calflower1_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FR_foot_motor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| FR_foot_joint | revolute | 0.000 | -1.000 | 23.7 | 30.1 |
| RL_hip_joint | revolute | -1.047 | 1.047 | 23.7 | 30.1 |
| RL_thigh_joint | revolute | -0.524 | 4.538 | 23.7 | 30.1 |
| RL_calf_joint | revolute | -2.723 | -0.838 | 35.5 | 20.1 |
| RL_calflower_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_calflower1_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_foot_motor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RL_foot_joint | revolute | 0.000 | -1.000 | 23.7 | 30.1 |
| RR_hip_joint | revolute | -1.047 | 1.047 | 23.7 | 30.1 |
| RR_thigh_joint | revolute | -0.524 | 4.538 | 23.7 | 30.1 |
| RR_calf_joint | revolute | -2.723 | -0.838 | 35.5 | 20.1 |
| RR_calflower_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_calflower1_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_foot_motor_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| RR_foot_joint | revolute | 0.000 | -1.000 | 23.7 | 30.1 |
| imu_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| radar_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/go2w_description/front.png`
- `screenshots/go2w_description/rear.png`
- `screenshots/go2w_description/left.png`
- `screenshots/go2w_description/right.png`
- `screenshots/go2w_description/top.png`
- `screenshots/go2w_description/perspective.png`
- `screenshots/go2w_description/isometric.png`

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._