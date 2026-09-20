# Analysis Scripts Directory

Python/Matlab scripts for data extraction, processing, and plotting.

## Current Status

**Empty** — No analysis scripts in the current repository.

## Recommended Scripts

| Script | Purpose |
|--------|---------|
| `extract_iv.py` | Parse SDevice `.plt`/`.dat` → Ion, Ioff, SS, VT |
| `plot_sweeps.py` | Generate comparison plots from CSV |
| `sensitivity_calc.py` | Compute ΔI/I, ΔVT per parameter unit |
| `band_diagram.py` | Extract 1D band profiles from 2D data |
| `export_csv.py` | Batch export all `.plt` to CSV |

## Workflow

```bash
# 1. Export numerical data from SDevice
sdevice_extract -input results.raw -output results/raw_data/

# 2. Run analysis scripts
python analysis/scripts/extract_iv.py
python analysis/scripts/plot_sweeps.py

# 3. Generate figures
python analysis/scripts/plot_publication.py
```

## Dependencies

- Python 3.8+
- `numpy`, `pandas`, `matplotlib`, `scipy`
- Optional: `originpro` (for Origin automation)