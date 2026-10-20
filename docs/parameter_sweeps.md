# Parameter Sweeps and Simulation Findings
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)  
**Authors:** Allen Joe A (24BVD1100), Guided by: Lakshmi B  
**Reference:** IEEE Sensors Journal, Vol. 24, No. 22, pp. 37923-37930 (Nov 2024)

---

## 1. Overview

The TCAD investigation examined three parameter sweeps to evaluate device performance and label-free biosensing capability:
1. **Cavity Length Variation ($L_{cav}$)**: Investigated the effect of nanocavity length ($L_{cav} = 30\text{ nm}, 35\text{ nm}, 40\text{ nm}$) on on-state drive current, off-state leakage, and switching ratio at constant cavity thickness ($T_{cav} = 3\text{ nm}$).
2. **Nanocavity Dielectric Constant ($K$)**: Evaluated dielectric modulation across a library of target biological analytes ($K = 1, 3, 5, 7, 12, 22$) to establish label-free sensitivity against the air reference ($K = 1$).
3. **Interface Fixed Charge ($Q_F$)**: Quantified electrostatic modulation across positive and negative biomolecule charges ($Q_F = \pm 10^{10}, \pm 5\times 10^{11}, \pm 10^{12}\text{ cm}^{-2}$).

---

## 2. Quantitative Performance Parameters

### Table I: Cavity Length Variation

All quantities are extracted directly from the consolidated Sentaurus simulation records ($V_{DS} = 1.0\text{ V}$):

| Cavity Length ($L_{cav}$) | $V_{th}$ (V) | $I_{ON}$ (mA) | $I_{OFF}$ (A) | $I_{ON}/I_{OFF}$ Ratio | $g_m$ (mS) | $SS$ (mV/dec) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **30 nm** | **0.4010** | **0.8040** | $1.11 \times 10^{-12}$ | **$7.2432 \times 10^8$** | 0.6110 | 61.0 |
| **35 nm** | 0.3969 | 0.1970 | $1.12 \times 10^{-12}$ | $1.7589 \times 10^8$ | 0.6099 | 59.0 |
| **40 nm** | 0.3969 | 0.1908 | $1.10 \times 10^{-12}$ | $1.7345 \times 10^8$ | 0.6135 | 59.8 |

> **Key Observation:** The 30 nm cavity achieves the highest on-state current ($0.8040\text{ mA}$) and maximum switching ratio ($7.24 \times 10^8$), outperforming the 35 nm and 40 nm designs by over $4\times$ in drive current.

---

### Table II: Biomolecule Dielectric Constant ($K$) Modulation

Target analyte dielectric constants simulated in the 30 nm nanocavity:

| Dielectric Constant ($K$) | Target Analyte | $V_{th}$ (V) | $I_{ON} / I_{DS}$ (mA) | $I_{ON}/I_{OFF}$ Ratio | $g_m$ (mS) | $SS$ (mV/dec) |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| **1 (Air)** | Baseline Reference | *Not reported* | **0.2040** | *Not reported* | *Not reported* | *Not reported* |
| **3** | Lipids | 0.4139 | 0.2050 | $1.5769 \times 10^8$ | *Not reported* | 60.10 |
| **5** | Carbohydrates | 0.4080 | 0.2120 | $1.7097 \times 10^8$ | 0.430 | 62.90 |
| **7** | Zein Protein | 0.4055 | 0.2160 | $1.9817 \times 10^8$ | 0.550 | 62.90 |
| **12** | Amino Acids | 0.4020 | 0.2257 | $2.0706 \times 10^8$ | 0.582 | 62.60 |
| **22** | MDA-MB-231 (Breast Cancer) | **0.3910** | **0.2410** | **$1.8538 \times 10^8$** | **0.650** | **62.07** |

---

### Table III: Calculated Current Sensitivity

Sensitivity is calculated with respect to the air reference ($I_{DS}(air) = 0.2040\text{ mA}$ at $K = 1$):
$$\text{Sensitivity}(I_{DS}) = \frac{|I_{DS}(bio) - I_{DS}(air)|}{I_{DS}(air)}$$

| Dielectric Constant ($K$) | Target Analyte | $I_{DS}$ (mA) | Sensitivity (Fraction) | Sensitivity (%) |
|:---:|:---|:---:|:---:|:---:|
| **1** | Air (Reference) | 0.2040 | 0.0000 | **0.000 %** |
| **3** | Lipids | 0.2050 | $4.9020 \times 10^{-3}$ | **0.490 %** |
| **5** | Carbohydrates | 0.2120 | $3.9216 \times 10^{-2}$ | **3.922 %** |
| **7** | Zein Protein | 0.2160 | $5.8824 \times 10^{-2}$ | **5.882 %** |
| **12** | Amino Acids | 0.2257 | $1.0637 \times 10^{-1}$ | **10.637 %** |
| **22** | MDA-MB-231 (Cancer Cell) | 0.2410 | $1.8137 \times 10^{-1}$ | **18.137 %** |

![Benchmark Summary](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/figures/comparative/metrics_benchmark_summary.png)

---

### Table IV: Fixed-Charge ($Q_F$) Polarity Sweep

Evaluating the impact of positive and negative biomolecule surface charges immobilized in the nanocavity at $K = 22$:

| Charge Polarity | Recorded Charge ($Q_F$, $\text{cm}^{-2}$) | Drain Current $I_{DS}$ (mA) |
|:---|:---:|:---:|
| **Positive $Q_F$** (Basic proteins / Poly-L-lysine) | $+1.0 \times 10^{10}$ | 0.2416 |
| | $+5.0 \times 10^{11}$ | 0.2256 |
| | $+1.0 \times 10^{12}$ | 0.2178 |
| **Negative $Q_F$** (DNA / RNA / Acidic proteins) | $-1.0 \times 10^{10}$ | 0.2110 |
| | $-5.0 \times 10^{11}$ | 0.2059 |
| | $-1.0 \times 10^{12}$ | 0.2040 |

---

## 3. Physical Insights

1. **Dielectric Modulation Mechanism**:
   - As biomolecules with higher dielectric permittivity ($K=1 \rightarrow 22$) fill the nanocavity, the effective gate oxide capacitance increases.
   - This tightens electrostatic control over the tunneling junction, lowering the tunneling barrier width and shifting the threshold voltage from $0.4139\text{ V}$ down to $0.3910\text{ V}$.
   - The on-state drive current increases monotonically, producing a peak sensitivity of **$18.137\%$** for MDA-MB-231 breast cancer cells.

2. **Ferroelectric Negative Capacitance Synergy**:
   - The $\text{Si:HfO}_2$ layer provides internal voltage amplification ($\partial \psi_s / \partial V_{GS} > 1$), maintaining steep subthreshold swing ($\approx 60\text{--}62\text{ mV/dec}$) and high transconductance ($g_m$ up to $0.650\text{ mS}$).

3. **Cavity Length Optimization**:
   - The 30 nm cavity places the gate electrode and ferroelectric stack in optimal proximity to the source-channel tunneling interface ($X = 10\text{ nm}$), maximizing band-to-band tunneling generation while maintaining low off-state leakage ($I_{OFF} \approx 1.1 \times 10^{-12}\text{ A}$).
