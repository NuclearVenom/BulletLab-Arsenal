# Goal Description
Enable nested package structures in BulletLab Arsenal (e.g. `unitree/g1_description`) so that a user can load `arsenal:unitree/g1_description/g1_29dof` seamlessly, without modifying the underlying folder architecture or `metadata.json` files in the Arsenal repository.

## Proposed Changes

### BulletLab Core Package (`bulletlab`)
We need to update the parser to dynamically match package names using the manifest, since a slash `/` can now represent both a nested package path *or* the separator between a package and a model ID.

#### [MODIFY] [resolver.py](file:///c:/Users/ranas/Desktop/BulletLab/bulletlab/arsenal/resolver.py)
- **`parse_source(source)`**: Rewrite this function to first call `_get_manifest()`. It will check the requested `source` string against all valid `package_name`s in the manifest (matching the longest possible prefix). 
- If `source` matches a package exactly (e.g. `unitree/g1_description`), it returns `(package_name, None)`.
- If it starts with `package_name + "/"`, it extracts the remainder as the `model_id`.
- This completely fixes the parsing ambiguity without breaking existing flat packages.

### BulletLab Arsenal Repository (`BulletLab Arsenal`)
We need to update the Arsenal verification pipeline to properly acknowledge nested packages and use their relative paths as the global identifiers.

#### [MODIFY] [manifest.py](file:///c:/Users/ranas/Desktop/BulletLab%20Arsenal/scripts/verification/manifest.py)
- Update `generate_category_manifest` to set the generated `package_name` to the relative path from the category root (e.g. `unitree/g1_description`), instead of just the basename (`g1_description`).
- This ensures the manifest outputs the full path, which BulletLab will use to construct the correct URL.

#### [MODIFY] [identity.py](file:///c:/Users/ranas/Desktop/BulletLab%20Arsenal/scripts/verification/identity.py)
- Change `_discover_packages` to use `rglob("metadata.json")` instead of `iterdir()`, allowing it to find nested packages (like `unitree/g1_description`) during identity verification.
- Update `PackageInfo` to store the `rel_path`.
- Update the global namespace uniqueness check to verify that the *relative path* is unique across the repository, rather than just the basename, preventing false-positive name collisions between different manufacturers.

## Verification Plan
### Automated Tests
- Run `arsenal verify --all` (or `python scripts/run_verification.py --all`) in the Arsenal repository. It should successfully discover all nested `unitree` models and pass the identity checks.
- Run `arsenal manifest` to regenerate `manifest.json`.

### Manual Verification
- Execute `python examples/08_loading_humanoid.py`. It should successfully parse `unitree/g1_description`, download the metadata from the nested URL, download the meshes, and open the PyBullet UI with the humanoid robot.
