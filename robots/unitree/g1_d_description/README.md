# G1 D Description

The ROS simulation packages for Unitree robots are provided here. You can load robots and joint controllers in Gazebo, enabling low-level control of the robot joints, including torque, position, and angular velocity. Please note that the Gazebo simulation is limited to low-level control and does not support high-level control, such as walking.

## Overview

| Field | Value |
|-------|-------|
| Package | `g1_d_description` |
| Version | `1.0.0` |
| License | `BSD-3-Clause` |
| Authors | Unitree Robotics |
| Tags | `ros`, `gazebo`, `simulation`, `robotics`, `unitree` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `g1_d` | G1 D | `urdf/g1_d.urdf`  **(default)** |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("g1_d_description")

# Load a specific variant
robot = Robot.load("g1_d_description/g1_d")
```

## Source Project

[Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots)

### Upstream Description

The ROS simulation packages for Unitree robots allow you to load robots and joint controllers in Gazebo, enabling low-level control of the robot joints. This includes control of torque, position, and angular velocity. However, please be aware that the Gazebo simulation does not support high-level control, such as walking. In addition to these simulation functions, you can also control your real robots in ROS using the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages. For real robots, you can perform both high-level and low-level control using our ROS packages.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements, such as Gazebo plugins and transmissions, have been removed.
* Before using this package in critical simulations, verify the physics parameters against the upstream source.
* This package has no ROS dependency and can be loaded directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
