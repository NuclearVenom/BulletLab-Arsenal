# G1 Description

The ROS simulation packages for Unitree robots are provided here. You can load robots and joint controllers in Gazebo, enabling low-level control of the robot joints, including torque, position, and angular velocity. Note that Gazebo simulation does not support high-level control, such as walking.

## Overview

| Field | Value |
|-------|-------|
| Package | `g1_description` |
| Version | `1.0.0` |
| License | `BSD-3-Clause` |
| Authors | HangZhou YuShu TECHNOLOGY CO.,LTD. |
| Tags | `ros`, `simulation`, `gazebo`, `unitree`, `robotics` |
| Source | [Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots) |
| BulletLab | `>=0.1.0` |

## Available Models

| ID | Display Name | Entrypoint |
|----|-------------|------------|
| `g1_23dof` | G1 23dof | `urdf/g1_23dof.urdf`  **(default)** |
| `g1_23dof_rev_1_0` | G1 23dof Rev 1.0 | `urdf/g1_23dof_rev_1_0.urdf` |
| `g1_29dof` | G1 29dof | `urdf/g1_29dof.urdf` |
| `g1_29dof_rev_1_0` | G1 29dof Rev 1.0 | `urdf/g1_29dof_rev_1_0.urdf` |
| `g1_29dof_with_hand` | G1 29dof with Hand | `urdf/g1_29dof_with_hand.urdf` |
| `g1_29dof_with_hand_rev_1_0` | G1 29dof with Hand Rev 1.0 | `urdf/g1_29dof_with_hand_rev_1_0.urdf` |

## Usage

```python
from bulletlab import Robot

# Load the default model
robot = Robot.load("g1_description")

# Load a specific variant
robot = Robot.load("g1_description/g1_23dof")
```

## Source Project

[Upstream Repository](https://github.com/unitreerobotics/unitree_ros/tree/master/robots)

### Upstream Description

The ROS simulation packages for Unitree robots allow you to load robots and joint controllers in Gazebo, enabling low-level control of the robot joints, including torque, position, and angular velocity. Please note that Gazebo simulation does not support high-level control, such as walking. In addition to these simulation functions, you can also control your real robots in ROS using the [unitree_ros_to_real](https://github.com/unitreerobotics/unitree_ros_to_real) packages. For real robots, you can perform both high-level and low-level control using our ROS packages.

## Known Limitations

* Mesh references have been rewritten to be self-contained (`../meshes/`).
* ROS-specific elements (Gazebo plugins, transmissions) have been removed.
* Verify physics parameters against the upstream source before use in critical simulations.
* This package has no ROS dependency and loads directly in BulletLab.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
