# NOTICE

## Original Project
**Dex2 5**

## Original Source Repository
https://github.com/unitreerobotics/unitree_ros/tree/master/robots

## Original Authors
- Unitree Robotics

## Original License
BSD-3-Clause (see LICENSE file)

## BulletLab Arsenal Modifications
This package was ported to BulletLab Arsenal by **BulletLab Forge**.

The following transformations were applied to the original source files:
- Resolved and rewrote mesh references and paths to use relative paths (`../meshes/<name>`) for a total of 70 mesh references and 90 mesh paths.

## Summary of Changes
1. All `package://` URI references were removed and replaced with relative paths (`../meshes/<filename>`).
2. ROS-specific XML elements (`<gazebo>`, `<transmission>`, `<ros2_control>`) were removed.
3. All mesh paths are now relative, eliminating external dependencies.
4. The package is self-contained and can be loaded without a ROS installation.

## Redistribution Notes
This package is distributed under the original upstream license stated above. All original copyright notices are preserved in the LICENSE file. BulletLab Forge modifications are released under the MIT License.

---

> **Machine-generated document** — Created automatically by [BulletLab Forge](https://github.com/NuclearVenom/BulletLab-Forge). Contents are based on the upstream repository and may require manual review before submission to BulletLab Arsenal.
