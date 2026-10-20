# FE-DGDM-JLTFET Biosensor: TCAD Modeling & Analysis

[![Language: Tcl 100%](https://img.shields.io/badge/Language-Tcl%20100%25-blue.svg)](sde/structure/sde_dvs.tcl)
[![TCAD: Synopsys Sentaurus](https://img.shields.io/badge/TCAD-Synopsys%20Sentaurus-red.svg)](docs/simulation_methodology.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status: Internship Portfolio](https://img.shields.io/badge/Status-Completed%20Internship-orange.svg)](docs/results_interpretation.md)

> **TCAD simulation, electrostatic modeling, and sensitivity analysis of a Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel Field-Effect Transistor (FE-DGDM-JLTFET) featuring a T-shaped channel and inverted-T nanocavity for label-free biomolecule detection.**

---

## Abstract

Point-of-care disease diagnostics and early cancer screening require ultra-sensitive, label-free transducers operating beyond the thermodynamic thermal subthreshold limit ($SS \ge 60\text{ mV/dec}$ at $300\text{ K}$). This repository documents the research and simulation outputs of a one-month internship evaluating a novel **Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) biosensor** designed in **Synopsys Sentaurus TCAD**. 

The device architecture integrates internal voltage amplification via a doped $\text{Si:HfO}_2$ ferroelectric negative-capacitance stack, quantum band-to-band tunneling (BTBT) across an electrostatically modulated junctionless body, a **T-shaped channel** with lateral source wings, and dual **inverted-T nanocavities** for biomolecule immobilization. 

Using Sentaurus Structure Editor (SDE) and Sentaurus Device (SDevice), extensive parametric sweeps were executed across:
1. **Nanocavity length** ($L_{cav} = 30\text{ nm}, 35\text{ nm}, 40\text{ nm}$),
2. **Biomolecule dielectric constant** ($K = 1\text{ to }22$, spanning air, lipids, carbohydrates, zein protein, amino acids, and **MDA-MB-231 breast cancer cells**),
3. **Fixed charge polarity and concentration** ($Q_F = \pm 10^{10}\text{ to }\pm 10^{12}\text{ cm}^{-2}$).

The optimized 30 nm cavity achieves an outstanding drive current of **$0.8040\text{ mA}$** and an $I_{ON}/I_{OFF}$ ratio of **$7.24 \times 10^8$**. In dielectric modulation sensing against the air reference ($K = 1, I_{DS} = 0.2040\text{ mA}$), current sensitivity reaches **$18.137\%$** for MDA-MB-231 breast cancer cells, establishing the design as a viable platform for clinical biosensing.

---

## Device Architecture & Grounded TCAD Geometry

The device architecture is directly verified from the Sentaurus Structure Editor input deck ([`sde/structure/sde_dvs.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/sde/structure/sde_dvs.tcl)) with an exact physical transport length of **158 nm** ($X \in [0.000, 0.158]\ \mu\text{m}$):

![FE-DGDM-JLTFET Device Schematic](figures/device/device_architecture_schematic.png)

### SDE Geometric Specifications

| Region | Material | $X$ Span (nm) | Length (nm) | $Y$ Coordinates ($\mu\text{m}$) | Thickness (nm) | Doping ($N_D$, $\text{cm}^{-3}$) |
|:---|:---|:---:|:---:|:---:|:---:|:---:|
| **Source (`source`)** | Silicon | $0 \rightarrow 10$ | 10 | $[-0.011, +0.011]$ | 22 | Arsenic $10^{19}$ |
| **Top Source Wing (`sourcet`)** | Silicon | $10 \rightarrow 55$ | 45 | $[-0.011, -0.009]$ | 2 | Arsenic $10^{19}$ |
| **Bottom Source Wing (`sourceb`)**| Silicon | $10 \rightarrow 55$ | 45 | $[+0.009, +0.011]$ | 2 | Arsenic $10^{19}$ |
| **Channel Body (`channel`)** | Silicon | $10 \rightarrow 103$ | 93 | $[-0.005, +0.005]$ | 10 ($T_{ch}$) | Arsenic $10^{15}$ |
| **Interfacial Oxide (`oxide1, 2`)**| $\text{SiO}_2$ | $10 \rightarrow 103$ | 93 | $[\pm 0.005, \pm 0.006]$ | 1 ($T_{ox}$) | Undoped |
| **Underlap Oxide (`sio2t, b`)** | $\text{SiO}_2$ | $10 \rightarrow 45$ | 35 | $[\pm 0.006, \pm 0.009]$ | 3 | Undoped |
| **Nanocavity (`vac1, vac2`)** | Vacuum / Biomolecules | $45 \rightarrow 75$ | 30 ($L_{cav}$) | $[\pm 0.006, \pm 0.009]$ | 3 ($T_{cav}$) | Undoped ($K=1\text{--}22$) |
| **Ferroelectric Stack (`hfo2t, b`)**| Doped $\text{Si:HfO}_2$ | $75 \rightarrow 103$ | 28 ($L_{FE}$) | $[\pm 0.006, \pm 0.009]$ | 3 ($T_{FE}$) | Undoped ($\epsilon_r = 31$) |
| **Drain Extension (`channelde`)** | Silicon | $103 \rightarrow 148$ | 45 | $[-0.008, +0.008]$ | 16 | Arsenic $10^{15}$ |
| **Extension Oxide (`oxide3, 4`)** | $\text{SiO}_2$ | $103 \rightarrow 148$ | 45 | $[\pm 0.008, \pm 0.009]$ | 1 | Undoped |
| **Drain (`drain`)** | Silicon | $148 \rightarrow 158$ | 10 | $[-0.009, +0.009]$ | 18 | Arsenic $10^{20}$ |

### Operating Mechanisms
- **T-Shaped Source & Channel**: Extended lateral source wings (`sourcet`, `sourceb`) increase the active tunneling surface area at the $X = 10\text{ nm}$ interface and shield the channel from drain-induced electrostatic penetration.
- **Inverted-T Nanocavity**: Sited in the gate-source underlap region ($X \in [45, 75]\text{ nm}$), immobilizing target analytes immediately adjacent to the tunneling barrier where electrostatic perturbation is strongest.
- **Negative Capacitance Amplification**: The 3 nm $\text{Si:HfO}_2$ ferroelectric layer exhibits negative stiffness ($\alpha = -3.7 \times 10^{10}\text{ cm/F}$, $\beta = 2.5 \times 10^{21}\text{ cm}^5/\text{F}\cdot\text{C}^2$), magnifying the internal gate surface potential ($\partial \psi_s / \partial V_{GS} > 1$).

---

## Sentaurus TCAD Decks (100% Tcl Codebase)

All input decks and workbench automation are supplied in standard Tcl format for complete reproducibility:
- [`sde/structure/sde_dvs.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/sde/structure/sde_dvs.tcl) — SDE geometry, region definitions, contacts, and mesh commands.
- [`sdevice/device/sdevice_des.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/sdevice/device/sdevice_des.tcl) — SDevice physics cards, solvers, and quasistationary ramp sequences.
- [`sdevice/physics/physics_models.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/sdevice/physics/physics_models.tcl) — Transport, Hurkx non-local BTBT, and ferroelectric models.
- [`parameter/sdevice.par`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/parameter/sdevice.par) — Calibrated material parameters for Silicon, $\text{SiO}_2$, $\text{HfO}_2$, and Vacuum.
- [`simulations/fe_dgdm_jltfet_simulation.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/simulations/fe_dgdm_jltfet_simulation.tcl) — SWB parametric sweep automation deck.

---

## Experimental Simulation Findings

### 1. Cavity Length Optimization ($L_{cav} = 30, 35, 40\text{ nm}$)

Evaluated at $V_{DS} = 1.0\text{ V}$ and empty cavity baseline:

| Cavity Length ($L_{cav}$) | $V_{th}$ (V) | $I_{ON}$ (mA) | $I_{OFF}$ (A) | $I_{ON}/I_{OFF}$ Ratio | $g_m$ (mS) | $SS$ (mV/dec) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **30 nm** | **0.4010** | **0.8040** | $1.11 \times 10^{-12}$ | **$7.2432 \times 10^8$** | 0.6110 | 61.0 |
| **35 nm** | 0.3969 | 0.1970 | $1.12 \times 10^{-12}$ | $1.7589 \times 10^8$ | 0.6099 | 59.0 |
| **40 nm** | 0.3969 | 0.1908 | $1.10 \times 10^{-12}$ | $1.7345 \times 10^8$ | 0.6135 | 59.8 |

![Cavity Length Sweep](figures/sensing/cavity_thickness_transfer_characteristics.png)

> **Key Finding:** The 30 nm cavity length delivers over **$4\times$ higher drive current** ($0.8040\text{ mA}$) than 35 nm or 40 nm while maintaining identical off-state leakage ($1.1 \times 10^{-12}\text{ A}$), yielding the maximum switching ratio of $7.24 \times 10^8$.

---

### 2. Biomolecule Dielectric Constant ($K$) Modulation & Sensitivity

Simulating immobilization of specific target biomolecules inside the 30 nm nanocavity:

| Dielectric Constant ($K$) | Biological Analyte | $V_{th}$ (V) | $I_{ON} / I_{DS}$ (mA) | $I_{ON}/I_{OFF}$ Ratio | $g_m$ (mS) | Calculated Sensitivity (%) |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| **1** | Air (Reference) | *Unreported* | **0.2040** | *Unreported* | *Unreported* | **0.000 %** |
| **3** | Lipids | 0.4139 | 0.2050 | $1.5769 \times 10^8$ | *Unreported* | **0.490 %** |
| **5** | Carbohydrates | 0.4080 | 0.2120 | $1.7097 \times 10^8$ | 0.430 | **3.922 %** |
| **7** | Zein Protein | 0.4055 | 0.2160 | $1.9817 \times 10^8$ | 0.550 | **5.882 %** |
| **12** | Amino Acids | 0.4020 | 0.2257 | $2.0706 \times 10^8$ | 0.582 | **10.637 %** |
| **22** | MDA-MB-231 (Breast Cancer) | **0.3910** | **0.2410** | **$1.8538 \times 10^8$** | **0.650** | **18.137 %** |

![K-Sweep Transfer Characteristics](figures/electrical/k_sweep_transfer_characteristics.png)
![Benchmark Summary](figures/comparative/metrics_benchmark_summary.png)

$$\text{Sensitivity}(I_{DS}) = \frac{|I_{DS}(bio) - I_{DS}(air)|}{I_{DS}(air)} \times 100\%$$

---

### 3. Biomolecule Fixed Charge ($Q_F$) Polarity Sweep

Evaluated for charged biomolecular species immobilized at $K = 22$:

| Charge Polarity | Recorded Charge ($Q_F$, $\text{cm}^{-2}$) | Drain Current $I_{DS}$ (mA) | Physical Effect |
|:---|:---:|:---:|:---|
| **Positive $Q_F$** (Basic proteins / Poly-L-lysine) | $+1.0 \times 10^{10}$ | 0.2416 | Downward band bending, earlier BTBT onset |
| | $+5.0 \times 10^{11}$ | 0.2256 | |
| | $+1.0 \times 10^{12}$ | 0.2178 | |
| **Negative $Q_F$** (DNA / RNA / Acidic proteins) | $-1.0 \times 10^{10}$ | 0.2110 | Upward band bending, widened tunneling barrier |
| | $-5.0 \times 10^{11}$ | 0.2059 | |
| | $-1.0 \times 10^{12}$ | 0.2040 | |

![Fixed Charge Comparison](figures/sensing/fixed_charge_sensitivity_comparison.png)

---

## Project Context & Metadata

- **Author:** Allen Joe A (Registration No: 24BVD1100)
- **Co-Author:** Asvitha R (Registration No: 24BEC1106)
- **Faculty Guide:** Dr. Lakshmi B
- **Institution:** School of Electronics Engineering (SENSE), VIT Chennai
- **Project Duration:** One-Month Internship (August 2026)
- **Primary Reference:** R. Anil Kumar, G. Sravani Kondavitee, G. Wadhwa, and S. R. Karumuri, *"A Novel T-Shape Channel With an Inverted-T Nano-Cavity Label-Free Detection Using Si:HfO2 Ferroelectric DGDM-JLTFET as a Biosensor—A Simulation Study,"* **IEEE Sensors Journal**, vol. 24, no. 22, pp. 37923-37930, Nov. 2024. [DOI: 10.1109/JSEN.2024.3468532](https://doi.org/10.1109/JSEN.2024.3468532).

---

## Reproducibility & Figure Generation

To regenerate all metric tables and publication figures:

```bash
# 1. Clone repository
git clone https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD.git
cd FE-DGDM-JLTFET-Biosensor-TCAD

# 2. Run publication figure generator
python analysis/scripts/plot_publication_figures.py
```
*Detailed reproducibility instructions are provided in [docs/reproducibility.md](docs/reproducibility.md).*

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
