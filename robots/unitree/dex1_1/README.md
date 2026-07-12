# Dex1 1

Here are the ROS simulation packages for Unitree robots. You can load robots and joint controllers in Gazebo, allowing for low-level control of the robot joints, including torque, position, and angular velocity. Please note that the Gazebo simulation does not support high-level control, such as walking.

## Overview

| Field | Value |
|-------|-------|
| Package | `dex1_1` |
| Version | `1.0.0` |
| License | `BSD-3-Clause` |
| Authors | Unitree Robotics |
| Tags | `dexterous-hand`, `urdf`, `robot-description` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `dex1_1` | Dex1 1 | `urdf/dex1_1.urdf`  **(default)** |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("dex1_1")

# Load a specific variant
robot = Robot.load("dex1_1/dex1_1")
```

## Source Project

[Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots)

### Upstream Description

The ROS simulation packages for Unitree robots enable loading robots and joint controllers in Gazebo, allowing for low-level control of the robot joints, including torque, position, and angular velocity. Please note that the Gazebo simulation does not support high-level control, such as walking. Additionally, you can control your real robots in ROS using the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages, which support both high-level and low-level control.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements (Gazebo plugins, transmissions) have been removed.
* Verify physics parameters against the upstream source before using them in critical simulations.
* This package has no ROS dependency and loads directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
