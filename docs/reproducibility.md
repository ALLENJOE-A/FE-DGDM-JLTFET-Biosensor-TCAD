# Reproducibility Guide
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)  
**Authors:** Allen Joe A (24BVD1100), Guided by: Lakshmi B  
**Reference:** IEEE Sensors Journal, Vol. 24, No. 22, pp. 37923-37930 (Nov 2024)

---

## 1. Prerequisites and Licensing

### TCAD Environment (For Full Device Simulation)
- **Synopsys Sentaurus TCAD** (Version 2018.06 or newer).
- Modules required:
  - `sde` (Sentaurus Structure Editor)
  - `snmesh` (Sentaurus Mesh)
  - `sdevice` (Sentaurus Device with non-local band-to-band tunneling and ferroelectric polarization models)
  - `inspect` or `svisual` (Output curve extraction)
- Input decks included in this repository:
  - [`sde/structure/sde_dvs.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/sde/structure/sde_dvs.tcl)
  - [`sdevice/device/sdevice_des.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/sdevice/device/sdevice_des.tcl)
  - [`parameter/sdevice.par`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/parameter/sdevice.par)
  - [`sdevice/physics/physics_models.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/sdevice/physics/physics_models.tcl)
  - [`simulations/fe_dgdm_jltfet_simulation.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/simulations/fe_dgdm_jltfet_simulation.tcl)

### Open-Source Data Analysis Environment (Without TCAD License)
- **Python**: Version 3.8 or newer.
- **Packages**:
  - `numpy`
  - `matplotlib`
  - `pillow` (PIL)

---

## 2. Reproducing TCAD Simulations (Sentaurus Environment)

### Step 1: Generate Device Geometry and Mesh
```bash
# Execute Structure Editor script in Sentaurus SDE
sde -e -l sde/structure/sde_dvs.tcl

# Build mesh
snmesh -a n@node@
```

### Step 2: Run Device Simulations
```bash
# Run SDevice with parameter card
sdevice sdevice/device/sdevice_des.tcl
```

### Step 3: Automated Parameter Sweeps
```bash
# Run Sentaurus Workbench Tcl automation
swb -batch simulations/fe_dgdm_jltfet_simulation.tcl
```

---

## 3. Reproducing Data Extraction & Publication Figures

Researchers without a Sentaurus license can regenerate all figures and extracted tables directly from the verified simulation data:

### Step 1: Clone Repository
```bash
git clone https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD.git
cd FE-DGDM-JLTFET-Biosensor-TCAD
```

### Step 2: Regenerate All Publication Figures
```bash
python analysis/scripts/plot_publication_figures.py
```
*Outputs generated:*
- `figures/device/device_architecture_schematic.png` (and `.svg`)
- `figures/electrical/k_sweep_transfer_characteristics.png` (and `.svg`)
- `figures/sensing/cavity_thickness_transfer_characteristics.png` (and `.svg`)
- `figures/sensing/fixed_charge_sensitivity_comparison.png` (and `.svg`)
- `figures/comparative/metrics_benchmark_summary.png` (and `.svg`)
