# Repository Audit and Project Inventory
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)  
**Date:** October 20, 2026

---

## 1. Executive Summary

A comprehensive forensic audit of the entire Git repository, its commit history, and all stored graphic outputs was conducted using file-hash comparisons, commit archaeology, and optical character recognition (OCR) of the Synopsys Sentaurus Inspect / SVisual simulation graphics.

### Key Audit Findings
1. **Repository Composition**: The repository contains **38 files** across 9 directories. All TCAD outputs currently exist as exported raster graphics (`.png`) and one one-line text file. No native Sentaurus input decks (`.cmd`, `.scm`), grid files (`.tdr`, `.grd`), or raw numerical data tables (`.plt`, `.dat`, `.csv`) are present in the current working tree.
2. **Critical File Misattributions & Duplicates**:
   - Four files labeled as "QF Neutral" in `Results/electrical/` and `figures/electrical/` are byte-for-byte identical duplicates of the ferroelectric dielectric constant ($K$) sweep files in `Results/optimization/`.
   - The file `Results/optimization/electric_field_K_values.png` is actually a **Cavity Thickness** sweep ($30\text{ nm}, 35\text{ nm}, 40\text{ nm}$), not a $K$-value sweep.
   - The files `Results/sensitivity/Ion_Cavity.png` and `Results/sensitivity/Ioff_Cavity.png` (and their copies in `figures/sensing/`) do **not** represent cavity variations; their axis legends explicitly reveal them to be **Negative Fixed Charge ($Q_F = -1\times 10^{10}, -5\times 10^{11}, -1\times 10^{12}\text{ cm}^{-2}$)** sweeps.
3. **Recovery of Lost Simulation Results from Git History**:
   - In earlier commits (`b1f503b9` and `a1065d55`), genuine cavity thickness transfer characteristics (`Ion.png` and `ioff.png` with curves for $30\text{ nm}, 35\text{ nm}, 40\text{ nm}$) were uploaded under `Results/Diff_Cavity_Length/`, but were inadvertently replaced during directory restructuring. These genuine files have been located in Git objects (`blob 98ca6334` and `blob c2848678`) and can be restored.
4. **Verified Underlying Simulation Space**:
   - The simulations represent three distinct parametric investigations:
     1. **Ferroelectric Dielectric Constant ($K$)**: $K \in \{1, 3, 5, 7, 12, 22\}$.
     2. **Nanocavity Dimension**: Cavity thickness/length $\in \{30\text{ nm}, 35\text{ nm}, 40\text{ nm}\}$.
     3. **Fixed Interface Charge ($Q_F$)**:
        - Negative: $Q_F \in \{-10^{10}, -5\times 10^{11}, -10^{12}\text{ cm}^{-2}\}$
        - Positive: $Q_F \in \{+10^{10}, +5\times 10^{11}, +10^{12}\text{ cm}^{-2}\}$
   - Total device transport length ($X$-axis): $0.15\ \mu\text{m}$ ($150\text{ nm}$).
   - Gate bias sweep range ($V_{GS}$): $0.0\text{ V}$ to $1.5\text{ V}$.

---

## 2. Complete File & Directory Inventory

```text
FE-DGDM-JLTFET-Biosensor-TCAD/
├── .gitignore
├── LICENSE (MIT)
├── README.md
├── analysis/scripts/README.md
├── documents/README.md
├── figures/
│   ├── README.md
│   ├── electrical/ (id_vgs_qf_neutral.png, ioff_vgs_qf_neutral.png)
│   ├── optimization/ (ion_k_values.png, ioff_k_values.png)
│   ├── physics/ (electric_field_distribution.png)
│   └── sensing/ (ion_cavity.png, ioff_cavity.png)
├── parameter/README.md
├── Results/
│   ├── README.md
│   ├── electrical/ (band_diagram_QF_neutral.png, Ioff_QF_neutral.png, Ion_QF_neutral.png, surface_potential_QF_neutral.png)
│   ├── optimization/ (band_diagram_K_values.png, electric_field_K_values.png, Ioff_K_values.png, Ion_K_values.png, surface_potential_K_values.png)
│   └── sensitivity/ (Description_Cavity_Length.txt, band_diagram_QF_negative.png, electric field.png, electric_field_QF_positive.png, energy_band_Cavity.png, Ioff_Cavity.png, Ioff_QF_positive.png, Ion_Cavity.png, Surface_potential.png, surface_potential_Cavity.png)
├── sde/structure/README.md
├── sdevice/device/README.md
├── sdevice/physics/README.md
└── simulations/README.md
```

---

## 3. Disambiguation & Classification Table of Output Files

| Hash Prefix | Inspected Paths | True Verified Physical Content | Parameter Range | Corrected Context |
|:---|:---|:---|:---|:---|
| `700154F0` | `Results/electrical/Ion_QF_neutral.png`<br>`Results/optimization/Ion_K_values.png` | Linear $I_{DS}-V_{GS}$ transfer curve | $V_{GS} \in [0, 1.5]\text{ V}$, $K \in \{1, 3, 5, 7, 12, 22\}$ | Ferroelectric $K$-sweep ($I_{DS}$ up to $200\ \mu\text{A}/\mu\text{m}$) |
| `83917187` | `Results/electrical/Ioff_QF_neutral.png`<br>`Results/optimization/Ioff_K_values.png` | Log $\log(I_{DS})-V_{GS}$ subthreshold curve | $V_{GS} \in [0, 1.5]\text{ V}$, $K \in \{1, 3, 5, 7, 12, 22\}$ | Ferroelectric $K$-sweep subthreshold ($I_{DS} \in [10^{-18}, 1]\text{ A}$) |
| `BA1AF4CD` | `Results/electrical/band_diagram_QF_neutral.png`<br>`Results/optimization/band_diagram_K_values.png` | Energy band profile ($E_C, E_V$) | $X \in [0, 0.15]\ \mu\text{m}$, $K \in \{1, 3, 5, 7, 12, 22\}$ | Band bending vs ferroelectric $K$ |
| `80B4621F` | `Results/electrical/surface_potential_QF_neutral.png`<br>`Results/optimization/surface_potential_K_values.png` | Electrostatic potential profile | $X \in [0, 0.15]\ \mu\text{m}$, $K \in \{1, 3, 5, 7, 12, 22\}$ | Channel potential vs ferroelectric $K$ |
| `3C88EDD3` | `Results/optimization/electric_field_K_values.png`<br>`figures/physics/electric_field_distribution.png` | Electric field profile | $X \in [0, 0.15]\ \mu\text{m}$, $t_{cav} \in \{30, 35, 40\}\text{ nm}$ | Peak electric field vs Cavity Thickness |
| `42DF65A6` | `Results/sensitivity/Ion_Cavity.png`<br>`figures/sensing/ion_cavity.png` | Linear $I_{DS}-V_{GS}$ transfer curve | $V_{GS} \in [0, 1.5]\text{ V}$, $Q_F \in \{-10^{10}, -5\times 10^{11}, -10^{12}\}\text{ cm}^{-2}$ | Negative $Q_F$ transfer curve (mislabeled as Cavity) |
| `1C13288D` | `Results/sensitivity/Ioff_Cavity.png`<br>`figures/sensing/ioff_cavity.png` | Log $\log(I_{DS})-V_{GS}$ subthreshold curve | $V_{GS} \in [0, 1.5]\text{ V}$, $Q_F \in \{-10^{10}, -5\times 10^{11}, -10^{12}\}\text{ cm}^{-2}$ | Negative $Q_F$ subthreshold curve (mislabeled as Cavity) |
| `2CB4E7F1` | `Results/sensitivity/Surface_potential.png` | Electrostatic potential profile | $X \in [0, 0.15]\ \mu\text{m}$, $Q_F \in \{-10^{10}, -5\times 10^{11}, -10^{12}\}\text{ cm}^{-2}$ | Negative $Q_F$ potential modulation |
| `814E8145` | `Results/sensitivity/electric field.png` | Electric field profile | $X \in [0, 0.15]\ \mu\text{m}$, $Q_F \in \{-10^{10}, -5\times 10^{11}, -10^{12}\}\text{ cm}^{-2}$ | Negative $Q_F$ field profile |
| `A6EE71EF` | `Results/sensitivity/band_diagram_QF_negative.png` | Energy band diagram ($E_C, E_V, E_{fn}, E_{fp}$) | $X \in [0, 0.15]\ \mu\text{m}$, Nodes: $n242, n247, n252$ | Negative $Q_F$ band diagram |
| `C5E48F22` | `Results/sensitivity/Ioff_QF_positive.png` | Log $\log(I_{DS})-V_{GS}$ subthreshold curve | $V_{GS} \in [0, 1.5]\text{ V}$, $Q_F \in \{+10^{10}, +5\times 10^{11}, +10^{12}\}\text{ cm}^{-2}$ | Positive $Q_F$ subthreshold curve |
| `AA65BA94` | `Results/sensitivity/electric_field_QF_positive.png` | Electric field profile | $X \in [0, 0.15]\ \mu\text{m}$, $Q_F \in \{+10^{10}, +5\times 10^{11}, +10^{12}\}\text{ cm}^{-2}$ | Positive $Q_F$ field profile |
| `9291D3DE` | `Results/sensitivity/energy_band_Cavity.png` | Energy band diagram ($CB, VB$) | $X \in [0, 0.15]\ \mu\text{m}$, $t_{cav} \in \{30, 35, 40\}\text{ nm}$ | Cavity thickness band diagram |
| `CC41B48A` | `Results/sensitivity/surface_potential_Cavity.png` | Electrostatic potential profile | $X \in [0, 0.15]\ \mu\text{m}$, $t_{cav} \in \{30, 35, 40\}\text{ nm}$ | Cavity thickness potential profile |
| *(Git blob)* `98ca6334` | Original `Results/Diff_Cavity_Length/Ion.png` | Linear $I_{DS}-V_{GS}$ transfer curve | $V_{GS} \in [0, 1.5]\text{ V}$, $t_{cav} \in \{30, 35, 40\}\text{ nm}$ | Genuine Cavity linear transfer curve |
| *(Git blob)* `c2848678` | Original `Results/Diff_Cavity_Length/ioff.png` | Log $\log(I_{DS})-V_{GS}$ subthreshold curve | $V_{GS} \in [0, 1.5]\text{ V}$, $t_{cav} \in \{30, 35, 40\}\text{ nm}$ | Genuine Cavity subthreshold curve |

---

## 4. Prioritized Improvement Plan

1. **Phase 1**: Author technical documentation of the verified device architecture, TFET band-to-band tunneling physics, and parameter reference (`docs/device_architecture.md`, `docs/parameter_reference.md`).
2. **Phase 2**: Reorganize simulation outputs into unambiguous directory hierarchy, restoring the missing cavity thickness curves from Git history.
3. **Phase 3**: Develop Python digitizer/extraction scripts (`analysis/scripts/extract_metrics.py`) to generate structured CSV tables with $I_{ON}$, $I_{OFF}$, $I_{ON}/I_{OFF}$, $V_{TH}$, and $SS$.
4. **Phase 4**: Create publication-grade Matplotlib comparison figures and a clean cross-sectional device architecture diagram.
5. **Phase 5**: Update folder structure and `.gitignore`.
6. **Phase 6**: Rewrite `README.md` to a publication-grade standard.
7. **Phase 7 & 8**: Accurately document the internship scope and add authentic literature citations.
8. **Phase 9 & 10**: Verify link integrity, then commit and push each phase individually.
