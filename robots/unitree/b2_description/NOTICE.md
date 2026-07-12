# NOTICE

## Original Project

**B2 Description**

## Original Source Repository

https://github.com/unitreerobotics/unitree_ros/tree/master/robots

## Original Authors

- Unitree Robotics

## Original License

BSD-3-Clause (see LICENSE file)

## BulletLab Arsenal Modifications

This package was ported to BulletLab Arsenal by **BulletLab Forge**.

The following transformations were applied to the original source files:

- Resolved 14 mesh references
- Rewrote mesh paths to use relative paths (../meshes/<name>)
- Removed the package:// URI scheme from mesh references
- Note: Xacro compilation failed for robot.xacro, so the raw content is returned
- Removed xacro namespace declarations

## Summary of Changes

1. Replaced all `package://` URI references with relative paths (../meshes/<filename>).
2. Removed ROS-specific XML elements, including `<gazebo>`, `<transmission>`, and `<ros2_control>`.
3. Converted all mesh paths to relative paths, eliminating external dependencies.
4. The package is now self-contained and can be loaded without a ROS installation.

## Redistribution Notes

This package is distributed under the original upstream license stated above. All original copyright notices are preserved in the LICENSE file. The modifications made by BulletLab Forge are released under the MIT License.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
