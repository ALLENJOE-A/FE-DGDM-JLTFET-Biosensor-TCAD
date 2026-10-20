# Sentaurus Device (SDevice) Simulation Decks

This directory contains the verified Sentaurus Device (SDevice) simulation decks for the FE-DGDM-JLTFET biosensor.

## Files

- [`sdevice_des.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/sdevice/device/sdevice_des.tcl): The primary Sentaurus Device command deck specifying electrodes, transport models, tunneling, recombination, math solvers, and quasistationary ramp sequences.

## Physics and Models Implemented

1. **Carrier Transport**:
   - Hydrodynamic transport model accounting for non-local carrier heating.
   - Fermi-Dirac statistics (`Fermi`).
   - OldSlotboom bandgap narrowing (`EffectiveIntrinsicDensity( OldSlotboom )`).

2. **Band-to-Band Tunneling (BTBT)**:
   - Dynamic non-local Hurkx BTBT model at the critical source-channel interface (`Math (RegionInterface="channel/source") { NonLocal(Length=30e-7 Permeation=3e-7 Permeable) }`).
   - Two-band barrier tunneling transmission for electrons and holes (`eBarrierTunneling`, `hBarrierTunneling`).

3. **Ferroelectric Polarization**:
   - Native Landau-Devonshire ferroelectric polarization (`FEPolarization`) applied to top and bottom $\text{HfO}_2$ regions (`hfo2t`, `hfo2b`).

4. **Mobility and Recombination**:
   - Philips Unified Mobility Model (`PhuMob`) for concentration and temperature-dependent mobility.
   - Lombardi surface-roughness mobility model (`Enormal(Lombardi)`).
   - High-field saturation (`eHighFieldSaturation(CarrierTempDrive)`, `hHighFieldSaturation(GradQuasiFermi)`).
   - Doping-dependent Shockley-Read-Hall (SRH) and Auger recombination.

5. **Numerical Solvers**:
   - Fully coupled Newton solver (`Coupled { Poisson Electron }`).
   - Quasistationary ramping of drain bias ($V_{DS}$) followed by fine-step gate bias ($V_{GS}$) sweep up to goal voltage.
