# Sentaurus Device Physics Models

This directory documents the calibrated physics models used in the Sentaurus Device simulations for the FE-DGDM-JLTFET biosensor.

## Files

- [`physics_models.tcl`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/sdevice/physics/physics_models.tcl): The exact physics model definitions including Hydrodynamic transport, Hurkx dynamic non-local BTBT, Landau-Devonshire ferroelectric polarization, PhuMob, and Lombardi models.

## Physics Model Summary

| Physics Phenomenon | Model Card | Parameters / Details |
|--------------------|------------|----------------------|
| **Carrier Transport** | Hydrodynamic + Fermi | Solves energy balance equations with Fermi-Dirac statistics |
| **Bandgap Narrowing** | `OldSlotboom` | $E_{bgn} = 9.0\text{ meV}$, $N_{ref} = 10^{17}\text{ cm}^{-3}$ |
| **Band-to-Band Tunneling** | `Band2Band(Model=Hurkx)` | Non-local dynamically evaluated at source-channel interface |
| **Barrier Transmission** | `eBarrierTunneling / hBarrierTunneling` | TwoBand transmission model |
| **Ferroelectric Polarization**| `FEPolarization` | Landau-Devonshire theory with negative stiffness $\alpha = -3.7 \times 10^{10}\text{ cm/F}$ |
| **Doping-Dependent Mobility** | `PhuMob` | Philips Unified Mobility Model |
| **Surface Roughness** | `Enormal(Lombardi)` | Acoustic phonon and surface roughness scattering degradation |
| **High-Field Saturation** | `eHighFieldSaturation(CarrierTempDrive)` | Carrier temperature-driven velocity saturation |
| **Recombination** | `SRH(DopingDep)` + `Auger` | Scharfetter relation with doping-dependent lifetime |
