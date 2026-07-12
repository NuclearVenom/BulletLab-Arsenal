# Aliengo Description

The aliengo_description package provides a description of the Aliengo robot for use in simulation and control applications.

## Overview

| Field | Value |
|-------|-------|
| Package | `aliengo_description` |
| Version | `0.0.0` |
| License | `BSD-3-Clause` |
| Authors | HangZhou YuShu TECHNOLOGY CO.,LTD. |
| Tags | `ros`, `gazebo`, `simulation`, `robot-description`, `controller`, `unitree` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

The following models are available in the aliengo_description package:

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `aliengo` | Aliengo | `urdf/aliengo.urdf`  (default) |
| `robot` | Robot | `urdf/robot.urdf` |

## Usage

To load the Aliengo robot model, use the following Python code:
```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("aliengo_description")

# Load a specific variant
robot = Robot.load("aliengo_description/aliengo")
```

## Source Project

The aliengo_description package is based on the [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots).

### Upstream Description

The upstream repository provides ROS simulation packages for Unitree robots, allowing users to load robots and joint controllers in Gazebo for low-level control. Note that Gazebo simulation does not support high-level control, such as walking. For real robots, the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages can be used for high-level and low-level control in ROS.

## Known Limitations

The following limitations apply to the aliengo_description package:

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements (Gazebo plugins, transmissions) have been removed.
* Physics parameters should be verified against the upstream source before use in critical simulations.
* This package has no ROS dependency and loads directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
