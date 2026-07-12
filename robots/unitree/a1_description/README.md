# A1 Description

The a1_description package

## Overview

| Field | Value |
|-------|-------|
| Package | `a1_description` |
| Version | `0.0.0` |
| License | `BSD-3-Clause` |
| Authors | HangZhou YuShu TECHNOLOGY CO., LTD. |
| Tags | `ros`, `simulation`, `gazebo`, `unitree`, `robot-description`, `joint-controller` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `a1` | A1 | `urdf/a1.urdf`  **(default)** |
| `robot` | Robot | `urdf/robot.urdf` |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("a1_description")

# Load a specific variant
robot = Robot.load("a1_description/a1")
```

## Source Project

[Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots)

### Upstream Description

The ROS simulation packages for Unitree robots allow you to load robots and joint controllers in Gazebo, enabling low-level control of robot joints, including torque, position, and angular velocity. Note that Gazebo simulation does not support high-level control, such as walking. In addition to simulation functions, you can also control your real robots in ROS using the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages, which support both high-level and low-level control.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements, including Gazebo plugins and transmissions, have been removed.
* Verify physics parameters against the upstream source before using them in critical simulations.
* This package has no ROS dependency and can be loaded directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
