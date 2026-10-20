# Analysis and Numerical Extraction Framework
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)

---

## 1. Overview

This directory provides automated, reproducible Python extraction scripts that digitize Sentaurus Inspect simulation curves and compute standard semiconductor device figures of merit ($I_{ON}, I_{OFF}, I_{ON}/I_{OFF}, V_{TH}, SS$).

## 2. Directory Structure

```text
analysis/
├── README.md                          # Methodology and metric extraction guide
└── scripts/
    ├── extract_metrics.py             # Curve digitization and parameter extraction script
    └── plot_publication_figures.py    # Publication-quality figure generation script
```

## 3. Extraction Methodology

The script `analysis/scripts/extract_metrics.py` applies calibrated pixel-to-coordinate mapping across the Sentaurus Inspect plot window ($X \in [20, 1340]\text{ px}$, $Y \in [50, 676]\text{ px}$) to extract $V_{GS}$ vs $I_{DS}$ points:

1. **$I_{ON}$**: Drain current evaluated at maximum gate overdrive ($V_{GS} = 1.5\text{ V}$).
2. **$I_{OFF}$**: Leakage current evaluated at zero gate bias ($V_{GS} = 0.0\text{ V}$).
3. **$I_{ON}/I_{OFF}$**: Current switching ratio.
4. **Threshold Voltage ($V_{TH}$)**: Extracted via the constant-current method at $I_{DS} = 10^{-7}\text{ A}/\mu\text{m}$.
5. **Subthreshold Swing ($SS$)**: Average slope across the subthreshold regime:
   $$SS_{avg} = \frac{\Delta V_{GS}}{\Delta \log_{10}(I_{DS})} \quad [\text{mV/dec}]$$

## 4. Generated Raw Data Tables

All extracted datasets are saved in `Results/raw_data/`:
- `k_sweep_transfer.csv`: $V_{GS}$ vs $I_{DS}$ for $K \in \{1, 3, 5, 7, 12, 22\}$.
- `cavity_sweep_transfer.csv`: $V_{GS}$ vs $I_{DS}$ for $t_{cav} \in \{30, 35, 40\}\text{ nm}$.
- `qf_negative_transfer.csv`: $V_{GS}$ vs $I_{DS}$ for $Q_F \in \{-10^{10}, -5\times 10^{11}, -10^{12}\}\text{ cm}^{-2}$.
- `qf_positive_transfer.csv`: $V_{GS}$ vs $I_{DS}$ for $Q_F \in \{+10^{10}, +5\times 10^{11}, +10^{12}\}\text{ cm}^{-2}$.
- `extracted_metrics_summary.csv`: Master comparison table of all figures of merit.

## 5. Execution

To re-run the extraction:
```bash
python analysis/scripts/extract_metrics.py
```
Dependencies: Python 3.8+, `numpy`, `pillow` (PIL).
