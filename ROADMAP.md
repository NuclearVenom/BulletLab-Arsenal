# BulletLab Arsenal Roadmap

BulletLab Arsenal is a long-term, curated ecosystem for robotics simulation assets. The roadmap outlines our planned progression from foundational robot models to a complete, seamless, single-line installation experience for complex simulation environments.

## Phase 1: Core Repository and Robot Validation Pipeline
*(Current Phase)*
Establishing the foundation of BulletLab Arsenal.
- Implement the two-layer verification pipeline.
- Define a strict package and metadata specification.
- Curate the initial collection of verified robot models.
- Auto-generate machine-readable manifests (`arsenal-manifest.json`).

## Phase 2: Interactive Package Viewer
A web-based interactive tool for previewing robots directly in the browser.
- Use `PyBullet.js` or a WebGL renderer to load and visualise URDFs from the Arsenal.
- Allow users to articulate joints and view metadata without installing anything.

## Phase 3: Verified Environments and Worlds
Expanding the Arsenal beyond robots to include simulation environments.
- Define a specification for world packages (SDF or URDF-based).
- Add verification for collision geometry and spawn points.
- Create an official `worlds/` directory and category manifest.

## Phase 4: Standardised Controller Interfaces
Defining generic controller interfaces for common locomotion and manipulation tasks.
- Provide baseline controllers for wheeled, bipedal, and quadrupedal robots.
- Integrate controllers smoothly with verified robots.

## Phase 5: Programmatic Installation Tool
Developing a command-line tool (e.g., `bl-install`) to easily pull packages from the Arsenal.
- Fetch robots, worlds, and controllers programmatically.
- Resolve dependencies if a robot requires a specific controller.

## Phase 6: Dynamic Web Registry
Building a full-fledged website (e.g., `arsenal.bulletlab.org`) to browse the ecosystem.
- Expose the auto-generated `arsenal-manifest.json` via a searchable frontend.
- Display verified screenshots, statistics, and GitHub contribution history natively on the site.

## Phase 7: Sensor Suite Specifications
Creating standard definitions for simulated sensors.
- LiDAR, RGB-D cameras, IMUs, and contact sensors.
- Standardise attachment points and data publication interfaces.

## Phase 8: Multi-agent Benchmarks
Providing out-of-the-box benchmark tasks.
- Combine verified robots, worlds, and sensors into reproducible benchmark scenarios (e.g., navigation, manipulation).
- Enable leaderboard tracking for research papers.
