# Sentaurus Structure Editor (SDE) Input Decks

This directory contains the verified Sentaurus Structure Editor (SDE) script for the Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) biosensor.

## Files

- [`sde_dvs.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/sde/structure/sde_dvs.tcl): The complete Sentaurus Structure Editor deck generating the 2D cross-section, doping definitions, contact placements, refinement windows, and meshing commands (`snmesh -a`).

## Device Architecture Implementation

The SDE script defines the exact 158 nm device structure:

1. **Silicon Regions & Doping Modulation**:
   - **Source**: $X \in [0.000, 0.010]\ \mu\text{m}$, $Y \in [-0.011, +0.011]\ \mu\text{m}$ ($N_D = 10^{19}\text{ cm}^{-3}$, Arsenic).
   - **Source Wings (`sourcet` / `sourceb`)**: $X \in [0.010, 0.055]\ \mu\text{m}$, $Y \in [\pm 0.009, \pm 0.011]\ \mu\text{m}$ ($N_D = 10^{19}\text{ cm}^{-3}$).
   - **Channel Body**: $X \in [0.010, 0.103]\ \mu\text{m}$, $Y \in [-0.005, +0.005]\ \mu\text{m}$ ($T_{ch} = 10\text{ nm}$, $N_D = 10^{15}\text{ cm}^{-3}$).
   - **Drain Extension (`channelde`)**: $X \in [0.103, 0.148]\ \mu\text{m}$, $Y \in [-0.008, +0.008]\ \mu\text{m}$ ($T_{ext} = 16\text{ nm}$, $N_D = 10^{15}\text{ cm}^{-3}$).
   - **Drain**: $X \in [0.148, 0.158]\ \mu\text{m}$, $Y \in [-0.009, +0.009]\ \mu\text{m}$ ($T_D = 18\text{ nm}$, $N_D = 10^{20}\text{ cm}^{-3}$).

2. **Dielectrics and Nanocavity (Sensing Region)**:
   - **Interfacial Oxide (`oxide1`, `oxide2`)**: 1 nm $\text{SiO}_2$ separating channel from gate stack and cavity ($Y \in [\pm 0.005, \pm 0.006]\ \mu\text{m}$).
   - **Gate Underlap Oxide (`sio2t`, `sio2b`)**: 3 nm $\text{SiO}_2$, $X \in [0.010, 0.045]\ \mu\text{m}$, $Y \in [\pm 0.006, \pm 0.009]\ \mu\text{m}$.
   - **Inverted-T Nanocavity (`vac1`, `vac2`)**: 3 nm thickness, $L_{cav} = 30\text{ nm}$ ($X \in [0.045, 0.075]\ \mu\text{m}$, $Y \in [\pm 0.006, \pm 0.009]\ \mu\text{m}$). Split at $X = 0.060\ \mu\text{m}$ for precise contact alignment.
   - **Ferroelectric Layer (`hfo2t`, `hfo2b`)**: 3 nm thickness, $L_{FE} = 28\text{ nm}$ ($X \in [0.075, 0.103]\ \mu\text{m}$, $Y \in [\pm 0.006, \pm 0.009]\ \mu\text{m}$) of doped $\text{Si:HfO}_2$.

3. **Contacts**:
   - `s` (Source): Left edge $X = 0.000\ \mu\text{m}$, $Y \in [-0.011, +0.011]\ \mu\text{m}$.
   - `d` (Drain): Right edge $X = 0.158\ \mu\text{m}$, $Y \in [-0.009, +0.009]\ \mu\text{m}$.
   - `g` (Double-Gate): Top and bottom edges at $Y = \pm 0.009\ \mu\text{m}$, spanning over the cavity and ferroelectric layer.

4. **Mesh Refinement**:
   - Multibox refinement window `RefEvalWin.active` placed at the critical source-channel tunneling interface ($X \in [0.005, 0.132]\ \mu\text{m}$) with $1\text{ nm} \times 0.1\text{ nm}$ minimum grid spacing.
