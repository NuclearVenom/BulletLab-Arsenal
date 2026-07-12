# NOTICE

## Original Project

**A7 Description**

## Original Source Repository

https://github.com/unitreerobotics/unitree_ros/tree/master/robots

## Original Authors

- HangZhou YuShu TECHNOLOGY CO., LTD.

## Original License

BSD-3-Clause (see LICENSE file)

## BulletLab Arsenal Modifications

This package was ported to BulletLab Arsenal by **BulletLab Forge**.

The following transformations were applied to the original source files:

- Resolved 18 mesh references
- Rewrote 36 mesh paths to ../meshes/<name>

## Summary of Changes

1. All `package://` URI references were removed and replaced with `../meshes/<filename>`.
2. ROS-specific XML elements (`<gazebo>`, `<transmission>`, and `<ros2_control>`) were removed.
3. All mesh paths are now relative, and no external dependencies remain.
4. The package is self-contained and loads without a ROS installation.

## Redistribution Notes

This package is distributed under the original upstream license stated above. All original copyright notices are preserved in the LICENSE file. The modifications made by BulletLab Forge are released under the MIT License.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
