# Device Architecture and Operating Physics
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)

---

## 1. Device Concept and Architectural Overview

The **FE-DGDM-JLTFET** (Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel Field-Effect Transistor) is an advanced steep-slope semiconductor biosensor engineered to overcome the thermodynamic thermal limit ($SS \ge 60\text{ mV/dec}$ at $300\text{ K}$) of conventional MOSFET biosensors while eliminating metallurgical p-n junction doping gradients.

```
       Top Gate Contact (Metal)
  ┌─────────────────────────────────┐
  │   Ferroelectric Layer (HfO2)   │
  ├──────────────┬──────────────────┤
  │ Gate Oxide   │   Nanocavity     │ (Inverted-T Biomolecule Region)
  ├──────────────┴───┬──────────────┤
  │                  │              │
  │   Source         │   Channel    │   Drain
  │  (n+ uniform)    │  (T-shaped)  │  (n+ uniform)
  │                  │              │
  ├──────────────────┴──────────────┤
  │       Bottom Gate Oxide         │
  ├─────────────────────────────────┤
  │ Bottom Ferroelectric Layer      │
  ├─────────────────────────────────┤
  │   Bottom Gate Contact (Metal)   │
  └─────────────────────────────────┘
  ◄───────────── 150 nm ────────────►
```

### Core Structural Features
1. **Junctionless Transport**: The channel, source, and drain regions share a uniform $n$-type doping concentration. The device eliminates physically abrupt metallurgical junctions, mitigating severe thermal diffusion and random dopant fluctuation (RDF) issues common in sub-20 nm scale devices.
2. **Double-Gate Doping Modulation (DGDM)**: The effective carrier density along the channel is modulated electrostatically by unequal or workfunction-engineered dual gates, creating an effective $p^+ - i - n^+$ electrostatic potential profile required for band-to-band tunneling (BTBT).
3. **T-Shaped Channel Geometry**: The channel cross-section incorporates a vertical extension (T-shape) that enhances gate electrostatic controllability, increases the tunneling surface area, and shields the channel interior from drain-induced barrier lowering (DIBL).
4. **Inverted-T Nanocavity**: A carved dielectric recess etched adjacent to the channel/tunnel junction serves as the receptor cavity for immobilizing target biomolecules (e.g., proteins, DNA, viral antigens). Its inverted-T profile provides high surface-to-volume capture area near the most sensitive electrostatic bottleneck: the tunneling junction.
5. **Ferroelectric Gate Stack**: Incorporating a ferroelectric thin film (such as doped $\text{HfO}_2$, e.g., $\text{Hf}_{0.5}\text{Zr}_{0.5}\text{O}_2$) within the gate dielectric stack provides negative capacitance (NC) amplification ($|C_{fe}|$), magnifying the channel surface potential beyond the applied physical gate voltage:
   $$\frac{\partial \psi_s}{\partial V_{GS}} = \frac{|C_{fe}|}{|C_{fe}| - C_{int}} > 1$$

---

## 2. Operating Physics and Transport Mechanism

### Band-to-Band Tunneling (BTBT)
Unlike conventional MOSFETs where carriers surmount a thermionic energy barrier ($E > q\phi_B$), transport in a Tunnel FET is governed by quantum mechanical band-to-band tunneling from the valence band of the source region into the conduction band of the channel region.

The transmission probability $T_{WKB}$ through the triangular electrostatic barrier is modeled using the Wentzel-Kramers-Brillouin (WKB) approximation:
$$T_{WKB} \approx \exp\left( - \frac{4 \sqrt{2 m^*} E_g^{3/2}}{3 q \hbar |E|} \right)$$
where:
- $m^*$ is the carrier effective tunneling mass.
- $E_g$ is the semiconductor bandgap.
- $|E|$ is the localized electric field at the tunnel junction.
- $\hbar$ is the reduced Planck constant.

The drain current is directly proportional to the transmission coefficient integrated across the tunneling energy window:
$$I_{DS} \propto \int_{E_C^{channel}}^{E_V^{source}} T_{WKB}(E) [f_S(E) - f_D(E)] dE$$

### Subthreshold Swing Amplification
The total subthreshold swing ($SS$) is the product of body factor $m$ and transport factor $n$:
$$SS = \frac{\partial V_{GS}}{\partial \log_{10}(I_{DS})} = \underbrace{\frac{\partial V_{GS}}{\partial \psi_s}}_{m} \times \underbrace{\frac{\partial \psi_s}{\partial \log_{10}(I_{DS})}}_{n}$$
- In classical MOSFETs, $m \ge 1$ and $n \ge 60\text{ mV/dec}$ at room temperature, yielding $SS \ge 60\text{ mV/dec}$.
- In the FE-DGDM-JLTFET, the negative capacitance effect delivers $m < 1$ (internal voltage amplification), while BTBT filtering delivers $n < 60\text{ mV/dec}$ at low currents, enabling steep switching and high current sensitivity.

---

## 3. Biosensing Transduction Mechanism

Target biomolecules (enzymes, antibodies, nucleic acids) carry intrinsic net electrostatic charges and possess distinct dielectric constants ($\kappa_{bio} \approx 2\text{--}10$).

```
Biomolecule binding in nanocavity
        ↓
Interface fixed charge (QF) & permittivity modulation
        ↓
Modulation of local electrostatic potential (Δψs)
        ↓
Change in tunneling barrier width (λ) & electric field (E)
        ↓
Exponential shift in tunneling transmission (TWKB)
        ↓
Macroscopic threshold voltage shift (ΔVTH) & current modulation (ΔIDS)
```

1. **Negative Charge Transduction ($Q_F < 0$)**:
   - Capturing negatively charged biomolecules (such as DNA/RNA chains or acidic proteins) introduces a negative sheet charge in the nanocavity.
   - This increases the electrostatic barrier height and modulates the gate-to-channel potential, shifting the effective threshold voltage ($V_{TH}$).
2. **Positive Charge Transduction ($Q_F > 0$)**:
   - Basic proteins or amine-functionalized ligands induce positive fixed charge ($Q_F > 0$).
   - This lowers the local conduction band edge, alters the tunneling alignment, and increases off-state leakage ($I_{OFF}$).
3. **Cavity Dimension Coupling**:
   - The spatial thickness/length of the nanocavity ($30\text{ nm}, 35\text{ nm}, 40\text{ nm}$) dictates the physical volume of captured biomolecules and the distance over which the gate electrode electrostatically couples to the channel.

---

## 4. TCAD Physical Models & Numerics

Based on standard Synopsys Sentaurus Device formulation for junctionless tunnel FETs:
- **Band-to-Band Tunneling**: Non-local path-based dynamic tunneling models (Kane or Hurkx non-local BTBT) to evaluate electron generation rates along curved electric field lines at the source-channel interface.
- **Quantum Mechanics**: Density Gradient quantum corrections to account for carrier confinement in the ultra-thin T-shaped channel.
- **Ferroelectrics**: Landau-Khalatnikov (L-K) polarization equation coupled self-consistently with the Poisson equation:
  $$E_{fe} = 2 \alpha P + 4 \beta P^3 + 6 \gamma P^5 + \rho \frac{\partial P}{\partial t}$$
- **Mobility & Recombination**:
  - High-field velocity saturation (Canali model).
  - Doping-dependent mobility (Masetti model).
  - Shockley-Read-Hall (SRH) recombination with trap-assisted tunneling (TAT) and Auger recombination.
- **Boundary Conditions & Bias Ranges**:
  - Drain Contact: $V_{DS} = \text{constant}$.
  - Gate Contacts: $V_{GS}$ swept from $0.0\text{ V}$ to $1.5\text{ V}$.
  - Source Contact: Grounded ($V_S = 0.0\text{ V}$).
