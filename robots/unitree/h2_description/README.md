# H2 Description

The ROS simulation packages for Unitree robots are provided here. You can load robots and joint controllers in Gazebo, enabling low-level control of the robot joints, including torque, position, and angular velocity. Please note that Gazebo simulation does not support high-level control, such as walking.

## Overview

| Field | Value |
|-------|-------|
| Package | `h2_description` |
| Version | `1.0.0` |
| License | `BSD-3-Clause` |
| Authors | HangZhou YuShu TECHNOLOGY CO.,LTD., Unitree Robotics |
| Tags | `ros`, `gazebo`, `simulation`, `robot-description`, `controller`, `unitree` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `h2` | H2 | `urdf/H2.urdf`  |
| `h2_dae` | H2 dae | `urdf/H2_dae.urdf` |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("h2_description")

# Load a specific variant
robot = Robot.load("h2_description/h2")
```

## Source Project

The upstream repository for this project is [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots).

### Introduction

The ROS simulation packages for Unitree robots allow you to load robots and joint controllers in Gazebo, enabling low-level control of the robot joints, including torque, position, and angular velocity. Please note that Gazebo simulation does not support high-level control, such as walking. Additionally, you can control your real robots in ROS using the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages, which support both high-level and low-level control.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements, such as Gazebo plugins and transmissions, have been removed.
* It is recommended to verify physics parameters against the upstream source before using them in critical simulations.
* This package has no ROS dependency and can be loaded directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
