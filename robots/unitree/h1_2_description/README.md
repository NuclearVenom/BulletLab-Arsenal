# H1 2 Description

The ROS simulation packages for Unitree robots are provided here. You can load robots and joint controllers in Gazebo, enabling low-level control of the robot joints, including torque, position, and angular velocity. Note that Gazebo simulation does not support high-level control, such as walking.

## Overview

| Field | Value |
|-------|-------|
| Package | `h1_2_description` |
| Version | `1.0.0` |
| License | `BSD-3-Clause` |
| Authors | HangZhou YuShu TECHNOLOGY CO.,LTD., Unitree Robotics |
| Tags | `ros`, `gazebo`, `simulation`, `robotics`, `unitree`, `urdf`, `low-level-control`, `robot-description` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `h1_2` | H1 2 | `urdf/h1_2.urdf`  **(default)** |
| `h1_2_handless` | H1 2 Handless | `urdf/h1_2_handless.urdf` |
| `h1_2_with_ftp_hand` | H1 2 with FTP Hand | `urdf/h1_2_with_FTP_hand.urdf` |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("h1_2_description")

# Load a specific variant
robot = Robot.load("h1_2_description/h1_2")
```

## Source Project

[Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots)

### Upstream Description

The ROS simulation packages for Unitree robots enable loading robots and joint controllers in Gazebo, allowing for low-level control of the robot joints. This includes control of torque, position, and angular velocity. Please note that Gazebo simulation does not support high-level control, such as walking. In addition to simulation functions, you can also control your real robots in ROS using the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages. For real robots, both high-level and low-level control are possible using our ROS packages.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements, such as Gazebo plugins and transmissions, have been removed.
* Verify physics parameters against the upstream source before using them in critical simulations.
* This package has no ROS dependency and loads directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
