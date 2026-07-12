# Dex2 5

The ROS simulation packages for Unitree robots are provided here. You can load robots and joint controllers in Gazebo, enabling low-level control of the robot joints, including torque, position, and angular velocity. Note that Gazebo simulation does not support high-level control, such as walking.

## Overview

| Field | Value |
|-------|-------|
| Package | `dex2_5` |
| Version | `1.0.0` |
| License | `BSD-3-Clause` |
| Authors | Unitree Robotics |
| Tags | `robot`, `hand`, `dexterous`, `ros` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `left_hand` | Left Hand | `urdf/Left_Hand.urdf`  |
| `left_hand_g1_5010_wrist` | Left Hand G1 5010 Wrist | `urdf/Left_Hand_G1_5010_Wrist.urdf` |
| `right_hand` | Right Hand | `urdf/Right_Hand.urdf` |
| `right_hand_g1_5010_wrist` | Right Hand G1 5010 Wrist | `urdf/Right_Hand_G1_5010_Wrist.urdf` |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("dex2_5")

# Load a specific variant
robot = Robot.load("dex2_5/left_hand")
```

## Source Project

The upstream repository for this package is [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots).

### Upstream Description

The ROS simulation packages for Unitree robots allow you to load robots and joint controllers in Gazebo, enabling low-level control of the robot joints. This includes control of torque, position, and angular velocity. However, please note that Gazebo simulation does not support high-level control, such as walking. In addition to simulation functions, you can also control your real robots in ROS using the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages. For real robots, you can perform both high-level and low-level control using our ROS packages.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements, such as Gazebo plugins and transmissions, have been removed.
* Before using this package in critical simulations, verify the physics parameters against the upstream source.
* This package has no ROS dependency and loads directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
