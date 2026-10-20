# Parameter Sweeps and Simulation Findings
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)

---

## 1. Overview

The TCAD investigation examined three orthogonal design parameters to optimize steep-slope switching and quantify label-free biosensing sensitivity:
1. **Ferroelectric Dielectric Constant ($K$)**: Investigated gate-to-channel capacitive matching and negative capacitance internal voltage amplification ($K = 1, 3, 5, 7, 12, 22$).
2. **Nanocavity Thickness ($t_{cav}$)**: Evaluated the trade-off between gate coupling and receptor volume ($t_{cav} = 30, 35, 40\text{ nm}$).
3. **Interface Fixed Charge ($Q_F$)**: Quantified biomolecule electrostatic transduction across negative and positive polarities ($Q_F = \pm 10^{10}, \pm 5\times 10^{11}, \pm 10^{12}\text{ cm}^{-2}$).

---

## 2. Quantitative Findings Summary Table

The following metrics were quantitatively extracted from the simulated transfer characteristics (`Results/raw_data/extracted_metrics_summary.csv`):

| Sweep Parameter | Condition | $I_{ON}$ ($\mu\text{A}/\mu\text{m}$) | $I_{OFF}$ ($\text{A}/\mu\text{m}$) | $I_{ON}/I_{OFF}$ Ratio | $V_{TH}$ (V) | $SS_{avg}$ (mV/dec) |
|:---|:---|:---:|:---:|:---:|:---:|:---:|
| **Ferroelectric $K$** | $K = 22$ ($\text{HfO}_2$) | **187.3** | $7.62\times 10^{-15}$ | $2.5\times 10^{10}$ | **0.42** | **45.2** |
| | $K = 12$ | 175.5 | $3.12\times 10^{-15}$ | $5.6\times 10^{10}$ | 0.48 | 54.7 |
| | $K = 7$ | 169.2 | $1.45\times 10^{-15}$ | $1.2\times 10^{11}$ | 0.53 | 58.6 |
| | $K = 5$ | 165.3 | $8.20\times 10^{-16}$ | $2.0\times 10^{11}$ | 0.57 | 62.1 |
| | $K = 3$ | 161.2 | $4.10\times 10^{-16}$ | $3.9\times 10^{11}$ | 0.62 | 68.4 |
| | $K = 1$ (Air-like) | 160.3 | $1.20\times 10^{-16}$ | $1.3\times 10^{12}$ | 0.69 | 74.8 |
| **Cavity Thickness** | $t_{cav} = 30\text{ nm}$ | **154.0** | $2.10\times 10^{-18}$ | **$7.3\times 10^{13}$** | **0.51** | **52.3** |
| | $t_{cav} = 35\text{ nm}$ | 140.0 | $6.50\times 10^{-18}$ | $2.2\times 10^{13}$ | 0.54 | 56.1 |
| | $t_{cav} = 40\text{ nm}$ | 125.0 | $1.80\times 10^{-17}$ | $6.9\times 10^{12}$ | 0.58 | 61.4 |
| **Negative $Q_F$** (DNA/Acidic) | $Q_F = -10^{10}\text{ cm}^{-2}$ | 108.0 | $1.80\times 10^{-17}$ | $6.0\times 10^{12}$ | 0.52 | 53.4 |
| | $Q_F = -5\times 10^{11}\text{ cm}^{-2}$ | 101.0 | $8.50\times 10^{-18}$ | $1.2\times 10^{13}$ | 0.56 | 56.8 |
| | $Q_F = -10^{12}\text{ cm}^{-2}$ | 94.6 | $3.20\times 10^{-18}$ | $3.0\times 10^{13}$ | 0.61 | 62.0 |
| **Positive $Q_F$** (Basic Protein) | $Q_F = +10^{10}\text{ cm}^{-2}$ | 130.0 | $8.38\times 10^{-15}$ | $1.6\times 10^{10}$ | 0.49 | 54.1 |
| | $Q_F = +5\times 10^{11}\text{ cm}^{-2}$ | 134.0 | $4.64\times 10^{-14}$ | $2.9\times 10^{9}$ | 0.46 | 55.3 |
| | $Q_F = +10^{12}\text{ cm}^{-2}$ | 137.0 | $2.50\times 10^{-13}$ | $5.5\times 10^{8}$ | 0.43 | 57.0 |

---

## 3. Physical Analysis & Discussion

### A. Ferroelectric Dielectric Constant ($K$) Trends
- **Subthreshold Swing Reduction**: Transitioning from low permittivity ($K=1, SS=74.8\text{ mV/dec}$) to ferroelectric high-$\kappa$ ($K=22, SS=45.2\text{ mV/dec}$) successfully breaks the classical Boltzmann limit ($60\text{ mV/dec}$ at $300\text{ K}$).
- **Threshold Voltage Shift**: The enhanced gate capacitance shifts the onset of band-to-band tunneling from $V_{GS} = 0.69\text{ V}$ down to $V_{GS} = 0.42\text{ V}$ ($\Delta V_{TH} = -270\text{ mV}$), enabling low-voltage supply operation ($V_{DD} \le 1.0\text{ V}$).
- **Drive Current Amplification**: $I_{ON}$ increases by $+16.8\%$ due to heightened peak electric field at the tunnel junction.

### B. Cavity Thickness Trends
- **Capacitive Coupling**: As cavity thickness increases from $30\text{ nm}$ to $40\text{ nm}$, gate-to-channel control degrades due to increased equivalent oxide thickness ($EOT$), causing a modest drop in drive current ($154\ \mu\text{A}/\mu\text{m} \rightarrow 125\ \mu\text{A}/\mu\text{m}$).
- **Leakage Floor**: $I_{OFF}$ remains ultra-low ($< 2\times 10^{-17}\text{ A}/\mu\text{m}$), yielding switching ratios exceeding $10^{12}$ across all three cavity thicknesses.

### C. Biomolecule Transduction & Sensitivity
- **Sensitivity Metric ($\Delta V_{TH} / \Delta Q_F$)**:
  - Across the investigated negative fixed charge range ($-10^{10}$ to $-10^{12}\text{ cm}^{-2}$), the threshold voltage shifts by **$+90\text{ mV}$** ($0.52\text{ V} \rightarrow 0.61\text{ V}$).
  - For positive charge ($+10^{10}$ to $+10^{12}\text{ cm}^{-2}$), $V_{TH}$ shifts by **$-60\text{ mV}$** ($0.49\text{ V} \rightarrow 0.43\text{ V}$).
  - The total dynamic detection span across polarities is **$180\text{ mV}$** ($0.43\text{ V}$ to $0.61\text{ V}$).
- **Current Modulation Metric ($\Delta I_{DS} / I_0$)**:
  - At $V_{GS} = 0.5\text{ V}$ (subthreshold sensing bias), the drain current modulates by over **two orders of magnitude** between neutral and charged biomolecule states, proving high electrostatic sensitivity.
