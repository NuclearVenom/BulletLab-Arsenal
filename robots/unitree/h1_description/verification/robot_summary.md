# Verification Report: H1 Description

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:27:57.793195+00:00
> **BulletLab version:** 0.2.1

## Description

The Unitree H1 Description Package

## Model: h1 (`h1`)

**Entrypoint:** `urdf/h1.urdf`

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
| Width (X) | 0.282 |
| Depth (Y) | 0.5131 |
| Height (Z)| 1.7314 |

**Links:** 25  |  **Joints:** 24  |  **Controllable:** 19

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| left_hip_yaw_joint | revolute | -0.430 | 0.430 | 200.0 | 23.0 |
| left_hip_roll_joint | revolute | -0.430 | 0.430 | 200.0 | 23.0 |
| left_hip_pitch_joint | revolute | -3.140 | 2.530 | 200.0 | 23.0 |
| left_knee_joint | revolute | -0.260 | 2.050 | 300.0 | 14.0 |
| left_ankle_joint | revolute | -0.870 | 0.520 | 40.0 | 9.0 |
| right_hip_yaw_joint | revolute | -0.430 | 0.430 | 200.0 | 23.0 |
| right_hip_roll_joint | revolute | -0.430 | 0.430 | 200.0 | 23.0 |
| right_hip_pitch_joint | revolute | -3.140 | 2.530 | 200.0 | 23.0 |
| right_knee_joint | revolute | -0.260 | 2.050 | 300.0 | 14.0 |
| right_ankle_joint | revolute | -0.870 | 0.520 | 40.0 | 9.0 |
| torso_joint | revolute | -2.350 | 2.350 | 200.0 | 23.0 |
| left_shoulder_pitch_joint | revolute | -2.870 | 2.870 | 40.0 | 9.0 |
| left_shoulder_roll_joint | revolute | -0.340 | 3.110 | 40.0 | 9.0 |
| left_shoulder_yaw_joint | revolute | -1.300 | 4.450 | 18.0 | 20.0 |
| left_elbow_joint | revolute | -1.250 | 2.610 | 18.0 | 20.0 |
| right_shoulder_pitch_joint | revolute | -2.870 | 2.870 | 40.0 | 9.0 |
| right_shoulder_roll_joint | revolute | -3.110 | 0.340 | 40.0 | 9.0 |
| right_shoulder_yaw_joint | revolute | -4.450 | 1.300 | 18.0 | 20.0 |
| right_elbow_joint | revolute | -1.250 | 2.610 | 18.0 | 20.0 |
| imu_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| logo_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| d435_left_imager_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| d435_rgb_module_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| mid360_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/h1/front.png`
- `screenshots/h1/rear.png`
- `screenshots/h1/left.png`
- `screenshots/h1/right.png`
- `screenshots/h1/top.png`
- `screenshots/h1/perspective.png`
- `screenshots/h1/isometric.png`

## Model: h1 with hand (`h1_with_hand`)

**Entrypoint:** `urdf/h1_with_hand.urdf`

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
| Width (X) | 0.5544 |
| Depth (Y) | 0.5131 |
| Height (Z)| 1.7314 |

**Links:** 52  |  **Joints:** 51  |  **Controllable:** 45

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| left_hip_yaw_joint | revolute | -0.430 | 0.430 | 200.0 | 23.0 |
| left_hip_roll_joint | revolute | -0.430 | 0.430 | 200.0 | 23.0 |
| left_hip_pitch_joint | revolute | -3.140 | 2.530 | 200.0 | 23.0 |
| left_knee_joint | revolute | -0.260 | 2.050 | 300.0 | 14.0 |
| left_ankle_joint | revolute | -0.870 | 0.520 | 40.0 | 9.0 |
| right_hip_yaw_joint | revolute | -0.430 | 0.430 | 200.0 | 23.0 |
| right_hip_roll_joint | revolute | -0.430 | 0.430 | 200.0 | 23.0 |
| right_hip_pitch_joint | revolute | -3.140 | 2.530 | 200.0 | 23.0 |
| right_knee_joint | revolute | -0.260 | 2.050 | 300.0 | 14.0 |
| right_ankle_joint | revolute | -0.870 | 0.520 | 40.0 | 9.0 |
| torso_joint | revolute | -2.350 | 2.350 | 200.0 | 23.0 |
| left_shoulder_pitch_joint | revolute | -2.870 | 2.870 | 40.0 | 9.0 |
| left_shoulder_roll_joint | revolute | -0.340 | 3.110 | 40.0 | 9.0 |
| left_shoulder_yaw_joint | revolute | -1.300 | 4.450 | 18.0 | 20.0 |
| left_elbow_joint | revolute | -1.250 | 2.610 | 18.0 | 20.0 |
| left_hand_joint | revolute | -3.054 | 3.054 | 6.0 | 12.0 |
| L_base_link_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| L_thumb_proximal_yaw_joint | revolute | -0.100 | 1.300 | 1.0 | 0.5 |
| L_thumb_proximal_pitch_joint | revolute | -0.100 | 0.600 | 1.0 | 0.5 |
| L_thumb_intermediate_joint | revolute | 0.000 | 0.800 | 1.0 | 0.5 |
| L_thumb_distal_joint | revolute | 0.000 | 1.200 | 1.0 | 0.5 |
| L_index_proximal_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| L_index_intermediate_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| L_middle_proximal_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| L_middle_intermediate_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| L_ring_proximal_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| L_ring_intermediate_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| L_pinky_proximal_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| L_pinky_intermediate_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| right_shoulder_pitch_joint | revolute | -2.870 | 2.870 | 40.0 | 9.0 |
| right_shoulder_roll_joint | revolute | -3.110 | 0.340 | 40.0 | 9.0 |
| right_shoulder_yaw_joint | revolute | -4.450 | 1.300 | 18.0 | 20.0 |
| right_elbow_joint | revolute | -1.250 | 2.610 | 18.0 | 20.0 |
| right_hand_joint | revolute | -3.054 | 3.054 | 6.0 | 12.0 |
| R_base_link_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| R_thumb_proximal_yaw_joint | revolute | -0.100 | 1.300 | 1.0 | 0.5 |
| R_thumb_proximal_pitch_joint | revolute | -0.100 | 0.600 | 1.0 | 0.5 |
| R_thumb_intermediate_joint | revolute | 0.000 | 0.800 | 1.0 | 0.5 |
| R_thumb_distal_joint | revolute | 0.000 | 1.200 | 1.0 | 0.5 |
| R_index_proximal_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| R_index_intermediate_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| R_middle_proximal_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| R_middle_intermediate_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| R_ring_proximal_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| R_ring_intermediate_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| R_pinky_proximal_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| R_pinky_intermediate_joint | revolute | 0.000 | 1.700 | 1.0 | 0.5 |
| logo_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| d435_left_imager_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| d435_rgb_module_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| mid360_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/h1_with_hand/front.png`
- `screenshots/h1_with_hand/rear.png`
- `screenshots/h1_with_hand/left.png`
- `screenshots/h1_with_hand/right.png`
- `screenshots/h1_with_hand/top.png`
- `screenshots/h1_with_hand/perspective.png`
- `screenshots/h1_with_hand/isometric.png`

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._