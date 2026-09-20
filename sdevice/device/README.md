# SDevice Directory

This directory is intended for Synopsys Sentaurus Device (SDevice) simulation input files.

## Expected Contents

### Device Structure (`device/`)
- `device.tdr` — Device structure imported from SDE
- `electrodes.tdr` — Contact bias definitions

### Physics Models (`physics/`)
- `models.tdr` — Physical model selection:
  - Band-to-band tunneling (BTBT): Hurkx, Schenk, or Kane model
  - Ferroelectric: Landau-Khalatnikov or Preisach model
  - Transport: Drift-diffusion / Hydrodynamic / Energy balance
  - Quantum corrections: Density gradient / Quantum potential
  - Mobility: Philips unified / Lombardi / High-field saturation

### Simulation Decks
- `dc_sweep.cmd` — VGS sweep at fixed VDS
- `param_sweep.cmd` — Parameter sweep templates (cavity, K, QF)
- `extract.cmd` — Parameter extraction (Ion, Ioff, SS, VT)

## Current Status

**No SDevice input files are present in the current repository.** The plots in `results/` were generated from simulations whose input decks are not included.

## Physics Models (Inferred from Results)

| Physics | Likely Model |
|---------|--------------|
| Tunneling | Hurkx or Kane BTBT |
| Ferroelectric | Landau-Khalatnikov (P-E hysteresis) |
| Transport | Drift-diffusion + BTBT |
| Mesh | Non-uniform, refined at junctions |

---

## SDevice Workflow

```text
sdevice
  ├── device.tdr            # From SDE output
  ├── models.tdr            # Physics models
  ├── doping.tdr            # Doping profiles
  ├── contact.tdr           # Electrode biases
  ├── dc_iv.cmd             # VGS-VDS sweeps
  └── extract.tcl           # Parameter extraction scripts
        ↓
Run SDevice → generates .dat/.plt files
        ↓
Post-process → plots in results/
```