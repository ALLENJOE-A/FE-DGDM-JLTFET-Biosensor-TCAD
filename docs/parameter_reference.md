# Device & Simulation Parameter Reference
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)  
**Authors:** Allen Joe A (24BVD1100), Guided by: Lakshmi B  
**Reference:** IEEE Sensors Journal, Vol. 24, No. 22, pp. 37923-37930 (Nov 2024)

---

## 1. Verified Device Geometry & Physical Parameters

All parameters below have been verified directly from the Sentaurus Structure Editor (`sde_dvs.tcl`), Sentaurus Device (`sdevice_des.tcl`), and parameter (`sdevice.par`) input files:

| Parameter | Symbol | Value | Unit | Source File or Evidence |
|:---|:---|:---:|:---:|:---|
| **Total Transport Length** | $L_{total}$ | 158 (0.158) | nm ($\mu\text{m}$) | `sde/structure/sde_dvs.tcl` (X from 0.000 to 0.158 $\mu\text{m}$) |
| **Main Source Length** | $L_S$ | 10 | nm | `sde/structure/sde_dvs.tcl` ($X \in [0.000, 0.010]\ \mu\text{m}$) |
| **Main Source Height** | $H_S$ | 22 | nm | `sde/structure/sde_dvs.tcl` ($Y \in [-0.011, +0.011]\ \mu\text{m}$) |
| **Source Wings Length** | $L_{wing}$ | 45 | nm | `sde/structure/sde_dvs.tcl` ($X \in [0.010, 0.055]\ \mu\text{m}$) |
| **Source Wings Thickness** | $T_{wing}$ | 2 | nm | `sde/structure/sde_dvs.tcl` ($Y \in [\pm 0.009, \pm 0.011]\ \mu\text{m}$) |
| **Source Doping Active** | $N_{S}$ | $1.0 \times 10^{19}$ | $\text{cm}^{-3}$ | `sde/structure/sde_dvs.tcl` (`ConstantProfileDefinition.source`, As) |
| **Channel Body Length** | $L_{ch}$ | 93 | nm | `sde/structure/sde_dvs.tcl` ($X \in [0.010, 0.103]\ \mu\text{m}$) |
| **Channel Silicon Thickness** | $T_{ch}$ | 10 | nm | `sde/structure/sde_dvs.tcl` ($Y \in [-0.005, +0.005]\ \mu\text{m}$) |
| **Channel Doping Active** | $N_{ch}$ | $1.0 \times 10^{15}$ | $\text{cm}^{-3}$ | `sde/structure/sde_dvs.tcl` (`ConstantProfileDefinition.channel`, As) |
| **Drain Extension Length** | $L_{ext}$ | 45 | nm | `sde/structure/sde_dvs.tcl` ($X \in [0.103, 0.148]\ \mu\text{m}$) |
| **Drain Extension Thickness**| $T_{ext}$ | 16 | nm | `sde/structure/sde_dvs.tcl` ($Y \in [-0.008, +0.008]\ \mu\text{m}$) |
| **Drain Extension Doping** | $N_{ext}$ | $1.0 \times 10^{15}$ | $\text{cm}^{-3}$ | `sde/structure/sde_dvs.tcl` (`ConstantProfileDefinition.channelde`, As) |
| **Main Drain Length** | $L_D$ | 10 | nm | `sde/structure/sde_dvs.tcl` ($X \in [0.148, 0.158]\ \mu\text{m}$) |
| **Main Drain Thickness** | $T_D$ | 18 | nm | `sde/structure/sde_dvs.tcl` ($Y \in [-0.009, +0.009]\ \mu\text{m}$) |
| **Drain Doping Active** | $N_{D}$ | $1.0 \times 10^{20}$ | $\text{cm}^{-3}$ | `sde/structure/sde_dvs.tcl` (`ConstantProfileDefinition.drain`, As) |
| **Interfacial Oxide** | $T_{ox}$ | 1 | nm | `sde/structure/sde_dvs.tcl` ($\text{SiO}_2$, $Y \in [\pm 0.005, \pm 0.006]\ \mu\text{m}$) |
| **Underlap Oxide Thickness**| $T_{under}$ | 3 | nm | `sde/structure/sde_dvs.tcl` ($\text{SiO}_2$, $X \in [0.010, 0.045]\ \mu\text{m}$) |
| **Nanocavity Length** | $L_{cav}$ | 30 (35, 40 swept) | nm | `sde/structure/sde_dvs.tcl` ($X \in [0.045, 0.075]\ \mu\text{m}$) |
| **Nanocavity Thickness** | $T_{cav}$ | 3 | nm | `sde/structure/sde_dvs.tcl` ($Y \in [\pm 0.006, \pm 0.009]\ \mu\text{m}$) |
| **Ferroelectric Stack Length**| $L_{FE}$ | 28 | nm | `sde/structure/sde_dvs.tcl` ($X \in [0.075, 0.103]\ \mu\text{m}$) |
| **Ferroelectric Thickness** | $T_{FE}$ | 3 | nm | `sde/structure/sde_dvs.tcl` ($\text{Si:HfO}_2$, $Y \in [\pm 0.006, \pm 0.009]\ \mu\text{m}$) |
| **Gate Electrode Length** | $L_G$ | 58 | nm | `sde/structure/sde_dvs.tcl` (spans cavity + $\text{HfO}_2$ stack) |

---

## 2. Ferroelectric & Material Physics Parameters

| Physical Parameter | Symbol | Value | Unit | Definition / Model Context |
|:---|:---|:---:|:---:|:---|
| **$\text{HfO}_2$ Permittivity** | $\epsilon_{FE}$ | 31.0 | — | Relative permittivity in `parameter/sdevice.par` |
| **Landau Parameter $\alpha$** | $\alpha$ | $-3.7 \times 10^{10}$ | cm/F | Negative stiffness enabling Negative Capacitance |
| **Landau Parameter $\beta$** | $\beta$ | $2.5 \times 10^{21}$ | $\text{cm}^5/(\text{F}\cdot\text{C}^2)$ | Higher-order polarization stability coefficient |
| **Remanent Polarization** | $P_r$ | 1.0 | $\mu\text{C/cm}^2$ | IEEE Sensors Journal reference calibration |
| **Saturation Polarization** | $P_s$ | 20.0 | $\mu\text{C/cm}^2$ | IEEE Sensors Journal reference calibration |
| **Coercive Field** | $E_c$ | 1.0 | MV/cm | IEEE Sensors Journal reference calibration |
| **Hurkx BTBT Parameter A** | $A$ | $8.9770 \times 10^{20}$ | $\text{cm}^{-1}\text{s}^{-1}\text{V}^{-2}$ | Silicon band-to-band tunneling rate prefactor |
| **Hurkx BTBT Parameter B** | $B$ | $2.1466 \times 10^{7}$ | V/cm | Silicon exponential tunneling field parameter |
| **Phonon Energy** | $\hbar\Omega$ | 0.0186 | eV | Transverse acoustic phonon assistance in Silicon |
| **Silicon Bandgap** | $E_{g0}$ | 1.12 | eV | Room temperature intrinsic bandgap |
| **Electron Affinity (Si)** | $\chi_0$ | 4.05 | eV | Electron affinity for Silicon |
| **$\text{SiO}_2$ Permittivity** | $\epsilon_{ox}$ | 3.9 | — | Interfacial and underlap oxide relative permittivity |
| **$\text{SiO}_2$ Bandgap** | $E_{g,ox}$ | 9.0 | eV | Energy bandgap for $\text{SiO}_2$ |

---

## 3. Biological Analyte Mapping (Dielectric Constant $K$)

In the dielectric modulation biosensing runs, the nanocavity relative permittivity is modulated to model immobilization of specific target biomolecules:

| Dielectric Constant ($K$) | Target Biological Analyte | Clinical / Biological Relevance |
|:---:|:---|:---|
| **$K = 1$** | Air Reference | Baseline empty/unbound nanocavity ($I_{DS} = 0.2040\text{ mA}$) |
| **$K = 3$** | Lipids / Cellular Membranes | Non-polar biological fatty acids, lipid bilayers |
| **$K = 5$** | Carbohydrates | Polysaccharides, glucose oligomers |
| **$K = 7$** | Zein Protein | Plant seed storage protein (corn prolamin) |
| **$K = 12$** | Amino Acids | Peptides, zwitterionic amino acid complexes |
| **$K = 22$** | MDA-MB-231 Breast Cancer Cells | Human epithelial adenocarcinoma breast cancer cell line |

---

## 4. Simulation Biasing and Mesh Settings

| Setting | Symbol | Value | Unit | Description |
|:---|:---|:---:|:---:|:---|
| **Drain Voltage** | $V_{DS}$ | 1.0 | V | Quasistationary goal bias applied to drain electrode |
| **Gate Sweep Voltage** | $V_{GS}$ | $0.0 \rightarrow 1.5$ | V | Quasistationary sweep goal with fine adaptive step size |
| **Simulation Temperature** | $T$ | 300 | K | Hydrodynamic transport room temperature |
| **Global Mesh Size** | $\Delta x, \Delta y$ | $2.0 \times 0.2$ | nm | Global device refinement window (`RefEvalWin.all`) |
| **Active Tunneling Mesh** | $\Delta x_{min}, \Delta y_{min}$ | $1.0 \times 0.1$ | nm | Sub-nanometer multibox at source-channel interface |
| **Transport Model** | — | Hydrodynamic | — | Coupled energy-balance Poisson and electron continuity |
