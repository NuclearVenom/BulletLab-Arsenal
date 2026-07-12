# Laikago Description

The laikago_description package

## Overview

| Field | Value |
|-------|-------|
| Package | `laikago_description` |
| Version | `0.0.0` |
| License | `BSD-3-Clause` |
| Authors | HangZhou YuShu TECHNOLOGY CO.,LTD. |
| Tags | `ros`, `gazebo`, `simulation`, `robotics`, `unitree`, `robot-description`, `controller` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `laikago` | Laikago | `urdf/laikago.urdf`  **(default)** |
| `robot` | Robot | `urdf/robot.urdf` |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("laikago_description")

# Load a specific variant
robot = Robot.load("laikago_description/laikago")
```

## Source Project

[Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots)

### Upstream Description

The ROS simulation packages for Unitree robots allow you to load robots and joint controllers in Gazebo, enabling low-level control of the robot joints, including torque, position, and angular velocity. Note that Gazebo simulation does not support high-level control, such as walking. Additionally, you can control your real robots in ROS using the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages, which support both high-level and low-level control.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements, including Gazebo plugins and transmissions, have been removed.
* Verify physics parameters against the upstream source before using them in critical simulations.
* This package has no ROS dependency and loads directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
