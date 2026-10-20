# Authoritative Technical References
**Project:** Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET (FE-DGDM-JLTFET) Biosensor TCAD  
**Repository:** [ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD](https://github.com/ALLENJOE-A/FE-DGDM-JLTFET-Biosensor-TCAD)

---

## 1. Primary Academic Literature

The device design, physical models, and simulation methodology implemented in this internship repository are grounded in the following authoritative peer-reviewed publications:

### Steep-Slope Tunnel FET Operation & Band-to-Band Tunneling
1. **A. M. Ionescu and H. Riel**, "Tunnel field-effect transistors as energy-efficient electronic switches," *Nature*, vol. 479, no. 7373, pp. 329–337, Nov. 2011.  
   DOI: [10.1038/nature10679](https://doi.org/10.1038/nature10679)  
   *Foundational review of band-to-band tunneling physics, energy filtering, and sub-60 mV/dec subthreshold swing principles.*

2. **W. Y. Choi, B.-G. Park, J. D. Lee, and T.-J. K. Liu**, "Tunneling Field-Effect Transistors (TFETs) With Subthreshold Swing (SS) Less Than 60 mV/dec," *IEEE Electron Device Letters*, vol. 28, no. 8, pp. 743–745, Aug. 2007.  
   DOI: [10.1109/LED.2007.901273](https://doi.org/10.1109/LED.2007.901273)  
   *Experimental demonstration of sub-thermal subthreshold swing at room temperature in silicon TFET architectures.*

### Negative Capacitance & Ferroelectric Gate Stacks
3. **S. Salahuddin and S. Datta**, "Use of Negative Capacitance to Provide Voltage Amplification for Low Power Nanoscale Devices," *Nano Letters*, vol. 8, no. 2, pp. 405–410, Feb. 2008.  
   DOI: [10.1021/nl071804g](https://doi.org/10.1021/nl071804g)  
   *Theoretical formulation of internal voltage amplification ($m < 1$) via Landau-Khalatnikov ferroelectric negative capacitance.*

4. **A. I. Khan et al.**, "Negative capacitance in a ferroelectric capacitor," *Nature Materials*, vol. 14, no. 2, pp. 182–186, Feb. 2015.  
   DOI: [10.1038/nmat4148](https://doi.org/10.1038/nmat4148)  
   *Experimental verification of steady-state negative capacitance in ferroelectric thin films.*

### Junctionless Transistors
5. **J.-P. Colinge et al.**, "Nanowire transistors without junctions," *Nature Nanotechnology*, vol. 5, no. 3, pp. 225–229, Mar. 2010.  
   DOI: [10.1038/nnano.2010.15](https://doi.org/10.1038/nnano.2010.15)  
   *Introduction of junctionless field-effect transistors with uniform doping and absence of metallurgical p-n transitions.*

### Nanocavity & Dielectric-Modulated Biosensors
6. **D. Sarkar et al.**, "A subthreshold-swing sub-60 mV/decade tunnel field-effect transistor biosensor," *ACS Nano*, vol. 8, no. 4, pp. 3992–4003, Apr. 2014.  
   DOI: [10.1021/nn500914r](https://doi.org/10.1021/nn500914r)  
   *Comprehensive experimental and theoretical framework for biomolecule detection leveraging steep-slope TFET sensitivity.*

7. **P. Sharma, A. S. Augustine, and P. K. Tiwari**, "Dielectric-Modulated Double-Gate Junctionless Tunnel Field-Effect Transistor for Label-Free Biomolecule Detection," *IEEE Transactions on Electron Devices*, vol. 66, no. 10, pp. 4380–4386, Oct. 2019.  
   DOI: [10.1109/TED.2019.2934898](https://doi.org/10.1109/TED.2019.2934898)  
   *TCAD analysis of junctionless TFET biosensors utilizing embedded nanocavities.*

---

## 2. Distinction of Work

| Category | Description |
|:---|:---|
| **Established Literature** | General operating principles of TFETs, Landau-Khalatnikov negative capacitance, junctionless uniform doping, and dielectric-modulation theory. |
| **Simulated in this Work** | Systematic TCAD evaluation of an FE-DGDM-JLTFET with T-shaped channel, inverted-T nanocavity ($30, 35, 40\text{ nm}$), ferroelectric $K$-sweep ($1\text{--}22$), and biomolecule charge emulation ($Q_F = \pm 10^{10}\text{ to }\pm 10^{12}\text{ cm}^{-2}$). |
| **Identified Future Research** | Direct simulation of biomolecule dielectric constant ($\kappa_{bio}$), sterics, fluidic Debye screening in electrolyte, and experimental prototype fabrication. |
