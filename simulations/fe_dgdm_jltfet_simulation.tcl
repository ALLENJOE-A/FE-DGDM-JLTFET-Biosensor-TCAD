# ==============================================================================
# Sentaurus Workbench (SWB) Tcl Automation Deck
# Project: Parametric Study of FE-DGDM-JLTFET Biosensor
# Author: Allen Joe A (24BVD1100), Guided by: Lakshmi B
# Reference: IEEE Sensors Journal, Vol. 24, No. 22, pp. 37923-37930 (Nov 2024)
# ==============================================================================
# This script organizes the parametric simulations across:
# 1. Cavity length variation: Lcav = 30 nm, 35 nm, 40 nm
# 2. Cavity dielectric constant (biomolecule K): K = 1, 3, 5, 7, 12, 22
#    - K = 1  : Air reference (empty cavity)
#    - K = 3  : Lipids
#    - K = 5  : Carbohydrates
#    - K = 7  : Zein protein
#    - K = 12 : Amino acids
#    - K = 22 : MDA-MB-231 (breast cancer cell line)
# 3. Fixed charge density (QF polarity sweep):
#    - Neutral: QF = 0
#    - Positive: +1e10, +5e11, +1e12 cm^-2
#    - Negative: -1e10, -5e11, -1e12 cm^-2
# ==============================================================================

proc run_simulation {case_name l_cav k_val qf_val vd_val vg_stop} {
    puts "=========================================================="
    puts "Executing TCAD simulation: $case_name"
    puts "  Cavity Length (Lcav)  : ${l_cav} nm"
    puts "  Dielectric Constant K : ${k_val}"
    puts "  Fixed Charge (QF)     : ${qf_val} cm^-2"
    puts "  Drain Bias (Vds)      : ${vd_val} V"
    puts "  Gate Voltage Stop     : ${vg_stop} V"
    puts "=========================================================="

    # In a live Sentaurus Workbench environment:
    # 1. Substitute variables in SDE deck (sde_dvs.tcl)
    # 2. Execute mesh generation: snmesh -a n${node}
    # 3. Substitute variables in parameter file (sdevice.par) for cavity K
    # 4. Substitute variables in SDevice deck (sdevice_des.tcl)
    # 5. Run device solver: sdevice sdevice_des.cmd
    # 6. Extract electrical metrics: Inspect / SVisual
}

# Example parameter sweep execution definitions:

# 1. Cavity length sweep (Air reference K=1, QF=0, Vds=1.0 V)
set cavity_lengths [list 30 35 40]
foreach lc $cavity_lengths {
    run_simulation "CavityLength_${lc}nm" $lc 1.0 0.0 1.0 1.5
}

# 2. Biomolecule Dielectric Constant K sweep (Lcav=30 nm, QF=0, Vds=1.0 V)
set k_values [list 1 3 5 7 12 22]
foreach k $k_values {
    run_simulation "Biomolecule_K_${k}" 30 $k 0.0 1.0 1.5
}

# 3. Positive Fixed Charge sweep (Lcav=30 nm, K=10 and K=22)
set qf_positive [list 1e10 5e11 1e12]
foreach qf $qf_positive {
    run_simulation "QF_Positive_${qf}" 30 22 $qf 1.0 1.5
}

# 4. Negative Fixed Charge sweep (Lcav=30 nm, K=10 and K=22)
set qf_negative [list -1e10 -5e11 -1e12]
foreach qf $qf_negative {
    run_simulation "QF_Negative_${qf}" 30 22 $qf 1.0 1.5
}

puts "SWB Tcl Automation script completed."
