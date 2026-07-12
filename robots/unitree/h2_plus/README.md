# H2 Plus

The H2 Plus package provides ROS simulation packages for Unitree robots. These packages enable loading robots and joint controllers in Gazebo, allowing for low-level control of robot joints, including torque, position, and angular velocity. Note that Gazebo simulation does not support high-level control, such as walking.

## Overview

| Field | Value |
|-------|-------|
| Package | `h2_plus` |
| Version | `1.0.0` |
| License | `BSD-3-Clause` |
| Authors | HangZhou YuShu TECHNOLOGY CO.,LTD. |
| Tags | `ros`, `gazebo`, `simulation`, `robotics`, `unitree`, `low-level-control`, `high-level-control` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `h2_plus` | H2 Plus | `urdf/H2_Plus.urdf`  |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("h2_plus")

# Load a specific variant
robot = Robot.load("h2_plus/h2_plus")
```

## Source Project

The upstream repository for this package is [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots).

### Upstream Description

The upstream repository provides ROS simulation packages for Unitree robots, allowing for low-level control of robot joints in Gazebo. Additionally, the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages enable control of real robots in ROS, supporting both high-level and low-level control.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements, such as Gazebo plugins and transmissions, have been removed.
* Physics parameters should be verified against the upstream source before use in critical simulations.
* This package has no ROS dependency and loads directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
