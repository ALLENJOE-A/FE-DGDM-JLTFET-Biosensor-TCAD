# SDE Structure Directory

This directory is intended for Synopsys Sentaurus Structure Editor (SDE) input files.

## Expected Contents

- `structure.tdf` — Technology data file defining materials, models
- `geometry.dat` / `.tdf` — Device geometry definition (2D cross-section)
- `mesh.dat` — Mesh generation parameters
- `doping.dat` — Doping profiles for source, channel, drain
- `electrodes.dat` — Contact/electrode definitions
- `materials.dat` — Material parameters (including ferroelectric)

## Current Status

**No SDE input files are present in the current repository.** The simulation outputs in `results/` were generated from SDE/SDevice files that are not included.

## Required for Reproducibility

To reproduce the simulations, the following SDE files need to be added:

1. **Device Geometry**: T-shaped channel, inverted-T nanocavity, double-gate stack
2. **Ferroelectric Layer**: HfO₂-based with Landau-Khalatnikov parameters
3. **Doping Profiles**: Junctionless n-type channel, n⁺ source/drain
4. **Mesh**: Fine mesh at tunnel junction and nanocavity region
5. **Boundaries**: Dirichlet/Neumann conditions for gates, source, drain, substrate

---

## SDE Workflow

```text
sde
  ├── geometry.tdr          # 2D device cross-section
  ├── doping.tdr            # Doping regions
  ├── material.tdr          # Material database (add FE material)
  ├── electrode.tdr         # Contact definitions
  └── mesh.tdr              # Mesh refinement regions
        ↓
Run SDE → generates .tdf for SDevice
```