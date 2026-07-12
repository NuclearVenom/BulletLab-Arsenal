# Verification Report: Dex5 Urdf R

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:24:55.866914+00:00
> **BulletLab version:** 0.2.1

## Description

Here are the ROS simulation packages for Unitree robots, You can load robots and joint controllers in Gazebo, so you can perform low-level control (control the torque, position and angular velocity) of the robot joints. Please be aware that the Gazebo simulation cannot do high-level control, namely 

## Model: Dex5 URDF R (`dex5_urdf_r`)

**Entrypoint:** `urdf/Dex5-URDF-R.urdf`

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
| Yaw_11R | revolute | -0.587 | 0.680 | 0.9 | 4.2 |
| Roll_12R | revolute | 0.000 | 1.815 | 0.9 | 4.2 |
| Pitch_13R | revolute | 0.000 | 1.765 | 0.9 | 4.2 |
| Pitch_14R | revolute | 0.000 | 1.641 | 0.9 | 4.2 |
| Roll_21R | revolute | -0.384 | 0.384 | 0.0 | 0.8 |
| Pitch_22R | revolute | 0.000 | 1.571 | 0.0 | 3.1 |
| Pitch_23R | revolute | 0.000 | 1.684 | 0.0 | 3.4 |
| Pitch_24R | revolute | 0.000 | 1.396 | 0.0 | 2.8 |
| Roll_31R | revolute | -0.384 | 0.384 | 0.0 | 0.8 |
| Pitch_32R | revolute | 0.000 | 1.571 | 0.0 | 3.1 |
| Pitch_33R | revolute | 0.000 | 1.684 | 0.0 | 3.4 |
| Pitch_34R | revolute | 0.000 | 1.396 | 0.0 | 2.8 |
| Roll_41R | revolute | -0.384 | 0.384 | 0.0 | 0.0 |
| Pitch_42R | revolute | 0.000 | 1.571 | 0.0 | 3.1 |
| Pitch_43R | revolute | 0.000 | 1.684 | 0.0 | 3.4 |
| Pitch_44R | revolute | 0.000 | 1.396 | 0.0 | 2.8 |
| Roll_51R | revolute | -0.384 | 0.384 | 0.0 | 0.0 |
| Pitch_52R | revolute | 0.000 | 1.571 | 0.0 | 3.1 |
| Pitch_53R | revolute | 0.000 | 1.684 | 0.0 | 3.4 |
| Pitch_54R | revolute | 0.000 | 1.396 | 0.0 | 2.8 |

### Screenshots

- `screenshots/dex5_urdf_r/front.png`
- `screenshots/dex5_urdf_r/rear.png`
- `screenshots/dex5_urdf_r/left.png`
- `screenshots/dex5_urdf_r/right.png`
- `screenshots/dex5_urdf_r/top.png`
- `screenshots/dex5_urdf_r/perspective.png`
- `screenshots/dex5_urdf_r/isometric.png`

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._