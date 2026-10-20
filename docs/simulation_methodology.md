# Simulation Methodology and Numerical Formulation
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)  
**Authors:** Allen Joe A (24BVD1100), Guided by: Lakshmi B  
**Reference:** IEEE Sensors Journal, Vol. 24, No. 22, pp. 37923-37930 (Nov 2024)

---

## 1. Sentaurus TCAD Toolchain Architecture

The device simulation framework uses the Synopsys Sentaurus TCAD suite:

```
┌────────────────────────────────────────────────────────┐
│  Sentaurus Structure Editor (SDE)                      │
│  - Script: sde/structure/sde_dvs.tcl                   │
│  - 2D Cross-section geometry (158 nm total length)     │
│  - T-channel body & Inverted-T nanocavity layout       │
│  - Electrode contacts (s, d, g) & doping definitions   │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│  Sentaurus Mesh (SNMesh: snmesh -a)                    │
│  - Global window: RefEvalWin.all (2.0 nm x 0.2 nm)     │
│  - Multibox refinement: RefEvalWin.active               │
│    (1.0 nm x 0.1 nm sub-nanometer grid at BTBT zone)   │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│  Sentaurus Device (SDevice)                            │
│  - Command Deck: sdevice/device/sdevice_des.tcl        │
│  - Parameter File: parameter/sdevice.par               │
│  - Physics Models: sdevice/physics/physics_models.tcl  │
│  - Coupled Poisson & Hydrodynamic transport equations  │
│  - Dynamic Non-Local Hurkx Band-to-Band Tunneling      │
│  - Landau-Devonshire Ferroelectric Polarization        │
│  - Quasistationary Vds ramp & Vgs fine sweep           │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│  Sentaurus Inspect & SVisual / Python Analysis         │
│  - SWB Automation: simulations/fe_dgdm_jltfet_...tcl   │
│  - Data extraction: analysis/scripts/extract_metrics.py│
│  - Figures: analysis/scripts/plot_publication_figures  │
└────────────────────────────────────────────────────────┘
```

---

## 2. Governing Equations and Physical Formulations

### A. Electrostatic Poisson & Hydrodynamic Transport
Carrier transport in the channel body is governed by the self-consistent solution of Poisson's equation and the Hydrodynamic conservation equations (accounting for non-local carrier heating and high-field saturation):

$$\nabla \cdot (\epsilon \nabla \psi) = -q (p - n + N_D^+ - N_A^-) - \nabla \cdot \mathbf{P}_{FE}$$

$$\nabla \cdot \mathbf{J}_n = q R_{net} - q G_{BTBT}$$
$$\nabla \cdot \mathbf{J}_p = -q R_{net} + q G_{BTBT}$$

$$\nabla \cdot \mathbf{S}_n = \mathbf{J}_n \cdot \mathbf{E} - n \left( \frac{\frac{3}{2} k_B (T_n - T_L)}{\tau_{w,ele}} \right)$$

where:
- $\mathbf{P}_{FE}$ is the ferroelectric polarization vector in the $\text{Si:HfO}_2$ regions.
- $\tau_{w,ele} = 0.3\text{ ps}$ is the electron energy relaxation time.
- $G_{BTBT}$ is the band-to-band tunneling generation rate.

### B. Dynamic Non-Local Hurkx Band-to-Band Tunneling (BTBT)
Tunneling across the source-channel interface ($X = 10\text{ nm}$) is evaluated dynamically along the curved electric field lines using the Hurkx model (`sdevice_des.tcl`):

$$G_{BTBT} = A \cdot D \cdot \left(\frac{E}{E_0}\right)^P \exp\left(-\frac{B}{E}\right)$$

where:
- Prefactor $A = 8.9770 \times 10^{20}\text{ cm}^{-1}\text{s}^{-1}\text{V}^{-2}$
- Exponential field $B = 2.1466 \times 10^{7}\text{ V/cm}$
- Phonon energy $\hbar\Omega = 18.6\text{ meV}$
- Evaluated with non-local path length $= 30\text{ nm}$ and permeation depth $= 3\text{ nm}$.

### C. Landau-Devonshire Ferroelectric Negative Capacitance
The ferroelectric gate stack (`hfo2t`, `hfo2b`) is simulated via native Landau-Devonshire theory:

$$E_{FE} = 2 \alpha P + 4 \beta P^3 + 6 \gamma P^5$$

Parameters configured in `parameter/sdevice.par`:
- $\alpha = -3.7 \times 10^{10}\text{ cm/F}$
- $\beta = 2.5 \times 10^{21}\text{ cm}^5/(\text{F}\cdot\text{C}^2)$
- $\gamma = 0.0$
- Permittivity $\epsilon_{FE} = 31.0$

### D. Bandgap Narrowing (OldSlotboom)
In the heavily doped source ($N_D = 10^{19}\text{ cm}^{-3}$) and drain ($N_D = 10^{20}\text{ cm}^{-3}$):

$$\Delta E_g = E_{bgn} \left( \ln\left(\frac{N}{N_{ref}}\right) + \sqrt{\left(\ln\left(\frac{N}{N_{ref}}\right)\right)^2 + 0.5} \right)$$
with $E_{bgn} = 9.0\text{ meV}$ and $N_{ref} = 1.0 \times 10^{17}\text{ cm}^{-3}$.

---

## 3. Numerical Convergence and Solver Strategy

The solver configuration in [`sdevice_des.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/sdevice/device/sdevice_des.tcl) utilizes:
1. **Newton Convergence Settings**:
   - `Digits = 8`
   - `RelErrControl`
   - `ErRef(Electron) = 1e8`
   - `Iterations = 25` (Coupled Poisson-Electron)
   - `TensorGridAniso` anisotropic grid interpolation
2. **Two-Stage Quasistationary Solution**:
   - Stage 1: Ramp drain electrode to $V_{DS} = 1.0\text{ V}$ with adaptive step size ($10^{-6}\text{ to }0.2\text{ V}$).
   - Stage 2: Ramp gate electrode $V_{GS}$ from $0.0\text{ V}$ to $1.5\text{ V}$ (`DoZero`, increment 1.2, min step $10^{-6}\text{ V}$).
