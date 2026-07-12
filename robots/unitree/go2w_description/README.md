# Go2W Description

The ROS simulation packages for Unitree robots are provided here. These packages allow you to load robots and joint controllers in Gazebo, enabling low-level control of the robot joints, including torque, position, and angular velocity. Note that Gazebo simulation does not support high-level control, such as walking.

## Overview

| Field | Value |
|-------|-------|
| Package | `go2w_description` |
| Version | `1.0.0` |
| License | `BSD-3-Clause` |
| Authors | TODO |
| Tags | `ros`, `gazebo`, `simulation`, `robot-description`, `controller`, `low-level-control` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `go2w_description` | Go2W Description | `urdf/go2w_description.urdf`  **(default)** |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("go2w_description")

# Load a specific variant
robot = Robot.load("go2w_description/go2w_description")
```

## Source Project

The upstream repository for this project is [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots).

### Upstream Description

The ROS simulation packages for Unitree robots allow you to load robots and joint controllers in Gazebo, enabling low-level control of the robot joints. This includes control of torque, position, and angular velocity. Please note that Gazebo simulation does not support high-level control, such as walking. In addition to simulation, you can also control your real robots in ROS using the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages. For real robots, you can perform both high-level and low-level control using our ROS packages.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements, such as Gazebo plugins and transmissions, have been removed.
* Before using this package in critical simulations, verify the physics parameters against the upstream source.
* This package has no ROS dependency and can be loaded directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
