# Figures Directory
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)

---

## 1. Overview

This directory contains publication-ready figures (PNG raster for web rendering and SVG vector format for publications) generated from digitized TCAD simulation data, alongside the original Sentaurus Inspect plots.

## 2. Directory Structure

```text
figures/
├── device/
│   ├── device_architecture_schematic.png     # Engineering cross-section diagram
│   └── device_architecture_schematic.svg     # Vector cross-section diagram
├── electrical/
│   ├── k_sweep_transfer_characteristics.png  # Dual-panel K-sweep transfer curve (linear & log)
│   ├── k_sweep_transfer_characteristics.svg  # Vector version
│   ├── id_vgs_qf_neutral.png                 # Original Sentaurus Inspect plot
│   └── ioff_vgs_qf_neutral.png               # Original Sentaurus Inspect plot
├── sensing/
│   ├── cavity_thickness_transfer_characteristics.png  # Cavity thickness variation (tcav = 30, 35, 40 nm)
│   ├── cavity_thickness_transfer_characteristics.svg  # Vector version
│   ├── fixed_charge_sensitivity_comparison.png        # Negative vs Positive QF biomolecule response
│   ├── fixed_charge_sensitivity_comparison.svg        # Vector version
│   ├── ion_cavity.png                        # Original Sentaurus Inspect plot
│   └── ioff_cavity.png                       # Original Sentaurus Inspect plot
├── comparative/
│   ├── metrics_benchmark_summary.png         # 4-panel benchmark (Ion, SS, Vth shift, Ion/Ioff)
│   └── metrics_benchmark_summary.svg         # Vector version
├── optimization/
│   ├── ion_k_values.png                      # Original Sentaurus Inspect plot
│   └── ioff_k_values.png                     # Original Sentaurus Inspect plot
└── physics/
    └── electric_field_distribution.png       # Original Sentaurus Inspect plot
```

## 3. Publication Standards

All generated plots adhere to IEEE Electron Device Society (EDS) / Nature publication guidelines:
- **Resolution**: 300 DPI raster (`.png`) and scalable vector (`.svg`).
- **Typography**: Clean sans-serif font hierarchy (10–12 pt).
- **Color Palettes**: High-contrast, distinguishable curve colors with SI-standard units ($\mu\text{A}/\mu\text{m}$, $\text{V}$, $\text{mV/dec}$, $\text{cm}^{-2}$).
- **Plotting Script**: Regenerable via `python analysis/scripts/plot_publication_figures.py`.
