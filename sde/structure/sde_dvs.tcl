# ==============================================================================
# Sentaurus Structure Editor (SDE) Input Deck
# Project: FE-DGDM-JLTFET Biosensor Device Generation
# Author: Allen Joe A (24BVD1100), Guided by: Lakshmi B
# Reference: IEEE Sensors Journal, Vol. 24, No. 22, pp. 37923-37930 (Nov 2024)
# ==============================================================================
# Device Architecture Summary:
# - Device: Ferroelectric Double-Gate Doping-Modulated Junctionless Tunnel FET
# - Total Device Length (X): 0.158 um (158 nm)
# - Source: X in [0.000, 0.010] um, Y in [-0.011, +0.011] um (As = 1e19 cm^-3)
# - Source Wings (sourcet/b): X in [0.010, 0.055] um, Y in [+/-0.009, +/-0.011] um (As = 1e19 cm^-3)
# - Channel Body: X in [0.010, 0.103] um, Y in [-0.005, +0.005] um (As = 1e15 cm^-3)
# - Drain Extension (channelde): X in [0.103, 0.148] um, Y in [-0.008, +0.008] um (As = 1e15 cm^-3)
# - Drain: X in [0.148, 0.158] um, Y in [-0.009, +0.009] um (As = 1e20 cm^-3)
# - Interfacial Oxide (oxide1, oxide2): 1 nm SiO2, Y in [+/-0.005, +/-0.006] um
# - Gate Underlap Oxide (sio2t, sio2b): 3 nm SiO2, X in [0.010, 0.045] um, Y in [+/-0.006, +/-0.009] um
# - Inverted-T Nanocavity (vac1, vac2): 30 nm cavity (X in [0.045, 0.075] um, Y in [+/-0.006, +/-0.009] um)
# - Ferroelectric Stack (hfo2t, hfo2b): 28 nm Si:HfO2 (X in [0.075, 0.103] um, Y in [+/-0.006, +/-0.009] um)
# ==============================================================================

(sdegeo:set-auto-region-naming OFF)

# ------------------------------------------------------------------------------
# 1. Silicon Channel and Extensions (Doping-Modulated Junctionless Body)
# ------------------------------------------------------------------------------
# Central thin silicon channel body (thickness Tch = 10 nm)
(bound? (quote channel))
(sdegeo:create-rectangle (position 0.010 -0.005 0) (position 0.103 0.005 0) "Silicon" "channel")

# Silicon channel drain extension (thickness = 16 nm)
(bound? (quote channelde))
(sdegeo:create-rectangle (position 0.103 -0.008 0) (position 0.148 0.008 0) "Silicon" "channelde")

# Main Silicon Source Region (thickness = 22 nm)
(bound? (quote source))
(sdegeo:create-rectangle (position 0.000 -0.011 0) (position 0.010 0.011 0) "Silicon" "source")

# Silicon Drain Region (thickness = 18 nm)
(bound? (quote drain))
(sdegeo:create-rectangle (position 0.148 -0.009 0) (position 0.158 0.009 0) "Silicon" "drain")
(roll)
(bound? (quote drain))
(sdegeo:create-rectangle (position 0.148 0.008 0) (position 0.158 -0.008 0) "Silicon" "drain")

# Source extensions (wings) forming T-shaped source / channel overlap
(sde:set-default-material "Silicon")
(bound? (quote sourcet))
(sdegeo:create-rectangle (position 0.010 -0.011 0) (position 0.055 -0.009 0) "Silicon" "sourcet")

(bound? (quote sourceb))
(sdegeo:create-rectangle (position 0.010 0.011 0) (position 0.055 0.009 0) "Silicon" "sourceb")

# ------------------------------------------------------------------------------
# 2. Gate Dielectrics and Nanocavity Definition
# ------------------------------------------------------------------------------
(sde:set-default-material "SiO2")

# Interfacial Oxide (Tox = 1 nm) between channel and gate/cavity
(bound? (quote oxide1))
(sdegeo:create-rectangle (position 0.010 -0.006 0) (position 0.103 -0.005 0) "SiO2" "oxide1")

(bound? (quote oxide2))
(sdegeo:create-rectangle (position 0.010 0.005 0) (position 0.103 0.006 0) "SiO2" "oxide2")

# Oxide along channel drain extension
(bound? (quote oxide3))
(sdegeo:create-rectangle (position 0.103 -0.008 0) (position 0.148 -0.007 0) "SiO2" "oxide3")
(roll)
(bound? (quote oxide3))
(sdegeo:create-rectangle (position 0.103 -0.008 0) (position 0.148 -0.009 0) "SiO2" "oxide3")

(bound? (quote oxide4))
(sdegeo:create-rectangle (position 0.103 0.008 0) (position 0.148 0.009 0) "SiO2" "oxide4")

# Underlap SiO2 layer under source extensions
(bound? (quote sio2t))
(sdegeo:create-rectangle (position 0.010 -0.009 0) (position 0.045 -0.006 0) "SiO2" "sio2t")

(bound? (quote sio2b))
(sdegeo:create-rectangle (position 0.010 0.006 0) (position 0.045 0.009 0) "SiO2" "sio2b")

# Ferroelectric Gate Stack (Si:HfO2, 3 nm thickness, L_FE = 28 nm)
(sde:set-default-material "HfO2")
(bound? (quote hfo2t))
(sdegeo:create-rectangle (position 0.075 -0.006 0) (position 0.103 -0.009 0) "HfO2" "hfo2t")

(bound? (quote hfo2b))
(sdegeo:create-rectangle (position 0.075 0.006 0) (position 0.103 0.009 0) "HfO2" "hfo2b")

# Inverted-T Nanocavity (Sensing Region, 3 nm thickness, L_cav = 30 nm)
# Split precisely at X = 0.060 um for localized contact alignment
(sde:set-default-material "Vacuum")
(bound? (quote vac1_top))
(sdegeo:create-rectangle (position 0.045 -0.009 0) (position 0.060 -0.006 0) "Vacuum" "vac1_top")

(bound? (quote vac1_bot))
(sdegeo:create-rectangle (position 0.060 -0.009 0) (position 0.075 -0.006 0) "Vacuum" "vac1_bot")

(bound? (quote vac2_top))
(sdegeo:create-rectangle (position 0.045 0.009 0) (position 0.060 0.006 0) "Vacuum" "vac2_top")

(bound? (quote vac2_bot))
(sdegeo:create-rectangle (position 0.060 0.009 0) (position 0.075 0.006 0) "Vacuum" "vac2_bot")

# ------------------------------------------------------------------------------
# 3. Contact Sets and Boundary Assignments
# ------------------------------------------------------------------------------
(sdegeo:define-contact-set "s" 4 (color:rgb 1 0 0) "##")
(sdegeo:define-contact-set "d" 4 (color:rgb 1 0 0) "##")
(sdegeo:define-contact-set "g" 4 (color:rgb 1 0 0) "##")

# Source Contact (left edge X = 0.000 um)
(sdegeo:set-current-contact-set "s")
(sdegeo:set-contact (list (car (find-edge-id (position 0.000 0.000 0)))) "s")

# Drain Contact (right edge X = 0.158 um)
(sdegeo:set-current-contact-set "d")
(sdegeo:set-contact (list (car (find-edge-id (position 0.158 0.000 0)))) "d")

# Top and Bottom Gate Contacts (centered over cavity and ferroelectric stack)
(sdegeo:set-current-contact-set "g")
(sdegeo:set-contact (list (car (find-edge-id (position 0.0675 -0.009 0)))) "g")
(sdegeo:set-contact (list (car (find-edge-id (position 0.0675 0.009 0)))) "g")

# ------------------------------------------------------------------------------
# 4. Doping Profiles (Junctionless n-type Modulation)
# ------------------------------------------------------------------------------
# Channel and Drain Extension: Arsenic active concentration = 1e15 cm^-3
(sdedr:define-constant-profile "ConstantProfileDefinition.channel" "ArsenicActiveConcentration" 1e+15)
(sdedr:define-constant-profile-region "ConstantProfilePlacement.channel" "ConstantProfileDefinition.channel" "channel")

(sdedr:define-constant-profile "ConstantProfileDefinition.channelde" "ArsenicActiveConcentration" 1e+15)
(sdedr:define-constant-profile-region "ConstantProfilePlacement.channelde" "ConstantProfileDefinition.channelde" "channelde")

# Source and Source Wings: Heavily doped Arsenic active concentration = 1e19 cm^-3
(sdedr:define-constant-profile "ConstantProfileDefinition.source" "ArsenicActiveConcentration" 1e+19)
(sdedr:define-constant-profile-region "ConstantProfilePlacement.source" "ConstantProfileDefinition.source" "source")

(sdedr:define-constant-profile "ConstantProfileDefinition.sourcet" "ArsenicActiveConcentration" 1e+19)
(sdedr:define-constant-profile-region "ConstantProfilePlacement.sourcet" "ConstantProfileDefinition.sourcet" "sourcet")

(sdedr:define-constant-profile "ConstantProfileDefinition.sourceb" "ArsenicActiveConcentration" 1e+19)
(sdedr:define-constant-profile-region "ConstantProfilePlacement.sourceb" "ConstantProfileDefinition.sourceb" "sourceb")

# Drain: Ultra-heavily doped Arsenic active concentration = 1e20 cm^-3
(sdedr:define-constant-profile "ConstantProfileDefinition.drain" "ArsenicActiveConcentration" 1e+20)
(sdedr:define-constant-profile-region "ConstantProfilePlacement.drain" "ConstantProfileDefinition.drain" "drain")

# ------------------------------------------------------------------------------
# 5. Mesh Refinement and Multi-Box Windows
# ------------------------------------------------------------------------------
# Global mesh window
(bound? (quote RefEvalWin.all))
(sdedr:define-refeval-window "RefEvalWin.all" "Rectangle" (position -0.0038 -0.0141 0) (position 0.1632 0.0153 0))
(sdedr:define-refinement-size "RefinementDefinition_1" 0.002 0.002 0.0002 0.0002)
(sdedr:define-refinement-placement "RefinementPlacement.all" "RefinementDefinition_1" (list "window" "RefEvalWin.all"))

# Active Tunneling Interface Refinement Window (Sub-nanometer precision for BTBT)
(bound? (quote RefEvalWin.active))
(sdedr:define-refeval-window "RefEvalWin.active" "Rectangle" (position 0.005 -0.0078 0) (position 0.132 0.008 0))
(sdedr:define-multibox-size "MultiboxDefinition.active" 0.001 0.001 0.0001 0.0001 1 1)
(sdedr:define-multibox-placement "MultiboxPlacement.active" "MultiboxDefinition.active" "RefEvalWin.active")

(sdedr:define-refinement-size "RefinementDefinition.all" 0.002 0.002 0.0002 0.0002)
(sdedr:define-refinement-placement "RefinementPlacement.all" "RefinementDefinition.all" (list "window" "RefEvalWin.all"))

# ------------------------------------------------------------------------------
# 6. Mesh Generation and Model Export
# ------------------------------------------------------------------------------
(sde:set-meshing-command "snmesh -a")
(sdedr:append-cmd-file "")
(sde:build-mesh "-a" "n@node@")
(system:command "svisual sdemodel_msh.tdr &")
(sde:xshow-material "nomat")
(sde:save-model "n@node@")
