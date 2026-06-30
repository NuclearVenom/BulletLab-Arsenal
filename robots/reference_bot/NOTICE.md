# Attribution Notice

## Source Information

**Original Project Name:** BLem1 — BulletLab Example Model 1

**Original Source Repository:** https://github.com/NuclearVenom/bulletlab-arsenal

**Original Authors:** Ranasurya Ghosh

**Original License:** MIT

## BulletLab Arsenal Modifications

This package was created as an original work specifically for the BulletLab Arsenal repository. It serves as the canonical reference template and worked example of the Arsenal package format.

No upstream assets were modified; all URDF, mesh, and metadata files were authored from scratch.

For reference, common modifications made when porting third-party robots include:

- Removing `xacro` preprocessing tags and compiling to plain URDF.
- Converting DAE visual meshes to STL or OBJ.
- Replacing `package://original_package/...` mesh paths with relative paths inside `meshes/`.
- Restructuring files into the required `urdf/` and `meshes/` directories.
- Simplifying collision meshes to improve simulation speed.
- Re-orienting the root link to conform to BulletLab's Z-up convention.

## Redistribution Notes

This package is released under the MIT License.

Redistribution and modification are permitted, provided that the original copyright notice and license text are preserved. See the LICENSE file in this directory for the full license terms.
