# Device Architecture and Operating Physics
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)  
**Authors:** Allen Joe A (24BVD1100), Guided by: Lakshmi B  
**Reference:** IEEE Sensors Journal, Vol. 24, No. 22, pp. 37923-37930 (Nov 2024)

---

## 1. Verified Device Architecture (Grounded in SDE Deck)

The **FE-DGDM-JLTFET** biosensor structure is defined in [`sde_dvs.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/sde/structure/sde_dvs.tcl) with a total physical transport length of **158 nm** ($X \in [0.000, 0.158]\ \mu\text{m}$).

![FE-DGDM-JLTFET Architecture](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/figures/device/device_architecture_schematic.png)

### Geometric Breakdown and Coordinates (TCAD SDE Specification)

| Region Name | Material | X Start ($\mu\text{m}$) | X End ($\mu\text{m}$) | Length (nm) | Y Range ($\mu\text{m}$) | Thickness (nm) | Active Doping ($N_D$, $\text{cm}^{-3}$) |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Source (`source`)** | Silicon | $0.000$ | $0.010$ | 10 | $[-0.011, +0.011]$ | 22 | Arsenic $1.0 \times 10^{19}$ |
| **Top Source Wing (`sourcet`)** | Silicon | $0.010$ | $0.055$ | 45 | $[-0.011, -0.009]$ | 2 | Arsenic $1.0 \times 10^{19}$ |
| **Bottom Source Wing (`sourceb`)** | Silicon | $0.010$ | $0.055$ | 45 | $[+0.009, +0.011]$ | 2 | Arsenic $1.0 \times 10^{19}$ |
| **Channel Body (`channel`)** | Silicon | $0.010$ | $0.103$ | 93 | $[-0.005, +0.005]$ | 10 ($T_{ch}$) | Arsenic $1.0 \times 10^{15}$ |
| **Interfacial Oxide (`oxide1`)** | $\text{SiO}_2$ | $0.010$ | $0.103$ | 93 | $[-0.006, -0.005]$ | 1 | Undoped |
| **Interfacial Oxide (`oxide2`)** | $\text{SiO}_2$ | $0.010$ | $0.103$ | 93 | $[+0.005, +0.006]$ | 1 | Undoped |
| **Underlap Oxide (`sio2t`, `sio2b`)** | $\text{SiO}_2$ | $0.010$ | $0.045$ | 35 | $[\pm 0.006, \pm 0.009]$ | 3 | Undoped |
| **Nanocavity (`vac1`, `vac2`)** | Vacuum / Biomolecules | $0.045$ | $0.075$ | 30 ($L_{cav}$) | $[\pm 0.006, \pm 0.009]$ | 3 ($T_{cav}$) | Undoped ($K = 1\text{--}22$) |
| **Ferroelectric Stack (`hfo2t`, `hfo2b`)** | Doped $\text{Si:HfO}_2$ | $0.075$ | $0.103$ | 28 ($L_{FE}$) | $[\pm 0.006, \pm 0.009]$ | 3 ($T_{FE}$) | Undoped ($\epsilon_r = 31$) |
| **Drain Extension (`channelde`)** | Silicon | $0.103$ | $0.148$ | 45 | $[-0.008, +0.008]$ | 16 | Arsenic $1.0 \times 10^{15}$ |
| **Extension Oxide (`oxide3`, `oxide4`)** | $\text{SiO}_2$ | $0.103$ | $0.148$ | 45 | $[\pm 0.008, \pm 0.009]$ | 1 | Undoped |
| **Drain (`drain`)** | Silicon | $0.148$ | $0.158$ | 10 | $[-0.009, +0.009]$ | 18 | Arsenic $1.0 \times 10^{20}$ |

---

## 2. Key Architectural Innovations

### A. T-Shaped Channel & Extended Source Wings
- The source features a central block ($22\text{ nm}$ height) and top/bottom horizontal extensions (`sourcet` and `sourceb`) extending $45\text{ nm}$ along the transport direction.
- This creates an effective **T-shaped source-channel interface** that:
  1. Enlarges the active tunneling cross-section at the $X = 10\text{ nm}$ junction.
  2. Enhances gate electrostatic coupling and suppresses ambipolar leakage current.
  3. Provides an electrostatic shield preventing drain electric field lines from degrading the source tunneling barrier.
- At $X = 103\text{ nm}$, the channel body steps up from $10\text{ nm}$ to $16\text{ nm}$ (`channelde`), providing low series resistance into the drain while maintaining strict sub-10 nm body confinement under the gate.

### B. Inverted-T Nanocavity (Bio-Capture Region)
- The nanocavity is situated in the gate-source underlap region ($X \in [45, 75]\text{ nm}$), directly upstream of the ferroelectric gate stack.
- Etched as an inverted-T recess, it captures target biomolecules directly above and below the thin silicon channel separated only by an ultra-thin 1 nm $\text{SiO}_2$ passivation layer.
- This positioning ensures that dielectric constant variations ($\Delta K$) and immobilized charges ($Q_F$) produce maximum electrostatic perturbation at the channel surface where band bending modulates the tunneling barrier width.

### C. Doping-Modulated Junctionless (DM-JL) Operation
- All silicon regions are $n$-type doped, eliminating metallurgical $p\text{--}n$ junctions and abrupt doping gradients:
  - Source: Heavily doped $n^+$ ($10^{19}\text{ cm}^{-3}$).
  - Channel: Lightly doped $n$ ($10^{15}\text{ cm}^{-3}$).
  - Drain Extension: Lightly doped $n$ ($10^{15}\text{ cm}^{-3}$).
  - Drain: Ultra-heavily doped $n^{++}$ ($10^{20}\text{ cm}^{-3}$).
- Carrier injection relies on band-to-band tunneling induced by gate-to-source bias rather than thermionic emission over a forward-biased junction.

### D. Ferroelectric Negative Capacitance Gate Stack ($\text{Si:HfO}_2$)
- Sited at $X \in [75, 103]\text{ nm}$, the 3 nm $\text{Si:HfO}_2$ layer provides negative capacitance (NC) amplification:
  $$C_{ox}^{eff} = \frac{C_{ox} |C_{FE}|}{|C_{FE}| - C_{ox}}$$
- The stabilized negative capacitance magnifies the internal gate potential, yielding subthreshold swings ($SS$) well below the thermodynamic Boltzmann limit ($60\text{ mV/dec}$ at $300\text{ K}$) and boosting the on-state driving current ($I_{ON}$).

---

## 3. Physical Models & Solvers (SDevice Implementation)

The TCAD simulations employ rigorous quantum-corrected and non-local transport physics configured in [`sdevice_des.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/sdevice/device/sdevice_des.tcl) and [`sdevice.par`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/parameter/sdevice.par):

1. **Non-Local Hurkx Band-to-Band Tunneling (BTBT)**:
   - Evaluated dynamically across the source-channel interface:
     $$R_{net}^{BTBT} = - A \cdot D \cdot \left(\frac{E}{E_0}\right)^P \exp\left(-\frac{B}{E}\right)$$
   - Hurkx Parameters:
     - $A = 8.9770 \times 10^{20}\text{ cm}^{-1}\text{s}^{-1}\text{V}^{-2}$
     - $B = 2.1466 \times 10^{7}\text{ V/cm}$
     - Phonon energy $\hbar\Omega = 18.6\text{ meV}$
     - Non-local evaluation length $= 30\text{ nm}$, permeation $= 3\text{ nm}$.

2. **Landau-Devonshire Ferroelectric Polarization (`FEPolarization`)**:
   - Electric field-polarization constitutive relation:
     $$E_{FE} = 2 \alpha P + 4 \beta P^3 + 6 \gamma P^5$$
   - Calibrated parameters for 3 nm $\text{Si:HfO}_2$:
     - Negative stiffness: $\alpha = -3.7 \times 10^{10}\text{ cm/F}$
     - Non-linear coefficient: $\beta = 2.5 \times 10^{21}\text{ cm}^5/(\text{F}\cdot\text{C}^2)$
     - Remanent polarization: $P_r = 1.0\ \mu\text{C/cm}^2$
     - Saturation polarization: $P_s = 20.0\ \mu\text{C/cm}^2$
     - Coercive field: $E_c = 1.0\text{ MV/cm}$
     - Dielectric constant: $\epsilon_{FE} = 31.0$

3. **Carrier Transport & Mobility**:
   - **Hydrodynamic Transport**: Solves the carrier energy conservation equation alongside Poisson and continuity equations.
   - **Fermi-Dirac Statistics**: Captures degenerate carrier distributions in the heavily doped source ($10^{19}$) and drain ($10^{20}$).
   - **OldSlotboom Bandgap Narrowing (BGN)**: $E_{bgn} = 9.0\text{ meV}$, $N_{ref} = 10^{17}\text{ cm}^{-3}$.
   - **Philips Unified Mobility Model (`PhuMob`)**: Concentration and temperature-dependent lattice scattering.
   - **Lombardi Surface Roughness Model (`Enormal`)**: Models mobility degradation near the $\text{Si/SiO}_2$ interface.
   - **Velocity Saturation**: $v_{sat} = 1.01 \times 10^{7}\text{ cm/s}$.
   - **Recombination**: Scharfetter doping-dependent SRH and Auger recombination.
