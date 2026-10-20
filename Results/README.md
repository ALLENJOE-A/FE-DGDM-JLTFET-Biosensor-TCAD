# Results Directory
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)

---

## 1. Overview

This directory contains the original Sentaurus TCAD simulation graphics (`.png`), recovered historical datasets, and structured raw numerical data tables (`.csv`) extracted using reproducible Python workflows.

## 2. Directory Structure

```text
Results/
├── raw_data/                               # Structured CSV tables
│   ├── k_sweep_transfer.csv                # K-sweep (K=1 to 22) I-V data
│   ├── cavity_sweep_transfer.csv           # Cavity thickness (30, 35, 40 nm) I-V data
│   ├── qf_negative_transfer.csv            # Negative QF I-V data
│   ├── qf_positive_transfer.csv            # Positive QF I-V data
│   └── extracted_metrics_summary.csv       # Master metrics benchmark table
├── electrical/                             # Transfer & band profiles
│   ├── Ion_QF_neutral.png                  # Linear Id-Vgs (K-sweep verified)
│   ├── Ioff_QF_neutral.png                 # Log Id-Vgs (K-sweep verified)
│   ├── band_diagram_QF_neutral.png         # Band diagram (K-sweep verified)
│   └── surface_potential_QF_neutral.png    # Surface potential (K-sweep verified)
├── sensitivity/                            # Nanocavity & QF sweeps
│   ├── Ion_Cavity_verified.png             # Recovered genuine cavity linear Id-Vgs
│   ├── Ioff_Cavity_verified.png            # Recovered genuine cavity log Id-Vgs
│   ├── energy_band_Cavity.png              # Cavity thickness band diagram (30, 35, 40 nm)
│   ├── surface_potential_Cavity.png        # Cavity thickness surface potential
│   ├── Ion_Cavity.png                      # Negative QF linear Id-Vgs
│   ├── Ioff_Cavity.png                     # Negative QF log Id-Vgs
│   ├── Surface_potential.png               # Negative QF surface potential
│   ├── electric field.png                  # Negative QF electric field
│   ├── band_diagram_QF_negative.png        # Negative QF band diagram
│   ├── Ioff_QF_positive.png                # Positive QF log Id-Vgs
│   ├── electric_field_QF_positive.png      # Positive QF electric field
│   └── Description_Cavity_Length.txt       # "Analysis of Different Cavity Thickness Values"
└── optimization/                           # Ferroelectric K-value sweeps
    ├── Ion_K_values.png                    # Linear Id-Vgs vs K
    ├── Ioff_K_values.png                   # Log Id-Vgs vs K
    ├── band_diagram_K_values.png           # Band diagram vs K
    ├── surface_potential_K_values.png      # Surface potential vs K
    └── electric_field_K_values.png         # Peak electric field (Cavity sweep verified)
```

## 3. Disambiguation Summary

Detailed forensic verification of every plot is documented in [docs/audit_report.md](../docs/audit_report.md) and [docs/results_interpretation.md](../docs/results_interpretation.md).
