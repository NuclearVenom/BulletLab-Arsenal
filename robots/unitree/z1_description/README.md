# Z1 Description

The z1_description package

## Overview

| Field | Value |
|-------|-------|
| Package | `z1_description` |
| Version | `0.0.0` |
| License | `BSD-3-Clause` |
| Authors | Unitree Robotics |
| Tags | `ros`, `gazebo`, `simulation`, `robotics`, `unitree` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `robot` | Robot | `urdf/robot.urdf`  **(default)** |
| `z1` | Z1 | `urdf/z1.urdf` |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("z1_description")

# Load a specific variant
robot = Robot.load("z1_description/robot")
```

## Source Project

[Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots)

### Upstream Description

The ROS simulation packages for Unitree robots allow you to load robots and joint controllers in Gazebo, enabling low-level control of the robot joints, including torque, position, and angular velocity. Note that Gazebo simulation does not support high-level control, such as walking. In addition to simulation functions, you can also control your real robots in ROS using the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages. For real robots, both high-level and low-level control are possible using our ROS packages.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements, including Gazebo plugins and transmissions, have been removed.
* Physics parameters should be verified against the upstream source before use in critical simulations.
* This package has no ROS dependency and loads directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
