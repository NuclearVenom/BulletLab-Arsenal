# Verification Report: G1 Description

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:25:34.722083+00:00
> **BulletLab version:** 0.2.1

## Description

Here are the ROS simulation packages for Unitree robots, You can load robots and joint controllers in Gazebo, so you can perform low-level control (control the torque, position and angular velocity) of the robot joints. Please be aware that the Gazebo simulation cannot do high-level control, namely 

## Model: g1 23dof (`g1_23dof`)

**Entrypoint:** `urdf/g1_23dof.urdf`

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
| Width (X) | 0.4547 |
| Depth (Y) | 0.3692 |
| Height (Z)| 1.3264 |

**Links:** 33  |  **Joints:** 32  |  **Controllable:** 23

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| pelvis_contour_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_hip_pitch_joint | revolute | -2.531 | 2.880 | 88.0 | 32.0 |
| left_hip_roll_joint | revolute | -0.524 | 2.967 | 88.0 | 32.0 |
| left_hip_yaw_joint | revolute | -2.758 | 2.758 | 88.0 | 32.0 |
| left_knee_joint | revolute | -0.087 | 2.880 | 139.0 | 20.0 |
| left_ankle_pitch_joint | revolute | -0.873 | 0.524 | 35.0 | 30.0 |
| left_ankle_roll_joint | revolute | -0.262 | 0.262 | 35.0 | 30.0 |
| right_hip_pitch_joint | revolute | -2.531 | 2.880 | 88.0 | 32.0 |
| right_hip_roll_joint | revolute | -2.967 | 0.524 | 88.0 | 32.0 |
| right_hip_yaw_joint | revolute | -2.758 | 2.758 | 88.0 | 32.0 |
| right_knee_joint | revolute | -0.087 | 2.880 | 139.0 | 20.0 |
| right_ankle_pitch_joint | revolute | -0.873 | 0.524 | 35.0 | 30.0 |
| right_ankle_roll_joint | revolute | -0.262 | 0.262 | 35.0 | 30.0 |
| waist_yaw_joint | revolute | -2.618 | 2.618 | 88.0 | 32.0 |
| waist_yaw_fixed_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| logo_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| head_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| waist_support_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| imu_in_torso_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| d435_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| mid360_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_shoulder_pitch_joint | revolute | -3.089 | 2.670 | 25.0 | 37.0 |
| left_shoulder_roll_joint | revolute | -1.588 | 2.252 | 25.0 | 37.0 |
| left_shoulder_yaw_joint | revolute | -2.618 | 2.618 | 25.0 | 37.0 |
| left_elbow_joint | revolute | -1.047 | 2.094 | 25.0 | 37.0 |
| left_wrist_roll_joint | revolute | -1.972 | 1.972 | 25.0 | 37.0 |
| right_shoulder_pitch_joint | revolute | -3.089 | 2.670 | 25.0 | 37.0 |
| right_shoulder_roll_joint | revolute | -2.252 | 1.588 | 25.0 | 37.0 |
| right_shoulder_yaw_joint | revolute | -2.618 | 2.618 | 25.0 | 37.0 |
| right_elbow_joint | revolute | -1.047 | 2.094 | 25.0 | 37.0 |
| right_wrist_roll_joint | revolute | -1.972 | 1.972 | 25.0 | 37.0 |
| imu_in_pelvis_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/g1_23dof/front.png`
- `screenshots/g1_23dof/rear.png`
- `screenshots/g1_23dof/left.png`
- `screenshots/g1_23dof/right.png`
- `screenshots/g1_23dof/top.png`
- `screenshots/g1_23dof/perspective.png`
- `screenshots/g1_23dof/isometric.png`

## Model: g1 23dof rev 1 0 (`g1_23dof_rev_1_0`)

**Entrypoint:** `urdf/g1_23dof_rev_1_0.urdf`

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
| Width (X) | 0.4547 |
| Depth (Y) | 0.3692 |
| Height (Z)| 1.3264 |

**Links:** 31  |  **Joints:** 30  |  **Controllable:** 23

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| pelvis_contour_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_hip_pitch_joint | revolute | -2.531 | 2.880 | 88.0 | 32.0 |
| left_hip_roll_joint | revolute | -0.524 | 2.967 | 139.0 | 20.0 |
| left_hip_yaw_joint | revolute | -2.758 | 2.758 | 88.0 | 32.0 |
| left_knee_joint | revolute | -0.087 | 2.880 | 139.0 | 20.0 |
| left_ankle_pitch_joint | revolute | -0.873 | 0.524 | 35.0 | 30.0 |
| left_ankle_roll_joint | revolute | -0.262 | 0.262 | 35.0 | 30.0 |
| right_hip_pitch_joint | revolute | -2.531 | 2.880 | 88.0 | 32.0 |
| right_hip_roll_joint | revolute | -2.967 | 0.524 | 139.0 | 20.0 |
| right_hip_yaw_joint | revolute | -2.758 | 2.758 | 88.0 | 32.0 |
| right_knee_joint | revolute | -0.087 | 2.880 | 139.0 | 20.0 |
| right_ankle_pitch_joint | revolute | -0.873 | 0.524 | 35.0 | 30.0 |
| right_ankle_roll_joint | revolute | -0.262 | 0.262 | 35.0 | 30.0 |
| waist_yaw_joint | revolute | -2.618 | 2.618 | 88.0 | 32.0 |
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
| right_shoulder_pitch_joint | revolute | -3.089 | 2.670 | 25.0 | 37.0 |
| right_shoulder_roll_joint | revolute | -2.252 | 1.588 | 25.0 | 37.0 |
| right_shoulder_yaw_joint | revolute | -2.618 | 2.618 | 25.0 | 37.0 |
| right_elbow_joint | revolute | -1.047 | 2.094 | 25.0 | 37.0 |
| right_wrist_roll_joint | revolute | -1.972 | 1.972 | 25.0 | 37.0 |
| imu_in_pelvis_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/g1_23dof_rev_1_0/front.png`
- `screenshots/g1_23dof_rev_1_0/rear.png`
- `screenshots/g1_23dof_rev_1_0/left.png`
- `screenshots/g1_23dof_rev_1_0/right.png`
- `screenshots/g1_23dof_rev_1_0/top.png`
- `screenshots/g1_23dof_rev_1_0/perspective.png`
- `screenshots/g1_23dof_rev_1_0/isometric.png`

## Model: g1 29dof (`g1_29dof`)

**Entrypoint:** `urdf/g1_29dof.urdf`

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
| Width (X) | 0.3785 |
| Depth (Y) | 0.3692 |
| Height (Z)| 1.3264 |

**Links:** 40  |  **Joints:** 39  |  **Controllable:** 29

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| pelvis_contour_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_hip_pitch_joint | revolute | -2.531 | 2.880 | 88.0 | 32.0 |
| left_hip_roll_joint | revolute | -0.524 | 2.967 | 88.0 | 32.0 |
| left_hip_yaw_joint | revolute | -2.758 | 2.758 | 88.0 | 32.0 |
| left_knee_joint | revolute | -0.087 | 2.880 | 139.0 | 20.0 |
| left_ankle_pitch_joint | revolute | -0.873 | 0.524 | 35.0 | 30.0 |
| left_ankle_roll_joint | revolute | -0.262 | 0.262 | 35.0 | 30.0 |
| right_hip_pitch_joint | revolute | -2.531 | 2.880 | 88.0 | 32.0 |
| right_hip_roll_joint | revolute | -2.967 | 0.524 | 88.0 | 32.0 |
| right_hip_yaw_joint | revolute | -2.758 | 2.758 | 88.0 | 32.0 |
| right_knee_joint | revolute | -0.087 | 2.880 | 139.0 | 20.0 |
| right_ankle_pitch_joint | revolute | -0.873 | 0.524 | 35.0 | 30.0 |
| right_ankle_roll_joint | revolute | -0.262 | 0.262 | 35.0 | 30.0 |
| waist_yaw_joint | revolute | -2.618 | 2.618 | 88.0 | 32.0 |
| waist_roll_joint | revolute | -0.520 | 0.520 | 35.0 | 30.0 |
| waist_pitch_joint | revolute | -0.520 | 0.520 | 35.0 | 30.0 |
| logo_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| head_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| waist_support_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
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
| left_hand_palm_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| right_shoulder_pitch_joint | revolute | -3.089 | 2.670 | 25.0 | 37.0 |
| right_shoulder_roll_joint | revolute | -2.252 | 1.588 | 25.0 | 37.0 |
| right_shoulder_yaw_joint | revolute | -2.618 | 2.618 | 25.0 | 37.0 |
| right_elbow_joint | revolute | -1.047 | 2.094 | 25.0 | 37.0 |
| right_wrist_roll_joint | revolute | -1.972 | 1.972 | 25.0 | 37.0 |
| right_wrist_pitch_joint | revolute | -1.614 | 1.614 | 5.0 | 22.0 |
| right_wrist_yaw_joint | revolute | -1.614 | 1.614 | 5.0 | 22.0 |
| right_hand_palm_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| imu_in_pelvis_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/g1_29dof/front.png`
- `screenshots/g1_29dof/rear.png`
- `screenshots/g1_29dof/left.png`
- `screenshots/g1_29dof/right.png`
- `screenshots/g1_29dof/top.png`
- `screenshots/g1_29dof/perspective.png`
- `screenshots/g1_29dof/isometric.png`

## Model: g1 29dof rev 1 0 (`g1_29dof_rev_1_0`)

**Entrypoint:** `urdf/g1_29dof_rev_1_0.urdf`

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
| Width (X) | 0.3785 |
| Depth (Y) | 0.3692 |
| Height (Z)| 1.3264 |

**Links:** 39  |  **Joints:** 38  |  **Controllable:** 29

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| pelvis_contour_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_hip_pitch_joint | revolute | -2.531 | 2.880 | 88.0 | 32.0 |
| left_hip_roll_joint | revolute | -0.524 | 2.967 | 139.0 | 20.0 |
| left_hip_yaw_joint | revolute | -2.758 | 2.758 | 88.0 | 32.0 |
| left_knee_joint | revolute | -0.087 | 2.880 | 139.0 | 20.0 |
| left_ankle_pitch_joint | revolute | -0.873 | 0.524 | 35.0 | 30.0 |
| left_ankle_roll_joint | revolute | -0.262 | 0.262 | 35.0 | 30.0 |
| right_hip_pitch_joint | revolute | -2.531 | 2.880 | 88.0 | 32.0 |
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
| left_hand_palm_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| right_shoulder_pitch_joint | revolute | -3.089 | 2.670 | 25.0 | 37.0 |
| right_shoulder_roll_joint | revolute | -2.252 | 1.588 | 25.0 | 37.0 |
| right_shoulder_yaw_joint | revolute | -2.618 | 2.618 | 25.0 | 37.0 |
| right_elbow_joint | revolute | -1.047 | 2.094 | 25.0 | 37.0 |
| right_wrist_roll_joint | revolute | -1.972 | 1.972 | 25.0 | 37.0 |
| right_wrist_pitch_joint | revolute | -1.614 | 1.614 | 5.0 | 22.0 |
| right_wrist_yaw_joint | revolute | -1.614 | 1.614 | 5.0 | 22.0 |
| right_hand_palm_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| imu_in_pelvis_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/g1_29dof_rev_1_0/front.png`
- `screenshots/g1_29dof_rev_1_0/rear.png`
- `screenshots/g1_29dof_rev_1_0/left.png`
- `screenshots/g1_29dof_rev_1_0/right.png`
- `screenshots/g1_29dof_rev_1_0/top.png`
- `screenshots/g1_29dof_rev_1_0/perspective.png`
- `screenshots/g1_29dof_rev_1_0/isometric.png`

## Model: g1 29dof with hand (`g1_29dof_with_hand`)

**Entrypoint:** `urdf/g1_29dof_with_hand.urdf`

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
| Width (X) | 0.5023 |
| Depth (Y) | 0.3692 |
| Height (Z)| 1.3264 |

**Links:** 54  |  **Joints:** 53  |  **Controllable:** 43

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| pelvis_contour_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_hip_pitch_joint | revolute | -2.531 | 2.880 | 88.0 | 32.0 |
| left_hip_roll_joint | revolute | -0.524 | 2.967 | 88.0 | 32.0 |
| left_hip_yaw_joint | revolute | -2.758 | 2.758 | 88.0 | 32.0 |
| left_knee_joint | revolute | -0.087 | 2.880 | 139.0 | 20.0 |
| left_ankle_pitch_joint | revolute | -0.873 | 0.524 | 35.0 | 30.0 |
| left_ankle_roll_joint | revolute | -0.262 | 0.262 | 35.0 | 30.0 |
| right_hip_pitch_joint | revolute | -2.531 | 2.880 | 88.0 | 32.0 |
| right_hip_roll_joint | revolute | -2.967 | 0.524 | 88.0 | 32.0 |
| right_hip_yaw_joint | revolute | -2.758 | 2.758 | 88.0 | 32.0 |
| right_knee_joint | revolute | -0.087 | 2.880 | 139.0 | 20.0 |
| right_ankle_pitch_joint | revolute | -0.873 | 0.524 | 35.0 | 30.0 |
| right_ankle_roll_joint | revolute | -0.262 | 0.262 | 35.0 | 30.0 |
| waist_yaw_joint | revolute | -2.618 | 2.618 | 88.0 | 32.0 |
| waist_roll_joint | revolute | -0.520 | 0.520 | 35.0 | 30.0 |
| waist_pitch_joint | revolute | -0.520 | 0.520 | 35.0 | 30.0 |
| logo_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| head_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| waist_support_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
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
| left_hand_palm_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_hand_thumb_0_joint | revolute | -1.047 | 1.047 | 2.5 | 3.1 |
| left_hand_thumb_1_joint | revolute | -0.611 | 1.047 | 1.4 | 12.0 |
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
| right_hand_thumb_0_joint | revolute | -1.047 | 1.047 | 2.5 | 3.1 |
| right_hand_thumb_1_joint | revolute | -1.047 | 0.611 | 1.4 | 12.0 |
| right_hand_thumb_2_joint | revolute | -1.745 | 0.000 | 1.4 | 12.0 |
| right_hand_middle_0_joint | revolute | 0.000 | 1.571 | 1.4 | 12.0 |
| right_hand_middle_1_joint | revolute | 0.000 | 1.745 | 1.4 | 12.0 |
| right_hand_index_0_joint | revolute | 0.000 | 1.571 | 1.4 | 12.0 |
| right_hand_index_1_joint | revolute | 0.000 | 1.745 | 1.4 | 12.0 |
| imu_in_pelvis_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/g1_29dof_with_hand/front.png`
- `screenshots/g1_29dof_with_hand/rear.png`
- `screenshots/g1_29dof_with_hand/left.png`
- `screenshots/g1_29dof_with_hand/right.png`
- `screenshots/g1_29dof_with_hand/top.png`
- `screenshots/g1_29dof_with_hand/perspective.png`
- `screenshots/g1_29dof_with_hand/isometric.png`

## Model: g1 29dof with hand rev 1 0 (`g1_29dof_with_hand_rev_1_0`)

**Entrypoint:** `urdf/g1_29dof_with_hand_rev_1_0.urdf`

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
| Width (X) | 0.5023 |
| Depth (Y) | 0.3692 |
| Height (Z)| 1.3264 |

**Links:** 53  |  **Joints:** 52  |  **Controllable:** 43

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| pelvis_contour_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_hip_pitch_joint | revolute | -2.531 | 2.880 | 88.0 | 32.0 |
| left_hip_roll_joint | revolute | -0.524 | 2.967 | 139.0 | 20.0 |
| left_hip_yaw_joint | revolute | -2.758 | 2.758 | 88.0 | 32.0 |
| left_knee_joint | revolute | -0.087 | 2.880 | 139.0 | 20.0 |
| left_ankle_pitch_joint | revolute | -0.873 | 0.524 | 35.0 | 30.0 |
| left_ankle_roll_joint | revolute | -0.262 | 0.262 | 35.0 | 30.0 |
| right_hip_pitch_joint | revolute | -2.531 | 2.880 | 88.0 | 32.0 |
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
| left_hand_palm_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| left_hand_thumb_0_joint | revolute | -1.047 | 1.047 | 2.5 | 3.1 |
| left_hand_thumb_1_joint | revolute | -0.611 | 1.047 | 1.4 | 12.0 |
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
| right_hand_thumb_0_joint | revolute | -1.047 | 1.047 | 2.5 | 3.1 |
| right_hand_thumb_1_joint | revolute | -1.047 | 0.611 | 1.4 | 12.0 |
| right_hand_thumb_2_joint | revolute | -1.745 | 0.000 | 1.4 | 12.0 |
| right_hand_middle_0_joint | revolute | 0.000 | 1.571 | 1.4 | 12.0 |
| right_hand_middle_1_joint | revolute | 0.000 | 1.745 | 1.4 | 12.0 |
| right_hand_index_0_joint | revolute | 0.000 | 1.571 | 1.4 | 12.0 |
| right_hand_index_1_joint | revolute | 0.000 | 1.745 | 1.4 | 12.0 |
| imu_in_pelvis_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/g1_29dof_with_hand_rev_1_0/front.png`
- `screenshots/g1_29dof_with_hand_rev_1_0/rear.png`
- `screenshots/g1_29dof_with_hand_rev_1_0/left.png`
- `screenshots/g1_29dof_with_hand_rev_1_0/right.png`
- `screenshots/g1_29dof_with_hand_rev_1_0/top.png`
- `screenshots/g1_29dof_with_hand_rev_1_0/perspective.png`
- `screenshots/g1_29dof_with_hand_rev_1_0/isometric.png`

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._