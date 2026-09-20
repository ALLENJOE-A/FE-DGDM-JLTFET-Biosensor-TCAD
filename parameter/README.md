# Parameter Directory

This directory is intended for simulation parameter files and sweep definitions.

## Expected Contents

- `device_params.json` — Core device dimensions and doping
- `ferroelectric_params.json` — FE material parameters (Landau coefficients)
- `sweep_cavity.json` — Cavity thickness sweep values
- `sweep_k_values.json` — Ferroelectric K sweep values
- `sweep_qf_values.json` — Ferroelectric QF polarity/values
- `simulation_settings.json` — Solver tolerances, convergence criteria

## Current Status

**No parameter files are present in the current repository.** The sweep ranges and exact values used to generate the plots in `results/` are not documented.

## Parameter Categories

| Category | Parameters | Status |
|----------|------------|--------|
| Geometry | Channel length, cavity depth/width, gate oxide thickness | Not documented |
| Doping | Channel, source, drain concentrations | Not documented |
| Ferroelectric | ε_r (K), P_s, E_c, Landau α/β/γ, QF | K and QF swept, values not documented |
| Electrical | VGS range, VDS, temperature | Not documented |
| Mesh | Min/max element size, refinement ratios | Not documented |
| Solver | Newton tolerance, Gummel iterations, damping | Not documented |

---

## Adding Parameter Files

When adding parameter files, use JSON format for readability:

```json
{
  "device": {
    "channel_length_nm": 30,
    "cavity_depth_nm": 10,
    "gate_oxide_nm": 2
  },
  "ferroelectric": {
    "dielectric_constant": 25,
    "fixed_charge_cm2": 1e12,
    "landau_alpha": 1.0e5,
    "landau_beta": 1.0e9
  },
  "sweeps": {
    "cavity_thickness_nm": [5, 10, 15, 20],
    "k_values": [15, 20, 25, 30, 35],
    "qf_polarity": ["negative", "neutral", "positive"]
  }
}
```