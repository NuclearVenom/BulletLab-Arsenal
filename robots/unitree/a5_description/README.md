# A5 Description

The ROS simulation packages for Unitree robots are provided here. You can load robots and joint controllers in Gazebo, enabling low-level control of the robot joints, including torque, position, and angular velocity. Note that Gazebo simulation does not support high-level control, such as walking.

## Overview

| Field | Value |
|-------|-------|
| Package | `a5_description` |
| Version | `1.0.0` |
| License | `BSD-3-Clause` |
| Authors | HangZhou YuShu TECHNOLOGY CO.,LTD. (Unitree Robotics) |
| Tags | `ros`, `gazebo`, `simulation`, `robot-description`, `joint-controller`, `low-level-control`, `unitree` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `a5` | A5 | `urdf/A5.urdf`  (default) |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("a5_description")

# Load a specific variant
robot = Robot.load("a5_description/a5")
```

## Source Project

The upstream repository for this project is [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots).

### Introduction

The ROS simulation packages for Unitree robots allow you to load robots and joint controllers in Gazebo, enabling low-level control of the robot joints. Please note that Gazebo simulation does not support high-level control, such as walking. In addition to simulation, you can also control your real robots in ROS using the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages. For real robots, you can perform both high-level and low-level control using our ROS packages.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements (gazebo plugins, transmissions) have been removed.
* Verify physics parameters against the upstream source before use in critical simulations.
* This package has no ROS dependency and loads directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
