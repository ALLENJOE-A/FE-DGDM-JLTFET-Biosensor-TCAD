# SDevice Physics Models Directory

Physics model configuration files for Sentaurus Device.

## Expected Contents

- `models.tdr` — Main physics model selection
- `ferroelectric.tdr` — FE-specific models (Landau-Khalatnikov)
- `tunneling.tdr` — BTBT model parameters
- `mobility.tdr` — Mobility model selection
- `quantum.tdr` — Quantum correction models

## Current Status

**Empty** — No physics model files in the current repository.

## Physics Models (Inferred)

Based on the simulation outputs (TFET operation, ferroelectric effects), the following models were likely used:

| Physics | Model | Notes |
|---------|-------|-------|
| Band-to-Band Tunneling | Hurkx / Kane / Schenk | Required for TFET |
| Ferroelectric Polarization | Landau-Khalatnikov | Dynamic P-E hysteresis |
| Carrier Transport | Drift-Diffusion + BTBT | Standard for TFET |
| Mobility | Philips Unified / Lombardi | High-field saturation |
| Quantum Effects | Density Gradient | For thin channels |
| Recombination | SRH / Auger | Standard |

## Adding Model Files

When adding physics files, document the exact model cards:

```text
# models.tdr example
Physics {
  BTBT { Model = Hurkx }
  Ferroelectric { Model = LandauKhalatnikov }
  Mobility { Model = PhilipsUnified }
  Quantum { Model = DensityGradient }
}
```