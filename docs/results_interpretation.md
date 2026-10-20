# Simulation Results Analysis and Physics Interpretation
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)  
**Authors:** Allen Joe A (24BVD1100), Guided by: Lakshmi B  
**Reference:** IEEE Sensors Journal, Vol. 24, No. 22, pp. 37923-37930 (Nov 2024)

---

## 1. Master Result Inventory

This inventory systematically maps every original Sentaurus output plot to its physical quantity, swept parameters, and verified interpretation:

| File Path | Physical Quantity | Swept Parameter | Observable Physical Trend | Numerical Data Status | Interpretation |
|:---|:---|:---|:---|:---:|:---:|
| `Results/optimization/Ion_K_values.png` | Linear $I_{DS}-V_{GS}$ | $K = 1, 3, 5, 7, 12, 22$ | $I_{DS}$ increases monotonically from $0.2040\text{ mA}$ (air) to $0.2410\text{ mA}$ ($K=22$) | Extracted in Report | Verified |
| `Results/optimization/Ioff_K_values.png` | Subthreshold $\log(I_{DS})-V_{GS}$ | $K = 1, 3, 5, 7, 12, 22$ | Subthreshold swing stabilizes near $60\text{--}62\text{ mV/dec}$; $I_{OFF} \approx 10^{-12}\text{ A}$ | Extracted in Report | Verified |
| `Results/optimization/band_diagram_K_values.png` | Energy bands ($E_C, E_V$) | $K = 1, 3, 5, 7, 12, 22$ | Conduction and valence band overlap widens with higher $K$, shortening the tunneling barrier width | Qualitative Plot | Verified |
| `Results/optimization/surface_potential_K_values.png` | Surface potential $\psi_s(x)$ | $K = 1, 3, 5, 7, 12, 22$ | Surface potential in the channel body increases with $K$, shifting $V_{th}$ from $0.4139\text{ V}$ to $0.3910\text{ V}$ | Extracted in Report | Verified |
| `Results/sensitivity/Ion_Cavity_verified.png` | Linear $I_{DS}-V_{GS}$ | $L_{cav} = 30, 35, 40\text{ nm}$ | $I_{ON}$ is maximum at $L_{cav} = 30\text{ nm}$ ($0.8040\text{ mA}$), decreasing to $0.1970\text{ mA}$ and $0.1908\text{ mA}$ | Extracted in Report | Verified |
| `Results/sensitivity/Ioff_Cavity_verified.png` | Subthreshold $\log(I_{DS})-V_{GS}$ | $L_{cav} = 30, 35, 40\text{ nm}$ | $I_{OFF}$ remains steady at $\approx 1.1 \times 10^{-12}\text{ A}$, yielding $I_{ON}/I_{OFF} = 7.24 \times 10^8$ at 30 nm | Extracted in Report | Verified |
| `Results/optimization/electric_field_K_values.png` | Electric field $|E|(x)$ | $L_{cav} = 30, 35, 40\text{ nm}$ | Peak electric field at tunnel junction exceeds $10^6\text{ V/cm}$, highest for 30 nm cavity | Extracted in Report | Verified |
| `Results/sensitivity/energy_band_Cavity.png` | Energy bands ($CB, VB$) | $L_{cav} = 30, 35, 40\text{ nm}$ | Tunneling path length is minimum at $L_{cav} = 30\text{ nm}$, enhancing band-to-band tunneling rate | Qualitative Plot | Verified |
| `Results/sensitivity/surface_potential_Cavity.png` | Surface potential $\psi_s(x)$ | $L_{cav} = 30, 35, 40\text{ nm}$ | Potential profile across channel shows optimal coupling for the 30 nm cavity | Qualitative Plot | Verified |
| `Results/sensitivity/Ion_Cavity.png` | Linear $I_{DS}-V_{GS}$ | $Q_F < 0$ ($-10^{10}, -5\times 10^{11}, -10^{12}$) | Negative charge suppresses drain current from $0.2110\text{ mA}$ down to $0.2040\text{ mA}$ | Extracted in Report | Verified |
| `Results/sensitivity/Ioff_Cavity.png` | Subthreshold $\log(I_{DS})-V_{GS}$ | $Q_F < 0$ ($-10^{10}, -5\times 10^{11}, -10^{12}$) | Upward band bending reduces leakage and increases effective threshold voltage | Extracted in Report | Verified |
| `Results/sensitivity/Surface_potential.png` | Surface potential $\psi_s(x)$ | $Q_F < 0$ ($-10^{10}, -5\times 10^{11}, -10^{12}$) | Potential dip proportional to immobilized negative charge density | Qualitative Plot | Verified |
| `Results/sensitivity/electric field.png` | Electric field $|E|(x)$ | $Q_F < 0$ ($-10^{10}, -5\times 10^{11}, -10^{12}$) | Localized field modulation at the nanocavity interface | Qualitative Plot | Verified |
| `Results/sensitivity/band_diagram_QF_negative.png` | Band diagram ($E_C, E_V$) | $Q_F < 0$ ($-10^{10}, -5\times 10^{11}, -10^{12}$) | Upward band bending raises conduction band edge relative to Fermi level | Qualitative Plot | Verified |
| `Results/sensitivity/Ioff_QF_positive.png` | Subthreshold $\log(I_{DS})-V_{GS}$ | $Q_F > 0$ ($+10^{10}, +5\times 10^{11}, +10^{12}$) | Positive charge shifts threshold voltage down, increasing subthreshold current | Extracted in Report | Verified |
| `Results/sensitivity/electric_field_QF_positive.png` | Electric field $|E|(x)$ | $Q_F > 0$ ($+10^{10}, +5\times 10^{11}, +10^{12}$) | Field profiles under positive biomolecule accumulation | Qualitative Plot | Verified |
| `Results/electrical/band_diagram_QF_neutral.png` | Energy bands ($E_C, E_V$) | $Q_F = 0$ (Neutral) | Baseline uncharged equilibrium energy band alignment | Baseline Plot | Verified |
| `Results/electrical/surface_potential_QF_neutral.png`| Surface potential $\psi_s(x)$ | $Q_F = 0$ (Neutral) | Baseline uncharged potential profile | Baseline Plot | Verified |
| `Results/electrical/Ion_QF_neutral.png` | Linear $I_{DS}-V_{GS}$ | $Q_F = 0$ (Neutral) | Baseline transfer characteristic | Baseline Plot | Verified |
| `Results/electrical/Ioff_QF_neutral.png` | Subthreshold $\log(I_{DS})-V_{GS}$ | $Q_F = 0$ (Neutral) | Baseline off-state leakage characteristic | Baseline Plot | Verified |

---

## 2. In-Depth Physical Analysis

### A. Nanocavity Length Optimization ($L_{cav} = 30, 35, 40\text{ nm}$)
1. **Drive Current Sensitivity**:
   - The 30 nm cavity configuration yields $I_{ON} = 0.8040\text{ mA}$, compared to $0.1970\text{ mA}$ at 35 nm and $0.1908\text{ mA}$ at 40 nm.
   - Placing the ferroelectric gate stack closer to the source tunneling interface ($X = 10\text{ nm}$) shortens the screening length and maximizes the localized tunneling electric field.
2. **Switching Performance**:
   - Off-state leakage is consistently suppressed to $\approx 1.1 \times 10^{-12}\text{ A}$ across all three cavity lengths.
   - The resulting switching ratio is highest at $L_{cav} = 30\text{ nm}$ ($I_{ON}/I_{OFF} = 7.2432 \times 10^8$), confirming 30 nm as the optimal design point.

### B. Biomolecule Dielectric Constant ($K$) Modulation
1. **Label-Free Transduction**:
   - An air-filled cavity ($K=1$) provides the baseline reference with $I_{DS} = 0.2040\text{ mA}$.
   - As target biomolecules bind within the nanocavity, local permittivity rises:
     - $K = 3$ (Lipids): $I_{DS} = 0.2050\text{ mA}$, Sensitivity $= 0.490\%$
     - $K = 5$ (Carbohydrates): $I_{DS} = 0.2120\text{ mA}$, Sensitivity $= 3.922\%$
     - $K = 7$ (Zein protein): $I_{DS} = 0.2160\text{ mA}$, Sensitivity $= 5.882\%$
     - $K = 12$ (Amino acids): $I_{DS} = 0.2257\text{ mA}$, Sensitivity $= 10.637\%$
     - $K = 22$ (MDA-MB-231 breast cancer cells): $I_{DS} = 0.2410\text{ mA}$, Sensitivity $= 18.137\%$
2. **Threshold Voltage Shift**:
   - $V_{th}$ drops monotonically from $0.4139\text{ V}$ at $K=3$ down to $0.3910\text{ V}$ at $K=22$ ($\Delta V_{th} = -22.9\text{ mV}$), while transconductance increases from $0.430\text{ mS}$ to $0.650\text{ mS}$.

### C. Biomolecule Fixed-Charge ($Q_F$) Transduction
1. **Charge Sign Discrimination**:
   - Positive charges ($Q_F > 0$, basic proteins) pull down the conduction band edge, facilitating earlier band alignment and shifting the subthreshold curve leftward.
   - Negative charges ($Q_F < 0$, nucleic acids/DNA) push up the conduction band edge, increasing the tunneling distance and shifting the transfer curve rightward.
2. **Dynamic Range**:
   - Across $\pm 10^{10}$ to $\pm 10^{12}\text{ cm}^{-2}$, the drain current modulates predictably, confirming the device's capability to detect both neutral dielectric permittivity and net electrical charges.
