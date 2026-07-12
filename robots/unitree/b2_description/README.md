# B2 Description

The ROS simulation packages for Unitree robots are provided here. You can load robots and joint controllers in Gazebo, enabling low-level control of the robot joints, including torque, position, and angular velocity. Note that the Gazebo simulation does not support high-level control, such as walking.

## Overview

| Field | Value |
|-------|-------|
| Package | `b2_description` |
| Version | `1.0.0` |
| License | `BSD-3-Clause` |
| Authors | Unitree Robotics |
| Tags | `ros`, `urdf`, `robot-description`, `b2`, `quadruped`, `simulation`, `gazebo` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `b2_description` | B2 Description | `urdf/b2_description.urdf`  **(default)** |
| `robot` | Robot | `urdf/robot.urdf` |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("b2_description")

# Load a specific variant
robot = Robot.load("b2_description/b2_description")
```

## Source Project

The upstream repository for this project is [https://github.com/unitreerobotics/unitree_ros/tree/master/robots](https://github.com/unitreerobotics/unitree_ros/tree/master/robots).

### Upstream Description

The ROS simulation packages for Unitree robots allow you to load robots and joint controllers in Gazebo, enabling low-level control of the robot joints. This includes control of torque, position, and angular velocity. Please note that the Gazebo simulation does not support high-level control, such as walking. In addition to simulation, you can also control your real robots in ROS using the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages. For real robots, you can perform both high-level and low-level control using our ROS packages.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements, such as Gazebo plugins and transmissions, have been removed.
* Before using this package in critical simulations, verify the physics parameters against the upstream source.
* This package has no ROS dependency and can be loaded directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
