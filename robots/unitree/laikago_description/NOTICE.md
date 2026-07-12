# NOTICE

## Original Project

**Laikago Description**

## Original Source Repository

https://github.com/unitreerobotics/unitree_ros/tree/master/robots

## Original Authors

- HangZhou YuShu TECHNOLOGY CO., LTD.

## Original License

BSD-3-Clause (see LICENSE file)

## BulletLab Arsenal Modifications

This package was ported to BulletLab Arsenal by **BulletLab Forge**.

The following transformations were applied to the original source files:

- Resolved 5 mesh references
- Rewrote 13 mesh paths to ../meshes/<name>
- WARNING: Xacro compilation failed for robot.xacro; raw content returned
- Resolved 1 additional mesh reference
- Rewrote 1 additional mesh path to ../meshes/<name>
- Removed the package:// URI scheme from mesh references
- Removed xacro namespace declarations

## Summary of Changes

1. All `package://` URI references have been removed and replaced with `../meshes/<filename>`.
2. ROS-specific XML elements (`<gazebo>`, `<transmission>`, and `<ros2_control>`) have been removed.
3. All mesh paths are now relative, eliminating external dependencies.
4. The package is self-contained and can be loaded without a ROS installation.

## Redistribution Notes

This package is distributed under the original upstream license stated above. All original copyright notices are preserved in the LICENSE file. The modifications made by BulletLab Forge are released under the MIT License.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
