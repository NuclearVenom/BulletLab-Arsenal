# BLem1 — BulletLab Example Model 1

This is the first official package in the BulletLab Arsenal registry! It was originally created by me, Ranasurya Ghosh — the founder of BulletLab — as a personal exercise while learning CAD. I later decided to publish it here as BulletLab's first robot model and as a practical, real-world template for contributors to reference when building their own packages.

---

## Robot Description

BLem1 is a compact four-wheeled rover with a distinctive mechanical design:

- **Body**: A rigid base chassis carrying most of the robot's mass.
- **Legs**: Four articulated legs — two at the front, two at the rear — each driven by a continuous-rotation joint. The legs serve as suspension arms and can fold to adjust ground clearance.
- **Wheels**: Four wheels, one at the end of each leg, driven independently via continuous-rotation joints.
- **Neck**: A continuously-rotating yaw joint mounted on top of the chassis.
- **Head**: A pitch-axis revolute joint attached to the neck, giving the head a tilting range of ±0.5 rad.

| Property | Value |
|---|---|
| Total links | 11 (base, neck, head, 4 legs, 4 wheels) |
| Total joints | 9 (4 leg, 4 wheel, 1 neck yaw, 1 head pitch) |
| Chassis mass | 22 kg |
| Mesh scale | 0.001 (source meshes in millimetres) |
| Mesh format | STL |

---

## Package Structure

```text
reference_bot/
├── metadata.json
├── LICENSE
├── NOTICE.md
├── README.md
├── urdf/
│   └── BLem1.urdf
└── meshes/
    ├── base_link.stl
    ├── neck.stl
    ├── head.stl
    ├── leg1.stl
    ├── leg2.stl
    ├── leg3.stl
    ├── leg4.stl
    ├── wheel1.stl
    ├── wheel2.stl
    ├── wheel3.stl
    └── wheel4.stl
```

---

## Using This Package as a Template

This package is designed to be a reference for contributors adding their own robots to BulletLab Arsenal. When building your own package, follow the same structure:

1. Place all URDF files inside `urdf/`.
2. Place all mesh files inside `meshes/`.
3. Use relative mesh paths in the URDF (e.g. `../meshes/part.stl`).
4. Fill in `metadata.json` following the same field structure shown here.
5. Include a `LICENSE` and `NOTICE.md` in the package root.

For the full specification, read [`docs/robot-package-spec.md`](../../docs/robot-package-spec.md).

---

## License

MIT License — see the [LICENSE](./LICENSE) file for details.
