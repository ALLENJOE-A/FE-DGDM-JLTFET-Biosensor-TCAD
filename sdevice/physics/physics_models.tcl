# ==============================================================================
# Sentaurus Device Physics & Material Models Configuration
# Project: FE-DGDM-JLTFET Biosensor
# Author: Allen Joe A (24BVD1100), Guided by: Lakshmi B
# Reference: IEEE Sensors Journal, Vol. 24, No. 22, pp. 37923-37930 (Nov 2024)
# ==============================================================================

# Global Device Physics Card
Physics {
    Temperature = 300
    Hydrodynamic
    EffectiveIntrinsicDensity( OldSlotboom )
}

# Silicon Active Material Physics Card
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

# Negative Capacitance Ferroelectric Material Physics Card
Physics( Region="hfo2t" ) {
    FEPolarization
}

Physics( Region="hfo2b" ) {
    FEPolarization
}

# Tunneling Interface Non-Local Formulation
Math ( RegionInterface="channel/source" ) {
    NonLocal( Length=30e-7 Permeation=3e-7 Permeable )
}
