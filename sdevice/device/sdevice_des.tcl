# ==============================================================================
# Sentaurus Device (SDevice) Simulation Deck
# Project: FE-DGDM-JLTFET Biosensor Electrical & Sensitivity Simulation
# Author: Allen Joe A (24BVD1100), Guided by: Lakshmi B
# Reference: IEEE Sensors Journal, Vol. 24, No. 22, pp. 37923-37930 (Nov 2024)
# ==============================================================================
# Simulation Specifications:
# - Transport: Hydrodynamic with Fermi-Dirac statistics
# - Bandgap Narrowing: OldSlotboom model
# - Tunneling: Nonlocal dynamic band-to-band tunneling (Hurkx model)
# - Ferroelectric Physics: Landau-Devonshire polarization (FEPolarization) in HfO2
# - Mobility: Philips Unified Mobility (PhuMob), Lombardi surface roughness (Enormal),
#             Canali high-field saturation (eHighFieldSaturation)
# - Recombination: SRH (doping-dependent), Auger, Hurkx Band-to-Band
# ==============================================================================

Electrode {
    { name="d" voltage=0.0 Resistor=10 }
    { name="s" voltage=0.0 Resistor=10 }
    { name="g" voltage=0.0 WorkFunction=@WF@ }
}

File {
    Grid      = "@tdr@"
    Plot      = "@tdrdat@"
    Current   = "@plot@"
    parameter = "sdevice.par"
}

Physics {
    Temperature = 300
    Hydrodynamic
    EffectiveIntrinsicDensity( OldSlotboom )
}

Physics( Material="Silicon" ) {
    Fermi
    Mobility(
        PhuMob
        eHighFieldSaturation( CarrierTempDrive )
        hHighFieldSaturation( GradQuasiFermi )
        Enormal( Lombardi )
    )
    Recombination(
        eBarrierTunneling( Band2Band TwoBand Transmission )
        hBarrierTunneling( Band2Band TwoBand Transmission )
        SRH( DopingDep )
        Band2Band( Model = Hurkx )
    )
}

Physics( Region="hfo2t" ) {
    FEPolarization
}

Physics( Region="hfo2b" ) {
    FEPolarization
}

Math ( RegionInterface="channel/source" ) {
    NonLocal( Length=30e-7 Permeation=3e-7 Permeable )
}

Math {
    Extrapolate
    RelErrControl
    Digits           = 8
    ErRef(Electron)  = 1.e8
    ErRef(Hole)      = 1.e8
    NotDamped        = 25
    Iterations       = 25
    TensorGridAniso
    NumberOfThreads  = maximum
}

Plot {
    eDensity hDensity
    eCurrent hCurrent
    TotalCurrent/Vector eCurrent/Vector hCurrent/Vector
    eMobility hMobility
    eVelocity hVelocity
    eEnormal hEnormal
    ElectricField/Vector Potential SpaceCharge
    eQuasiFermi hQuasiFermi
    Potential Doping SpaceCharge
    SRH Auger
    AvalancheGeneration
    DonorConcentration AcceptorConcentration
    Doping
    eGradQuasiFermi/Vector hGradQuasiFermi/Vector
    eEparallel hEparallel
    BandGap
    BandGapNarrowing
    Affinity
    ConductionBand ValenceBand
    eQuantumPotential
    eBarrierTunneling hBarrierTunneling
    HeavyIonChargeDensity
    StressXX
    eBand2BandGeneration
    hBand2BandGeneration
    Polarization
    Polarization/Vector
}

Solve {
    # 1. Equilibrium Poisson initial solution
    Coupled ( Iterations=100 LineSearchDamping=1e-4 ) { Poisson }
    Coupled { Poisson Electron }

    # 2. Quasistationary ramp of Drain Voltage (Vds) to target bias
    Quasistationary(
        InitialStep = 1e-3
        Increment   = 1.2
        MinStep     = 1e-6
        MaxStep     = 0.2
        Goal { Name="d" Voltage=@vd@ }
    ) { Coupled { Poisson Electron } }

    # 3. Quasistationary gate voltage sweep (Vgs) for transfer characteristics
    Quasistationary(
        DoZero
        InitialStep = 1e-3
        Increment   = 1.2
        MinStep     = 1e-6
        MaxStep     = 0.2
        Goal { Name="g" Voltage=@vg@ }
    ) { Coupled { Poisson Electron } }
}
