# NOTICE

## Original Project

**B2W Description**

## Original Source Repository

https://github.com/unitreerobotics/unitree_ros/tree/master/robots

## Original Authors

* TODO: Please specify the original authors of the project.

## Original License

The original project is licensed under the BSD-3-Clause license (see LICENSE file).

## BulletLab Arsenal Modifications

This package was ported to BulletLab Arsenal by **BulletLab Forge**. The following transformations were applied to the original source files:

* Resolved 18 mesh references
* Rewrote 26 mesh paths to ../meshes/<name>
* Removed package:// URI scheme from mesh references
* Note: Xacro compilation failed for robot.xacro; raw content was returned
* Removed xacro namespace declarations

## Summary of Changes

1. All `package://` URI references were removed and replaced with relative paths (`../meshes/<filename>`).
2. ROS-specific XML elements (`<gazebo>`, `<transmission>`, `<ros2_control>`) were removed.
3. All mesh paths are now relative, eliminating external dependencies.
4. The package is self-contained and can be loaded without a ROS installation.

## Redistribution Notes

This package is distributed under the original upstream license stated above. All original copyright notices are preserved in the LICENSE file. The modifications made by BulletLab Forge are released under the MIT License.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
