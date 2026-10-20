# Simulation Results Analysis and Physics Interpretation
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)

---

## 1. Master Result Inventory

This inventory systematically catalogues all simulation outputs, their physical quantity, swept parameters, observable trends, and verification status.

| File Path | Physical Quantity | Swept Parameter | Observable Physical Trend | Data Status | Interpretation Status |
|:---|:---|:---|:---|:---|:---|
| `Results/optimization/Ion_K_values.png` | Linear $I_{DS}-V_{GS}$ | $K = 1, 3, 5, 7, 12, 22$ | ON-current increases with $K$ from $\approx 50\ \mu\text{A}/\mu\text{m}$ up to $\approx 200\ \mu\text{A}/\mu\text{m}$ due to heightened gate capacitance and tunneling field | Digitizable | Verified |
| `Results/optimization/Ioff_K_values.png` | Subthreshold $\log(I_{DS})-V_{GS}$ | $K = 1, 3, 5, 7, 12, 22$ | Subthreshold swing steepens dramatically with higher $K$; OFF-state current remains suppressed at $\sim 10^{-17}\text{ A}/\mu\text{m}$ | Digitizable | Verified |
| `Results/optimization/band_diagram_K_values.png` | Energy bands ($E_C, E_V$) | $K = 1, 3, 5, 7, 12, 22$ | Conduction and valence band bending sharpens across $X \approx 40\text{--}60\text{ nm}$, narrowing tunneling width $\lambda$ | Qualitative | Verified |
| `Results/optimization/surface_potential_K_values.png` | Surface potential $\psi_s(x)$ | $K = 1, 3, 5, 7, 12, 22$ | Surface potential across channel increases monotonically from $\approx 0.4\text{ V}$ to $\approx 1.3\text{ V}$ with increasing $K$ | Qualitative | Verified |
| `Results/sensitivity/Ion_Cavity_verified.png` | Linear $I_{DS}-V_{GS}$ | $t_{cav} = 30, 35, 40\text{ nm}$ | Thicker cavity slightly weakens gate electrostatic coupling, modulating ON-state drive current | Digitizable | Verified (Recovered) |
| `Results/sensitivity/Ioff_Cavity_verified.png` | Subthreshold $\log(I_{DS})-V_{GS}$ | $t_{cav} = 30, 35, 40\text{ nm}$ | $I_{OFF}$ varies between $10^{-19}\text{ A}$ and $10^{-16}\text{ A}$; subthreshold slope shifts with cavity dimension | Digitizable | Verified (Recovered) |
| `Results/optimization/electric_field_K_values.png` | Electric field $|E|(x)$ | $t_{cav} = 30, 35, 40\text{ nm}$ | Peak electric field at tunnel junction exceeds $10^6\text{ V/cm}$; modulation localized at cavity edge | Digitizable | Verified (Cavity sweep) |
| `Results/sensitivity/energy_band_Cavity.png` | Energy bands ($CB, VB$) | $t_{cav} = 30, 35, 40\text{ nm}$ | Conduction/valence band profiles for 30 nm, 35 nm, 40 nm show lateral barrier modulation in the cavity region | Qualitative | Verified |
| `Results/sensitivity/surface_potential_Cavity.png` | Surface potential $\psi_s(x)$ | $t_{cav} = 30, 35, 40\text{ nm}$ | Potential shift localized under the nanocavity footprint | Qualitative | Verified |
| `Results/sensitivity/Ion_Cavity.png` | Linear $I_{DS}-V_{GS}$ | $Q_F = -10^{10}, -5\times 10^{11}, -10^{12}\text{ cm}^{-2}$ | Negative charge suppresses drain current, shifting $V_{TH}$ positively | Digitizable | Verified (Negative $Q_F$) |
| `Results/sensitivity/Ioff_Cavity.png` | Subthreshold $\log(I_{DS})-V_{GS}$ | $Q_F = -10^{10}, -5\times 10^{11}, -10^{12}\text{ cm}^{-2}$ | Negative fixed charge lowers off-state leakage by enhancing the source barrier | Digitizable | Verified (Negative $Q_F$) |
| `Results/sensitivity/Surface_potential.png` | Surface potential $\psi_s(x)$ | $Q_F = -10^{10}, -5\times 10^{11}, -10^{12}\text{ cm}^{-2}$ | Potential dip proportional to negative charge density inside the nanocavity | Qualitative | Verified (Negative $Q_F$) |
| `Results/sensitivity/electric field.png` | Electric field $|E|(x)$ | $Q_F = -10^{10}, -5\times 10^{11}, -10^{12}\text{ cm}^{-2}$ | Modulates peak junction electric field near $X \approx 50\text{ nm}$ | Qualitative | Verified (Negative $Q_F$) |
| `Results/sensitivity/band_diagram_QF_negative.png` | Band diagram ($E_C, E_V, E_{fn}, E_{fp}$) | $Q_F = -10^{10}, -5\times 10^{11}, -10^{12}\text{ cm}^{-2}$ | Upward band bending induced by negative charges, widening the tunneling barrier | Qualitative | Verified (Negative $Q_F$) |
| `Results/sensitivity/Ioff_QF_positive.png` | Subthreshold $\log(I_{DS})-V_{GS}$ | $Q_F = +10^{10}, +5\times 10^{11}, +10^{12}\text{ cm}^{-2}$ | Positive charge induces downward band bending, shifting $V_{TH}$ negatively and elevating $I_{OFF}$ to $10^{-13}\text{--}10^{-11}\text{ A}$ | Digitizable | Verified (Positive $Q_F$) |
| `Results/sensitivity/electric_field_QF_positive.png` | Electric field $|E|(x)$ | $Q_F = +10^{10}, +5\times 10^{11}, +10^{12}\text{ cm}^{-2}$ | Modulates junction field distribution for positive biomolecule charges | Qualitative | Verified (Positive $Q_F$) |

---

## 2. In-Depth Sweep Physics Analysis

### A. Cavity-Thickness Sweep ($30\text{ nm}, 35\text{ nm}, 40\text{ nm}$)
1. **Electrostatic Coupling**:
   - The nanocavity represents a low-permittivity region ($\kappa_{air} = 1.0$) situated between the gate electrode and the silicon channel.
   - Increasing the cavity thickness from $30\text{ nm}$ to $40\text{ nm}$ increases the effective oxide thickness ($EOT$), lowering the local gate capacitance ($C_g$).
2. **Impact on Tunneling**:
   - The peak electric field at the source-channel tunneling interface decreases slightly as the cavity thickness increases (`Results/optimization/electric_field_K_values.png`), widening the spatial tunneling barrier $\lambda$.
   - Consequently, the ON-state current shows a gradual decrease with increasing cavity thickness.
3. **Biosensor Design Trade-off**:
   - While a thinner cavity ($30\text{ nm}$) provides stronger gate-to-channel capacitive coupling and higher drive current, real biomolecules (e.g., antibodies with hydrodynamic radii $\sim 10\text{--}15\text{ nm}$) require sufficient physical height for fluidic infiltration and binding. Thus, $30\text{--}40\text{ nm}$ provides an optimal steric window.

### B. Ferroelectric Dielectric Constant ($K$) Sweep ($K = 1, 3, 5, 7, 12, 22$)
1. **Gate Capacitance Scaling**:
   - As $K$ increases from $1$ (air-like) to $22$ ($\text{HfO}_2$-like ferroelectric), the equivalent gate capacitance $C_{fe} = \frac{\epsilon_0 K}{t_{fe}}$ increases more than 20-fold.
2. **Channel Potential & Band Bending**:
   - In `Results/optimization/surface_potential_K_values.png`, the surface potential increases across the channel, providing much stronger electrostatic inversion/modulation.
   - In `Results/optimization/band_diagram_K_values.png`, the valence band in the source and the conduction band in the channel achieve greater energetic overlap, drastically thinning the tunneling distance $\lambda$.
3. **Subthreshold Swing ($SS$) & Current Ratio**:
   - At $K=22$, the subthreshold transfer curve demonstrates sharp transition with high current ratio ($I_{ON}/I_{OFF} > 10^{12}$), showing the advantage of high-$K$/ferroelectric gate integration in TFETs.

### C. Ferroelectric Fixed Charge ($Q_F$) Polarity Sweep
1. **Biomolecule Charge Emulation**:
   - Fixed interface charge $Q_F$ directly emulates the native net charge of captured biomolecules.
2. **Negative Charge Transduction ($Q_F = -10^{10}\text{ to }-10^{12}\text{ cm}^{-2}$)**:
   - Negative charge produces an opposing electrostatic field, repelling channel electrons and elevating the conduction band edge ($E_C$).
   - This widens the tunneling barrier $\lambda$, shifting the transfer curve to the right (positive $\Delta V_{TH}$) and reducing $I_{OFF}$.
3. **Positive Charge Transduction ($Q_F = +10^{10}\text{ to }+10^{12}\text{ cm}^{-2}$)**:
   - Positive charge attracts channel electrons and pulls down the energy bands, creating premature tunneling at lower gate biases.
   - This causes a leftward threshold shift (negative $\Delta V_{TH}$) and increases subthreshold leakage current ($I_{OFF}$).
