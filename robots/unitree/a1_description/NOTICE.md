# NOTICE

## Original Project

**A1 Description**

## Original Source Repository

https://github.com/unitreerobotics/unitree_ros/tree/master/robots

## Original Authors

- HangZhou YuShu TECHNOLOGY CO., LTD.

## Original License

BSD-3-Clause (see LICENSE file)

## BulletLab Arsenal Modifications

This package was ported to BulletLab Arsenal by **BulletLab Forge**.

The following transformations were applied to the original source files:

- Removed 45 ROS/simulation-only elements (gazebo, transmission, ros2_control)
- Resolved and rewrote mesh references, including:
  - 6 mesh references resolved
  - 14 mesh paths rewritten to ../meshes/<name>
- Removed package:// URI scheme from mesh references
- Note: xacro compilation failed for robot.xacro; raw content returned
- Removed xacro namespace declarations

## Summary of Changes

1. All `package://` URI references removed and replaced with relative paths (`../meshes/<filename>`).
2. ROS-specific XML elements (`<gazebo>`, `<transmission>`, `<ros2_control>`) removed.
3. All mesh paths are now relative; no external dependencies remain.
4. Package is self-contained and loads without a ROS installation.

## Redistribution Notes

Distributed under the original upstream license stated above.
All original copyright notices are preserved in the LICENSE file.
BulletLab Forge modifications are released under the MIT License.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
