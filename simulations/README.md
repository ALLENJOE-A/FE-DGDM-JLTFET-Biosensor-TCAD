# Simulations Directory

Organized simulation campaigns by device variant.

## Structure

```
simulations/
├── baseline/       # Non-FE JLTFET (empty - needed for comparison)
├── proposed/       # FE-DGDM-JLTFET main device (empty - SDE/SDevice files needed)
├── biomolecule/    # Biomolecule-specific simulations (empty)
└── README.md
```

## Current Status

All subdirectories are **empty**. The repository only contains post-processed plots in `results/`, not the simulation input decks.

## Intended Use

| Directory | Purpose |
|-----------|---------|
| `baseline/` | Standard DG-JLTFET without ferroelectric for direct comparison |
| `proposed/` | Complete FE-DGDM-JLTFET simulation decks (SDE + SDevice) |
| `biomolecule/` | Simulations with explicit biomolecule models (charge, dipole, dielectric) |

## Adding Simulations

Each simulation campaign should contain:

```
simulations/proposed/
├── sde/
│   ├── geometry.tdr
│   ├── doping.tdr
│   └── mesh.tdr
├── sdevice/
│   ├── models.tdr
│   ├── dc_iv.cmd
│   └── extract.tcl
└── results/          # Link to ../results/ or copy outputs
```