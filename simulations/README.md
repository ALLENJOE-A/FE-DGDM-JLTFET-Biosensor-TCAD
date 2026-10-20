# TCAD Simulation Decks & Automation

This directory contains Sentaurus Workbench (SWB) automation and batch simulation scripts for the FE-DGDM-JLTFET biosensor.

## Files

- [`fe_dgdm_jltfet_simulation.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/simulations/fe_dgdm_jltfet_simulation.tcl): Sentaurus Workbench Tcl script to automate parameter sweeps across cavity lengths, biomolecule dielectric constants ($K$), and fixed charges ($Q_F$).

## Automated Sweeps

1. **Cavity Length Variation**:
   - $L_{cav} \in \{30, 35, 40\}\text{ nm}$ at fixed $T_{cav} = 3\text{ nm}$, $V_{DS} = 1.0\text{ V}$.
   - Evaluates impact on tunneling electric field, band bending, and $I_{ON}/I_{OFF}$ ratio.

2. **Biomolecule Dielectric Constant ($K$)**:
   - $K \in \{1, 3, 5, 7, 12, 22\}$ at $L_{cav} = 30\text{ nm}$.
   - Simulates label-free detection from air ($K=1$) up to breast cancer cells MDA-MB-231 ($K=22$).

3. **Fixed Charge Polarity and Density ($Q_F$)**:
   - Neutral ($Q_F = 0$).
   - Positive charges ($+10^{10}, +5\times 10^{11}, +10^{12}\text{ cm}^{-2}$).
   - Negative charges ($-10^{10}, -5\times 10^{11}, -10^{12}\text{ cm}^{-2}$).
