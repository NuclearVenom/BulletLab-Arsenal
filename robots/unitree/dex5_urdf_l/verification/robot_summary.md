# Verification Report: Dex5 Urdf L

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:24:26.950181+00:00
> **BulletLab version:** 0.2.1

## Description

Here are the ROS simulation packages for Unitree robots, You can load robots and joint controllers in Gazebo, so you can perform low-level control (control the torque, position and angular velocity) of the robot joints. Please be aware that the Gazebo simulation cannot do high-level control, namely 

## Model: Dex5 URDF L (`dex5_urdf_l`)

**Entrypoint:** `urdf/Dex5-URDF-L.urdf`

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
| Width (X) | 0.205 |
| Depth (Y) | 0.2171 |
| Height (Z)| 0.0869 |

**Links:** 21  |  **Joints:** 20  |  **Controllable:** 20

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| Yaw_11L | revolute | -0.587 | 0.680 | 0.9 | 4.2 |
| Roll_12L | revolute | -1.815 | 0.000 | 0.9 | 4.2 |
| Pitch_13L | revolute | 0.000 | 1.765 | 0.9 | 4.2 |
| Pitch_14L | revolute | 0.000 | 1.641 | 0.9 | 4.2 |
| Roll_21L | revolute | -0.384 | 0.384 | 0.9 | 0.8 |
| Pitch_22L | revolute | 0.000 | 1.571 | 0.9 | 3.1 |
| Pitch_23L | revolute | 0.000 | 1.684 | 0.9 | 3.4 |
| Pitch_24L | revolute | 0.000 | 1.396 | 0.9 | 2.8 |
| Roll_31L | revolute | -0.384 | 0.384 | 0.9 | 0.8 |
| Pitch_32L | revolute | 0.000 | 1.571 | 0.9 | 3.1 |
| Pitch_33L | revolute | 0.000 | 1.684 | 0.9 | 3.4 |
| Pitch_34L | revolute | 0.000 | 1.396 | 0.9 | 2.8 |
| Link_41L | revolute | -0.384 | 0.384 | 0.9 | 0.8 |
| Pitch_42L | revolute | 0.000 | 1.571 | 0.9 | 3.1 |
| Pitch_43L | revolute | 0.000 | 1.684 | 0.9 | 3.4 |
| Pitch_44L | revolute | 0.000 | 1.396 | 0.9 | 2.8 |
| Roll_51L | revolute | -0.384 | 0.384 | 0.9 | 0.8 |
| Pitch_52L | revolute | 0.000 | 1.571 | 0.9 | 3.1 |
| Pitch_53L | revolute | 0.000 | 1.684 | 0.9 | 3.4 |
| Pitch_54L | revolute | 0.000 | 1.396 | 0.9 | 2.8 |

### Screenshots

- `screenshots/dex5_urdf_l/front.png`
- `screenshots/dex5_urdf_l/rear.png`
- `screenshots/dex5_urdf_l/left.png`
- `screenshots/dex5_urdf_l/right.png`
- `screenshots/dex5_urdf_l/top.png`
- `screenshots/dex5_urdf_l/perspective.png`
- `screenshots/dex5_urdf_l/isometric.png`

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._