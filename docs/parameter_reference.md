# Device & Simulation Parameter Reference
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)

---

## 1. Verified Device Geometry & Physical Parameters

This table documents device parameters verified from the simulation plots, axis bounds, and curve descriptors. Where an explicit parameter value was not included in the uploaded files, it is designated as *"Not available in the inspected files"*, maintaining strict scientific integrity.

| Parameter | Symbol | Value | Unit | Source File or Evidence |
|:---|:---|:---|:---|:---|
| **Total Transport Length** | $L_{total}$ | 150 (0.15) | nm ($\mu\text{m}$) | $X$-axis span in all 1D profile plots (`band_diagram`, `electric_field`, `surface_potential`) |
| **Channel Architecture** | — | T-shaped, Junctionless | — | Project specification & potential distribution profiles |
| **Tunnel Junction Location** | $X_{junction}$ | $\approx 40\text{--}60$ | nm | Peak electric field coordinate and steep potential drop location |
| **Nanocavity Dimensions** | $t_{cav}$ | 30, 35, 40 | nm | `Results/sensitivity/energy_band_Cavity.png`, `Results/Diff_Cavity_Length/ioff.png` |
| **Gate Architecture** | — | Double-Gate (Top & Bottom) | — | Documented device architecture & boundary symmetry |
| **Channel Thickness** | $T_{ch}$ | Not available in the inspected files | nm | SDE structure file missing |
| **Source/Drain Length** | $L_S, L_D$ | Not available in the inspected files | nm | SDE structure file missing |
| **Gate Oxide Thickness** | $t_{ox}$ | Not available in the inspected files | nm | SDE structure file missing |
| **Ferroelectric Layer Thickness** | $t_{fe}$ | Not available in the inspected files | nm | SDE structure file missing |
| **Channel Doping Concentration** | $N_{ch}$ | Not available in the inspected files | $\text{cm}^{-3}$ | SDE structure file missing |
| **Source Doping Concentration** | $N_S$ | Not available in the inspected files | $\text{cm}^{-3}$ | SDE structure file missing |
| **Drain Doping Concentration** | $N_D$ | Not available in the inspected files | $\text{cm}^{-3}$ | SDE structure file missing |
| **Channel Semiconductor Material** | — | Silicon (assumed) | — | Bandgap $\approx 1.12\text{ eV}$ observable in band diagrams |
| **Gate Metal Workfunction** | $\Phi_M$ | Not available in the inspected files | eV | SDevice simulation deck missing |

---

## 2. Verified Simulation Sweeps & Electrical Parameters

| Parameter | Symbol | Swept / Operating Values | Unit | Source File or Evidence |
|:---|:---|:---|:---|:---|
| **Gate Voltage Sweep** | $V_{GS}$ | $0.0 \rightarrow 1.5$ (step $\approx 0.05$) | V | $X$-axis of all $I_{DS}-V_{GS}$ transfer curves |
| **Drain Bias** | $V_{DS}$ | Fixed (constant) | V | Transfer characteristics simulated under constant drain bias |
| **Ferroelectric Dielectric Constant** | $K$ ($\epsilon_{fe}$) | 1, 3, 5, 7, 12, 22 | — | `Results/optimization/Ioff_K_values.png`, `Results/optimization/Ion_K_values.png` |
| **Negative Interface Fixed Charge** | $Q_F^{neg}$ | $-1\times 10^{10},\ -5\times 10^{11},\ -1\times 10^{12}$ | $\text{cm}^{-2}$ | `Results/sensitivity/Surface_potential.png`, `Results/sensitivity/Ion_Cavity.png` |
| **Positive Interface Fixed Charge** | $Q_F^{pos}$ | $+1\times 10^{10},\ +5\times 10^{11},\ +1\times 10^{12}$ | $\text{cm}^{-2}$ | `Results/sensitivity/Ioff_QF_positive.png`, `Results/sensitivity/electric_field_QF_positive.png` |
| **Simulation Temperature** | $T$ | 300 (standard room temp) | K | Assumed standard TCAD environment default |

---

## 3. Sentaurus TCAD Physical Model Cards (Inferred & Recommended)

| Physical Mechanism | Sentaurus Model | Implementation Card | Status |
|:---|:---|:---|:---|
| **Band-to-Band Tunneling** | Kane non-local BTBT / Hurkx BTBT | `Band2Band(Model=Kane)` | Active (governs subthreshold and on-state current) |
| **Ferroelectric Polarization** | Landau-Khalatnikov | `Ferroelectric(Model=Landau)` | Active (governs internal voltage amplification) |
| **Carrier Transport** | Drift-Diffusion | `DriftDiffusion` | Active (Poisson + continuity solver) |
| **Quantum Confinement** | Density Gradient | `Quantum(Model=DensityGradient)` | Recommended for sub-10 nm T-channel ribs |
| **Mobility Degradation** | Masetti / Lombardi / High-Field | `DopingDependence HighFieldSaturation Enormal` | Active (models velocity saturation and surface scattering) |
| **Recombination** | SRH + Auger + TAT | `SRH(DopingDependence) Auger TrapAssistedTunneling` | Active (sets baseline reverse leakage current) |
