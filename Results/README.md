# Results Directory

Organized simulation outputs categorized by analysis type.

## Structure

```
results/
├── electrical/       # QF Neutral: Transfer characteristics (Ion, Ioff)
├── electrostatic/    # (Empty - 2D plots in sensitivity/optimization)
├── sensitivity/      # Cavity sweep + QF Negative/Positive
├── optimization/     # K-value sweep
└── raw_data/         # (Empty - CSV/DAT exports needed)
```

## Subdirectories

### `electrical/`
QF Neutral (baseline-like) transfer curves:
- `Ion_QF_neutral.png` — ON-current vs VGS
- `Ioff_QF_neutral.png` — OFF-current vs VGS
- `band_diagram_QF_neutral.png` — Energy band at relevant bias
- `surface_potential_QF_neutral.png` — Surface potential contour

### `sensitivity/`
Biomolecule-sensitivity related sweeps:
- **Cavity Thickness**: `Ion_Cavity.png`, `Ioff_Cavity.png`, `energy_band_Cavity.png`, `surface_potential_Cavity.png`
- **QF Negative**: `band_diagram_QF_negative.png`, `electric_field_QF_negative.png` (typo: "elctric"), `Ioff_Cavity.png`, `Ion_Cavity.png`, `Surface_potential.png`, `surface_potential_Cavity.png`
- **QF Positive**: `Ioff_QF_positive.png`, `electric_field_QF_positive.png`
- `Description_Cavity_Length.txt` — "Analysis of Different Cavity Thickness Values"

### `optimization/`
Ferroelectric material optimization (K sweep):
- `Ion_K_values.png`, `Ioff_K_values.png`
- `band_diagram_K_values.png` (typo: "digram")
- `electric_field_K_values.png`
- `surface_potential_K_values.png`

### `raw_data/`
**Empty** — Numerical data exports (CSV) needed for:
- Quantitative comparison tables
- Origin/Python replotting
- Statistical analysis

---

## File Naming Convention

| Pattern | Meaning |
|---------|---------|
| `{Quantity}_{Sweep}.png` | e.g., `Ion_Cavity.png` |
| `{Quantity}_QF_{polarity}.png` | e.g., `Ioff_QF_positive.png` |
| `{Quantity}_K_values.png` | K-value sweep |
| `Description_{Sweep}.txt` | Sweep description |

## Missing Data

| Data Type | Status |
|-----------|--------|
| Numerical CSV exports | Not available |
| Subthreshold swing values | Extractable from plots |
| Threshold voltage values | Extractable from plots |
| Ion/Ioff ratios | Extractable from plots |
| Sensitivity metrics (ΔI/I) | Not computed |