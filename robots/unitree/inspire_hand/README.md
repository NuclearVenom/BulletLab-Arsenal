# Inspire Hand

The Inspire Hand package provides ROS simulation packages for Unitree robots. These packages enable loading robots and joint controllers in Gazebo, allowing for low-level control of robot joints, including torque, position, and angular velocity. Note that Gazebo simulation does not support high-level control, such as walking.

## Overview

| Field | Value |
|-------|-------|
| Package | `inspire_hand` |
| Version | `1.0.0` |
| License | `BSD-3-Clause` |
| Authors | Unitree Robotics |
| Tags | `ros`, `urdf`, `robot-description`, `dexterous-hand`, `simulation` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `dfq_left_hand` | DFQ left hand | `urdf/DFQ_left_hand.urdf`  |
| `dfq_right_hand` | DFQ right hand | `urdf/DFQ_right_hand.urdf` |
| `ftp_left_hand` | FTP left hand | `urdf/FTP_left_hand.urdf` |
| `ftp_right_hand` | FTP right hand | `urdf/FTP_right_hand.urdf` |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("inspire_hand")

# Load a specific variant
robot = Robot.load("inspire_hand/dfq_left_hand")
```

## Source Project

The Inspire Hand package is based on the [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots). The upstream repository provides ROS simulation packages for Unitree robots, allowing for low-level control of robot joints in Gazebo. Additionally, the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages enable control of real robots in ROS, supporting both high-level and low-level control.

## Introduction to Upstream Repository

The upstream repository contains ROS simulation packages for Unitree robots. These packages allow for loading robots and joint controllers in Gazebo, enabling low-level control of robot joints. However, please note that Gazebo simulation does not support high-level control, such as walking. For real robots, the upstream repository provides ROS packages that support both high-level and low-level control.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements, including Gazebo plugins and transmissions, have been removed.
* It is essential to verify physics parameters against the upstream source before using them in critical simulations.
* This package has no ROS dependency and can be loaded directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
