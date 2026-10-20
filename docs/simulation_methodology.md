# Simulation Methodology and Numerical Formulation
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)

---

## 1. Sentaurus TCAD Toolchain Architecture

The device simulation framework uses the industry-standard Synopsys Sentaurus TCAD suite:

```
┌──────────────────────────────────────────────┐
│  Sentaurus Structure Editor (SDE)            │
│  - 2D Cross-section geometry definition      │
│  - T-channel & Inverted-T nanocavity layout │
│  - Electrode contacts & doping profiles      │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│  Sentaurus Mesh (SNMesh)                     │
│  - Delaunay triangulation                    │
│  - Sub-nanometer refinement at tunnel junction│
│  - Nanocavity interface boundary mesh        │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│  Sentaurus Device (SDevice)                  │
│  - Coupled Poisson & Drift-Diffusion solvers │
│  - Kane Non-Local Band-to-Band Tunneling     │
│  - Landau-Khalatnikov Ferroelectric models   │
│  - DC voltage ramp & parameter sweeps        │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│  Sentaurus Inspect / SVisual                 │
│  - Extraction of I-V transfer curves         │
│  - 1D profiles (Potential, E-field, Bands)   │
└──────────────────────────────────────────────┘
```

---

## 2. Mathematical Formulations & Governing Equations

### A. Electrostatic Poisson & Drift-Diffusion System
Carrier transport inside the silicon channel is governed by the self-consistent solution of Poisson's equation and electron/hole continuity equations:

$$\nabla \cdot (\epsilon \nabla \psi) = -q (p - n + N_D^+ - N_A^-) - \rho_{trap}$$

$$\nabla \cdot \mathbf{J}_n = q R_{net} - q G_{BTBT}$$
$$\nabla \cdot \mathbf{J}_p = -q R_{net} + q G_{BTBT}$$

where:
- $\mathbf{J}_n = -q \mu_n n \nabla \phi_n$ and $\mathbf{J}_p = -q \mu_p p \nabla \phi_p$ are electron and hole current densities.
- $G_{BTBT}$ is the band-to-band tunneling generation rate.
- $R_{net}$ is the net recombination rate (SRH + Auger).

### B. Band-to-Band Tunneling Generation Rate
The non-local Kane tunneling generation rate along carrier trajectories is computed as:
$$G_{BTBT} = A_{Kane} \cdot \frac{|E|^2}{E_g^{1/2}} \cdot \exp\left( - B_{Kane} \cdot \frac{E_g^{3/2}}{|E|} \right)$$
where $A_{Kane}$ and $B_{Kane}$ are calibrated parameters for silicon ($A_{Kane} \approx 4.0\times 10^{14}\text{ cm}^{-1/2}\text{V}^{-2}\text{s}^{-1}$, $B_{Kane} \approx 1.9\times 10^{7}\text{ V/cm}\cdot\text{eV}^{-3/2}$).

### C. Landau-Khalatnikov (L-K) Ferroelectric Equation
The polarization state $P$ of the ferroelectric layer ($\text{HfO}_2$) is governed by the dynamic Ginzburg-Landau equation:
$$\rho \frac{\partial P}{\partial t} + \nabla_P F = E_{fe}$$
$$F(P) = \alpha P^2 + \beta P^4 + \gamma P^6 - E_{fe} P$$
In the steady-state DC regime ($\partial P/\partial t \rightarrow 0$), the negative stiffness region ($\alpha < 0$) produces internal voltage amplification without hysteresis when stabilized in series with gate capacitance $C_{int}$:
$$V_{internal} = V_{GS} + \frac{Q_{gate}}{|C_{fe}|}$$

---

## 3. Mesh Strategy & Numerical Convergence Settings

1. **Spatial Discretization**:
   - Total device length: $150\text{ nm}$.
   - Bulk regions: Minimum grid step $\Delta x = 2.0\text{ nm}, \Delta y = 2.0\text{ nm}$.
   - Refinement Box at Tunneling Junction ($X \in [40, 60]\text{ nm}$):
     - $\Delta x_{min} = 0.2\text{ nm}$
     - $\Delta y_{min} = 0.2\text{ nm}$
     - Refinement ratio: $1.2$
   - Nanocavity Boundary: Conforming triangular mesh with sub-nanometer resolution ($\Delta x \le 0.5\text{ nm}$) to resolve sharp electric field gradients.

2. **Nonlinear Solver Settings**:
   - Primary solver: Coupled Newton-Raphson scheme with norm-damping.
   - Relative error tolerance: $10^{-5}$
   - Maximum iterations per bias step: 25
   - Adaptive step control: Gate bias increment drops from $0.05\text{ V}$ to $0.001\text{ V}$ upon steep current onset ($SS < 60\text{ mV/dec}$) to prevent divergence.
