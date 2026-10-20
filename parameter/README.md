# Sentaurus Device Parameter Directory

This directory contains material, transport, and ferroelectric parameter files utilized in the TCAD device simulations.

## Files

- [`sdevice.par`](file:///D:/3RD%20YEAR%20MATERIALS/AGY/FE-DGDM-JLTFET-Biosensor-TCAD/parameter/sdevice.par): Verified Sentaurus parameter file providing calibrated material properties for Silicon, $\text{SiO}_2$ (oxide), $\text{HfO}_2$ (ferroelectric), and Vacuum (nanocavity).

## Key Parameters Defined

### 1. Silicon (Channel & S/D)
- **Hurkx BTBT**: $A = 8.9770 \times 10^{20}\text{ cm}^{-1}\text{s}^{-1}\text{V}^{-2}$, $B = 2.1466 \times 10^{7}\text{ V/cm}$, $\hbar\Omega = 18.6\text{ meV}$.
- **Permittivity**: $\epsilon_r = 11.7$.
- **Bandgap**: $E_{g0} = 1.12\text{ eV}$, $\chi_0 = 4.05\text{ eV}$.
- **OldSlotboom BGN**: $E_{bgn} = 9.0\text{ meV}$, $N_{ref} = 1.0 \times 10^{17}\text{ cm}^{-3}$.
- **Lattice Mobility**: $\mu_{max,e} = 1445\text{ cm}^2/\text{V}\cdot\text{s}$, $\mu_{max,h} = 486\text{ cm}^2/\text{V}\cdot\text{s}$.
- **Saturation Velocity**: $v_{sat} = 1.01 \times 10^{7}\text{ cm/s}$.

### 2. Ferroelectric Stack ($\text{Si:HfO}_2$)
- **Permittivity**: $\epsilon_r = 31.0$.
- **Landau-Devonshire Parameters**:
  - $\alpha = -3.7 \times 10^{10}\text{ cm/F}$ (negative stiffness parameter enabling negative capacitance).
  - $\beta = 2.5 \times 10^{21}\text{ cm}^5/(\text{F}\cdot\text{C}^2)$.
  - $\gamma = 0.0$.
- **Polarization**: Remanent polarization $P_r = 1\ \mu\text{C/cm}^2$, Saturation polarization $P_s = 20\ \mu\text{C/cm}^2$, Coercive field $E_c = 1\text{ MV/cm}$.
- **Bandgap**: $E_{g0} = 5.58\text{ eV}$, $\chi_0 = 2.15\text{ eV}$.

### 3. Interfacial and Underlap Oxide ($\text{SiO}_2$)
- **Permittivity**: $\epsilon_r = 3.9$.
- **Bandgap**: $E_{g0} = 9.0\text{ eV}$, $\chi_0 = 0.9\text{ eV}$.

### 4. Nanocavity (Sensing Region)
- **Reference**: $\epsilon_r = 1.0$ (air / vacuum).
- **Modulated Permittivity**: Varied during biosensing runs to represent target analytes ($K = 3$ lipids, $K = 5$ carbohydrates, $K = 7$ zein protein, $K = 12$ amino acids, $K = 22$ MDA-MB-231 breast cancer cells).
