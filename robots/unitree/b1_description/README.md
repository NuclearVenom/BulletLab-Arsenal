# B1 Description

The b1_description package

## Overview

| Field | Value |
|-------|-------|
| Package | `b1_description` |
| Version | `0.0.0` |
| License | `BSD-3-Clause` |
| Authors | HangZhou YuShu TECHNOLOGY CO.,LTD. (Unitree Robotics) |
| Tags | `ros`, `gazebo`, `simulation`, `unitree`, `b1-robot`, `urdf`, `low-level-control`, `robotics` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `b1` | B1 | `urdf/b1.urdf`  **(default)** |
| `robot` | Robot | `urdf/robot.urdf` |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("b1_description")

# Load a specific variant
robot = Robot.load("b1_description/b1")
```

## Source Project

[Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots)

### Upstream Description

# Introduction
The ROS simulation packages for Unitree robots allow you to load robots and joint controllers in Gazebo, enabling low-level control (control of torque, position, and angular velocity) of the robot joints. Please note that Gazebo simulation does not support high-level control, such as walking. In addition to these simulation functions, you can also control your real robots in ROS using the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages. For real robots, you can perform both high-level and low-level control using our ROS packages.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements (Gazebo plugins, transmissions) have been removed.
* Verify physics parameters against the upstream source before using them in critical simulations.
* This package has no ROS dependency and loads directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
