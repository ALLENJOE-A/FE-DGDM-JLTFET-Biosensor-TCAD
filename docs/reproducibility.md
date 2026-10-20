# Reproducibility Guide
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)

---

## 1. Prerequisites and Licensing

### TCAD Environment
- **Synopsys Sentaurus TCAD** (Version 2018.06 or newer).
- Modules required:
  - `sde` (Sentaurus Structure Editor)
  - `snmesh` (Sentaurus Mesh)
  - `sdevice` (Sentaurus Device with Advanced Physics license for Band-to-Band Tunneling and Ferroelectric models)
  - `inspect` or `svisual` (Visualization and curve extraction)
- *Note:* Synopsys Sentaurus TCAD is commercial proprietary software subject to university/enterprise licensing.

### Open-Source Data Analysis Environment
- **Python**: Version 3.8 or newer.
- **Packages**:
  - `numpy`
  - `matplotlib`
  - `pillow` (PIL)
  - Standard library `csv`

---

## 2. Reproduction of Data Extraction & Publication Figures

A researcher who does not hold a Synopsys license can fully reproduce all quantitative data extraction, tables, and publication-ready figures using the open-source pipeline provided in this repository.

### Step 1: Clone Repository
```bash
git clone https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD.git
cd FE-DGDM-JLTFET-Biosensor-TCAD
```

### Step 2: Run Metrics Extraction
```bash
python analysis/scripts/extract_metrics.py
```
*Outputs generated:*
- `Results/raw_data/k_sweep_transfer.csv`
- `Results/raw_data/cavity_sweep_transfer.csv`
- `Results/raw_data/qf_negative_transfer.csv`
- `Results/raw_data/qf_positive_transfer.csv`
- `Results/raw_data/extracted_metrics_summary.csv`

### Step 3: Generate Publication-Grade Figures
```bash
python analysis/scripts/plot_publication_figures.py
```
*Outputs generated:*
- `figures/device/device_architecture_schematic.png` (.svg)
- `figures/electrical/k_sweep_transfer_characteristics.png` (.svg)
- `figures/sensing/cavity_thickness_transfer_characteristics.png` (.svg)
- `figures/sensing/fixed_charge_sensitivity_comparison.png` (.svg)
- `figures/comparative/metrics_benchmark_summary.png` (.svg)

---

## 3. Sentaurus TCAD Command Execution Template

When rerun in an authorized Sentaurus environment, the execution sequence proceeds as follows:

```bash
# 1. Structure definition & meshing
sde -e -l sde_device.cmd
snmesh sde_device

# 2. Electrical device simulation
sdevice sdevice_des.cmd

# 3. Post-processing & extraction
inspect -f sdevice_des.plt
```
