# Verification Report: Z1 Description

> **Overall Status:** PASS
> **Verified on:** 2026-07-12T08:29:40.009695+00:00
> **BulletLab version:** 0.2.1

## Description

The z1_description package

## Model: robot (`robot`)

**Entrypoint:** `urdf/robot.urdf`

**Status:** PASS

### Verification Checks

| Check          | Result |
|----------------|--------|
| Loading        | PASS |
| Stability      | PASS |
| Joint Exercise | PASS |

### Dimensions

| Axis      | Size (m) |
|-----------|----------|
| Width (X) | 0.356 |
| Depth (Y) | 0.006 |
| Height (Z)| 0.193 |

**Links:** 8  |  **Joints:** 7  |  **Controllable:** 6

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| base_static_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| joint1 | revolute | 0.000 | 0.000 | 0.0 | 0.0 |
| joint2 | revolute | 0.000 | 0.000 | 0.0 | 0.0 |
| joint3 | revolute | 0.000 | 0.000 | 0.0 | 0.0 |
| joint4 | revolute | 0.000 | 0.000 | 0.0 | 0.0 |
| joint5 | revolute | 0.000 | 0.000 | 0.0 | 0.0 |
| joint6 | revolute | 0.000 | 0.000 | 0.0 | 0.0 |

### Screenshots

- `screenshots/robot/front.png`
- `screenshots/robot/rear.png`
- `screenshots/robot/left.png`
- `screenshots/robot/right.png`
- `screenshots/robot/top.png`
- `screenshots/robot/perspective.png`
- `screenshots/robot/isometric.png`

## Model: z1 (`z1`)

**Entrypoint:** `urdf/z1.urdf`

**Status:** PASS

### Verification Checks

| Check          | Result |
|----------------|--------|
| Loading        | PASS |
| Stability      | PASS |
| Joint Exercise | PASS |

### Dimensions

| Axis      | Size (m) |
|-----------|----------|
| Width (X) | 0.4267 |
| Depth (Y) | 0.108 |
| Height (Z)| 0.2 |

**Links:** 8  |  **Joints:** 7  |  **Controllable:** 6

### Joint Summary

| Name | Type | Lower | Upper | Max Force | Max Vel |
|------|------|-------|-------|-----------|---------|
| base_static_joint | fixed | 0.000 | -1.000 | 0.0 | 0.0 |
| joint1 | revolute | -2.618 | 2.618 | 30.0 | 3.1 |
| joint2 | revolute | 0.000 | 2.967 | 60.0 | 3.1 |
| joint3 | revolute | -2.880 | 0.000 | 30.0 | 3.1 |
| joint4 | revolute | -1.518 | 1.518 | 30.0 | 3.1 |
| joint5 | revolute | -1.344 | 1.344 | 30.0 | 3.1 |
| joint6 | revolute | -2.793 | 2.793 | 30.0 | 3.1 |

### Screenshots

- `screenshots/z1/front.png`
- `screenshots/z1/rear.png`
- `screenshots/z1/left.png`
- `screenshots/z1/right.png`
- `screenshots/z1/top.png`
- `screenshots/z1/perspective.png`
- `screenshots/z1/isometric.png`

---
_This report was generated automatically by BulletLab Arsenal verification. Do not edit manually._