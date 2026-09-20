# Figures Directory

Publication-ready figures for papers, presentations, and portfolio.

## Structure

```
figures/
├── device/           # Device architecture diagrams (empty - needed)
├── electrical/       # Transfer characteristics
├── physics/          # 2D physics contours (E-field, potential, bands)
├── sensing/          # Biosensing response curves
└── optimization/     # Parameter optimization plots
```

## Current Contents

| Directory | Files | Description |
|-----------|-------|-------------|
| `device/` | *(empty)* | Need: cross-section, 3D view, band diagram schematic |
| `electrical/` | `id_vgs_qf_neutral.png`, `ioff_vgs_qf_neutral.png` | QF Neutral transfer curves |
| `physics/` | `electric_field_distribution.png` | Peak E-field at tunnel junction |
| `sensing/` | `ion_cavity.png`, `ioff_cavity.png` | Cavity thickness sensitivity |
| `optimization/` | `ion_k_values.png`, `ioff_k_values.png` | K-value optimization |

## Figure Guidelines

For future additions, follow these standards:

- **Format**: PNG (for GitHub) + PDF/SVG (for papers)
- **Resolution**: ≥300 DPI for raster, vector preferred
- **Fonts**: Arial/Helvetica, 8-10 pt axis labels
- **Axes**: SI units (μA/μm, V, V/cm, eV)
- **Legends**: Clear, inside plot area if possible
- **Color**: Colorblind-safe palette (viridis, cividis, or Okabe-Ito)

## Generating New Figures

```python
# Example: Extract data from SDevice .plt → Plot with matplotlib
import matplotlib.pyplot as plt
# ... load data ...
plt.savefig('figures/electrical/id_vgs.pdf', dpi=300, bbox_inches='tight')
```

## Missing Figures (Recommended)

1. **Device architecture** — Cross-section with labels
2. **Energy band diagram** — Annotated schematic (OFF/ON states)
3. **Sensing mechanism** — Biomolecule in cavity → ΔVT illustration
4. **Comparison plot** — Baseline vs FE-DGDM-JLTFET
5. **Sensitivity vs concentration** — When biomolecule data available