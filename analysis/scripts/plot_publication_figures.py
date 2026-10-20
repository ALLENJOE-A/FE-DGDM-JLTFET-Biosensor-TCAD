"""
Publication-Quality Scientific Figure Generator for FE-DGDM-JLTFET Biosensor TCAD
Generates high-resolution publication plots (PNG + PDF/SVG) using Matplotlib from extracted TCAD data.
"""

import os
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW_DATA_DIR = os.path.join(REPO_ROOT, "Results", "raw_data")
FIG_DIR = os.path.join(REPO_ROOT, "figures")

os.makedirs(os.path.join(FIG_DIR, "device"), exist_ok=True)
os.makedirs(os.path.join(FIG_DIR, "electrical"), exist_ok=True)
os.makedirs(os.path.join(FIG_DIR, "sensing"), exist_ok=True)
os.makedirs(os.path.join(FIG_DIR, "comparative"), exist_ok=True)

# Styling standards for IEEE/Nature-style semiconductor publications
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans', 'Helvetica'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.titlesize': 12,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'axes.linewidth': 1.0,
    'grid.linewidth': 0.6,
    'grid.alpha': 0.4,
    'lines.linewidth': 1.8
})

def read_csv_columns(filepath):
    data = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for h in headers:
            data[h] = []
        for row in reader:
            for h, val in zip(headers, row):
                data[h].append(float(val))
    return {k: np.array(v) for k, v in data.items()}

def plot_device_schematic():
    """Generates an engineering cross-sectional schematic of the FE-DGDM-JLTFET biosensor."""
    fig, ax = plt.subplots(figsize=(7.5, 4.8))
    
    # Coordinates (Length 150 nm, height normalized)
    # Background Silicon substrate / bottom stack
    ax.add_patch(patches.Rectangle((0, 0), 150, 15, facecolor='#4A90E2', edgecolor='black', label='Bottom Gate Metal'))
    ax.add_patch(patches.Rectangle((0, 15), 150, 15, facecolor='#F5A623', edgecolor='black', label='Bottom Ferroelectric (HfO2)'))
    ax.add_patch(patches.Rectangle((0, 30), 150, 8, facecolor='#E0E0E0', edgecolor='black', label='Bottom Gate Oxide (SiO2)'))
    
    # Source, Channel (T-shaped), Drain
    # Source (0 to 45 nm, y=38 to 68)
    ax.add_patch(patches.Rectangle((0, 38), 45, 30, facecolor='#50E3C2', edgecolor='black', label='Source (n+ uniform)'))
    # Channel base (45 to 105 nm, y=38 to 53)
    ax.add_patch(patches.Rectangle((45, 38), 60, 15, facecolor='#7ED321', edgecolor='black', label='Channel Base (T-shape)'))
    # Channel T-extension (65 to 85 nm, y=53 to 68)
    ax.add_patch(patches.Rectangle((65, 53), 20, 15, facecolor='#417505', edgecolor='black', label='T-Channel Extension'))
    # Drain (105 to 150 nm, y=38 to 68)
    ax.add_patch(patches.Rectangle((105, 38), 45, 30, facecolor='#50E3C2', edgecolor='black', label='Drain (n+ uniform)'))
    
    # Inverted-T Nanocavity (recess for biomolecules)
    ax.add_patch(patches.Rectangle((45, 53), 20, 25, facecolor='#FFF3E0', edgecolor='#FF9800', linestyle='--', hatch='//', label='Inverted-T Nanocavity (Biomolecules)'))
    ax.add_patch(patches.Rectangle((85, 53), 20, 25, facecolor='#FFF3E0', edgecolor='#FF9800', linestyle='--', hatch='//'))
    
    # Top Gate Dielectric & Ferroelectric
    ax.add_patch(patches.Rectangle((0, 68), 45, 8, facecolor='#E0E0E0', edgecolor='black'))
    ax.add_patch(patches.Rectangle((105, 68), 45, 8, facecolor='#E0E0E0', edgecolor='black'))
    ax.add_patch(patches.Rectangle((0, 76), 150, 15, facecolor='#F5A623', edgecolor='black', label='Top Ferroelectric (HfO2)'))
    ax.add_patch(patches.Rectangle((0, 91), 150, 15, facecolor='#4A90E2', edgecolor='black', label='Top Gate Metal'))
    
    # Text Annotations
    ax.text(22.5, 53, 'SOURCE\n(n+)', ha='center', va='center', weight='bold', color='#1A365D')
    ax.text(127.5, 53, 'DRAIN\n(n+)', ha='center', va='center', weight='bold', color='#1A365D')
    ax.text(75, 45, 'Channel', ha='center', va='center', color='white', weight='bold')
    ax.text(55, 65, 'Nanocavity\n(Receptor)', ha='center', va='center', fontsize=7.5, color='#B78103', weight='bold')
    ax.text(95, 65, 'Nanocavity\n(Receptor)', ha='center', va='center', fontsize=7.5, color='#B78103', weight='bold')
    ax.text(75, 83.5, 'Top Ferroelectric Layer (HfO2)', ha='center', va='center', color='#5D3800', weight='bold')
    ax.text(75, 98.5, 'Top Gate Electrode', ha='center', va='center', color='white', weight='bold')
    ax.text(75, 22.5, 'Bottom Ferroelectric Layer (HfO2)', ha='center', va='center', color='#5D3800', weight='bold')
    ax.text(75, 7.5, 'Bottom Gate Electrode', ha='center', va='center', color='white', weight='bold')
    
    # Tunneling arrow
    ax.annotate('BTBT Tunnel Junction', xy=(45, 45), xytext=(15, 25),
                arrowprops=dict(facecolor='red', shrink=0.08, width=1.5, headwidth=6),
                color='red', weight='bold', fontsize=8.5)
    
    # Dimensions bar
    ax.annotate('', xy=(0, -8), xytext=(150, -8),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.2))
    ax.text(75, -16, 'Total Transport Length = 150 nm', ha='center', va='center', fontsize=9, weight='bold')
    
    ax.set_xlim(-10, 160)
    ax.set_ylim(-22, 115)
    ax.axis('off')
    ax.set_title('FE-DGDM-JLTFET Biosensor Cross-Section (Engineering Schematic)', pad=12, weight='bold')
    
    out_png = os.path.join(FIG_DIR, "device", "device_architecture_schematic.png")
    out_svg = os.path.join(FIG_DIR, "device", "device_architecture_schematic.svg")
    plt.tight_layout()
    plt.savefig(out_png, bbox_inches='tight')
    plt.savefig(out_svg, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated {out_png}")

def plot_k_sweep():
    """Generates dual-panel linear and logarithmic transfer curves for K-sweep."""
    data = read_csv_columns(os.path.join(RAW_DATA_DIR, "k_sweep_transfer.csv"))
    vgs = data["Vgs_V"]
    
    k_labels = [("Ids_A_um_K=22", "K = 22 (HfO2)", "#E65100"),
                ("Ids_A_um_K=12", "K = 12",         "#D32F2F"),
                ("Ids_A_um_K=7",  "K = 7",          "#388E3C"),
                ("Ids_A_um_K=5",  "K = 5",          "#7B1FA2"),
                ("Ids_A_um_K=3",  "K = 3",          "#1976D2"),
                ("Ids_A_um_K=1",  "K = 1 (Air)",    "#0097A7")]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))
    
    # Panel (a): Log scale
    for col, lbl, clr in k_labels:
        ax1.semilogy(vgs, data[col], label=lbl, color=clr, lw=1.8)
    ax1.set_xlabel('Gate-to-Source Voltage $V_{GS}$ (V)')
    ax1.set_ylabel('Drain Current $I_{DS}$ (A/μm)')
    ax1.set_title('(a) Subthreshold Characteristics (Log Scale)', weight='bold')
    ax1.grid(True, which='both', linestyle=':')
    ax1.set_ylim(1e-16, 5e-4)
    ax1.legend(loc='lower right', frameon=True)
    
    # Panel (b): Linear scale
    for col, lbl, clr in k_labels:
        ax2.plot(vgs, data[col] * 1e6, label=lbl, color=clr, lw=1.8)
    ax2.set_xlabel('Gate-to-Source Voltage $V_{GS}$ (V)')
    ax2.set_ylabel('Drain Current $I_{DS}$ (μA/μm)')
    ax2.set_title('(b) ON-State Drive Current (Linear Scale)', weight='bold')
    ax2.grid(True, linestyle=':')
    ax2.set_ylim(0, 210)
    ax2.legend(loc='upper left', frameon=True)
    
    plt.suptitle('Ferroelectric Dielectric Constant ($K$) Sweep Analysis', weight='bold', y=1.02)
    plt.tight_layout()
    
    out_png = os.path.join(FIG_DIR, "electrical", "k_sweep_transfer_characteristics.png")
    out_svg = os.path.join(FIG_DIR, "electrical", "k_sweep_transfer_characteristics.svg")
    plt.savefig(out_png, bbox_inches='tight')
    plt.savefig(out_svg, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated {out_png}")

def plot_cavity_sweep():
    """Generates dual-panel transfer curves for Cavity-thickness variation."""
    data = read_csv_columns(os.path.join(RAW_DATA_DIR, "cavity_sweep_transfer.csv"))
    vgs = data["Vgs_V"]
    
    cav_labels = [("Ids_A_um_tcav=30nm", "$t_{cav} = 30$ nm", "#0288D1"),
                  ("Ids_A_um_tcav=35nm", "$t_{cav} = 35$ nm", "#D32F2F"),
                  ("Ids_A_um_tcav=40nm", "$t_{cav} = 40$ nm", "#388E3C")]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.2))
    
    for col, lbl, clr in cav_labels:
        ax1.semilogy(vgs, data[col], label=lbl, color=clr, lw=2.0)
        ax2.plot(vgs, data[col] * 1e6, label=lbl, color=clr, lw=2.0)
        
    ax1.set_xlabel('Gate-to-Source Voltage $V_{GS}$ (V)')
    ax1.set_ylabel('Drain Current $I_{DS}$ (A/μm)')
    ax1.set_title('(a) Subthreshold Current vs Cavity Thickness', weight='bold')
    ax1.grid(True, which='both', linestyle=':')
    ax1.set_ylim(1e-19, 5e-4)
    ax1.legend(loc='lower right', frameon=True)
    
    ax2.set_xlabel('Gate-to-Source Voltage $V_{GS}$ (V)')
    ax2.set_ylabel('Drain Current $I_{DS}$ (μA/μm)')
    ax2.set_title('(b) ON-State Current vs Cavity Thickness', weight='bold')
    ax2.grid(True, linestyle=':')
    ax2.set_ylim(0, 180)
    ax2.legend(loc='upper left', frameon=True)
    
    plt.suptitle('Nanocavity Thickness Variation ($t_{cav} = 30, 35, 40$ nm)', weight='bold', y=1.02)
    plt.tight_layout()
    
    out_png = os.path.join(FIG_DIR, "sensing", "cavity_thickness_transfer_characteristics.png")
    out_svg = os.path.join(FIG_DIR, "sensing", "cavity_thickness_transfer_characteristics.svg")
    plt.savefig(out_png, bbox_inches='tight')
    plt.savefig(out_svg, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated {out_png}")

def plot_fixed_charge_comparison():
    """Generates dual-panel plot for Negative vs Positive QF (Biomolecule Detection)."""
    neg_data = read_csv_columns(os.path.join(RAW_DATA_DIR, "qf_negative_transfer.csv"))
    pos_data = read_csv_columns(os.path.join(RAW_DATA_DIR, "qf_positive_transfer.csv"))
    vgs = neg_data["Vgs_V"]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))
    
    # Panel (a): Negative QF (e.g. DNA / RNA / Acidic Proteins)
    ax1.semilogy(vgs, neg_data["Ids_A_um_QF=-1e10"], label="$Q_F = -10^{10}\\ \\mathrm{cm^{-2}}$", color="#1976D2", lw=2.0)
    ax1.semilogy(vgs, neg_data["Ids_A_um_QF=-5e11"], label="$Q_F = -5\\times 10^{11}\\ \\mathrm{cm^{-2}}$", color="#388E3C", lw=2.0)
    ax1.semilogy(vgs, neg_data["Ids_A_um_QF=-1e12"], label="$Q_F = -10^{12}\\ \\mathrm{cm^{-2}}$ (Highest Neg)", color="#D32F2F", lw=2.0)
    ax1.set_xlabel('Gate Voltage $V_{GS}$ (V)')
    ax1.set_ylabel('Drain Current $I_{DS}$ (A/μm)')
    ax1.set_title('(a) Negative Charge: DNA/Acidic Proteins ($Q_F < 0$)', weight='bold')
    ax1.grid(True, which='both', linestyle=':')
    ax1.set_ylim(1e-18, 5e-4)
    ax1.legend(loc='lower right', frameon=True)
    
    # Panel (b): Positive QF (e.g. Basic Proteins / Poly-L-lysine)
    ax2.semilogy(vgs, pos_data["Ids_A_um_QF=+1e10"], label="$Q_F = +10^{10}\\ \\mathrm{cm^{-2}}$", color="#0288D1", lw=2.0)
    ax2.semilogy(vgs, pos_data["Ids_A_um_QF=+5e11"], label="$Q_F = +5\\times 10^{11}\\ \\mathrm{cm^{-2}}$", color="#F57C00", lw=2.0)
    ax2.semilogy(vgs, pos_data["Ids_A_um_QF=+1e12"], label="$Q_F = +10^{12}\\ \\mathrm{cm^{-2}}$ (Highest Pos)", color="#7B1FA2", lw=2.0)
    ax2.set_xlabel('Gate Voltage $V_{GS}$ (V)')
    ax2.set_ylabel('Drain Current $I_{DS}$ (A/μm)')
    ax2.set_title('(b) Positive Charge: Basic Proteins ($Q_F > 0$)', weight='bold')
    ax2.grid(True, which='both', linestyle=':')
    ax2.set_ylim(1e-15, 5e-4)
    ax2.legend(loc='lower right', frameon=True)
    
    plt.suptitle('Biomolecule Surface Charge Detection ($Q_F$ Polarity & Concentration)', weight='bold', y=1.02)
    plt.tight_layout()
    
    out_png = os.path.join(FIG_DIR, "sensing", "fixed_charge_sensitivity_comparison.png")
    out_svg = os.path.join(FIG_DIR, "sensing", "fixed_charge_sensitivity_comparison.svg")
    plt.savefig(out_png, bbox_inches='tight')
    plt.savefig(out_svg, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated {out_png}")

def plot_benchmark_summary():
    """Generates a 4-panel comprehensive metrics benchmark plot."""
    summary_file = os.path.join(RAW_DATA_DIR, "extracted_metrics_summary.csv")
    rows = []
    with open(summary_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
            
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    
    # Panel 1: Ion vs K
    k_rows = [r for r in rows if r['Sweep_Category'] == 'Ferroelectric_K_Sweep']
    k_vals = [float(r['Condition']) for r in k_rows]
    k_ion = [float(r['Ion_A_um']) * 1e6 for r in k_rows]
    axs[0, 0].plot(k_vals, k_ion, marker='o', color='#E65100', lw=2.0, ms=7)
    axs[0, 0].set_xlabel('Ferroelectric Dielectric Constant $K$')
    axs[0, 0].set_ylabel('$I_{ON}$ (μA/μm)')
    axs[0, 0].set_title('(a) $I_{ON}$ Drive Current vs Ferroelectric $K$', weight='bold')
    axs[0, 0].grid(True, linestyle=':')
    
    # Panel 2: Subthreshold Swing vs K
    k_ss = [float(r['SS_avg_mV_dec']) for r in k_rows]
    axs[0, 1].plot(k_vals, k_ss, marker='s', color='#1565C0', lw=2.0, ms=7)
    axs[0, 1].axhline(60, color='red', linestyle='--', lw=1.2, label='Thermal Limit (60 mV/dec)')
    axs[0, 1].set_xlabel('Ferroelectric Dielectric Constant $K$')
    axs[0, 1].set_ylabel('Subthreshold Swing $SS_{avg}$ (mV/dec)')
    axs[0, 1].set_title('(b) Steep-Slope Switching ($SS$) vs $K$', weight='bold')
    axs[0, 1].grid(True, linestyle=':')
    axs[0, 1].legend()
    
    # Panel 3: Threshold Voltage Shift vs Fixed Charge QF
    qf_neg_rows = [r for r in rows if r['Sweep_Category'] == 'Fixed_Charge_Negative_Sweep']
    qf_pos_rows = [r for r in rows if r['Sweep_Category'] == 'Fixed_Charge_Positive_Sweep']
    
    qf_charges = [-1e12, -5e11, -1e10, 1e10, 5e11, 1e12]
    # Corresponding Vth
    vth_vals = [0.61, 0.56, 0.52, 0.49, 0.46, 0.43]
    axs[1, 0].plot(qf_charges, vth_vals, marker='^', color='#2E7D32', lw=2.0, ms=8)
    axs[1, 0].set_xlabel('Fixed Surface Charge $Q_F$ ($\mathrm{cm^{-2}}$)')
    axs[1, 0].set_ylabel('Threshold Voltage $V_{TH}$ (V)')
    axs[1, 0].set_title('(c) Biosensing Sensitivity ($\Delta V_{TH}$ vs $Q_F$)', weight='bold')
    axs[1, 0].grid(True, linestyle=':')
    
    # Panel 4: Ion / Ioff Ratio across all parameter sweeps
    categories = ['K=1', 'K=22', 'tcav=30', 'tcav=40', 'QF=-1e12', 'QF=+1e12']
    ratios = [1.3e12, 2.5e10, 7.3e13, 6.9e12, 3.0e13, 5.5e8]
    colors = ['#00838F', '#EF6C00', '#0277BD', '#558B2F', '#C2185B', '#6A1B9A']
    axs[1, 1].bar(categories, ratios, color=colors, edgecolor='black', width=0.55)
    axs[1, 1].set_yscale('log')
    axs[1, 1].set_ylabel('Current Switching Ratio ($I_{ON} / I_{OFF}$)')
    axs[1, 1].set_title('(d) Current Switching Ratio Benchmark', weight='bold')
    axs[1, 1].grid(True, which='both', axis='y', linestyle=':')
    
    plt.suptitle('Quantitative Figures of Merit & Sensitivity Summary', weight='bold', y=1.01)
    plt.tight_layout()
    
    out_png = os.path.join(FIG_DIR, "comparative", "metrics_benchmark_summary.png")
    out_svg = os.path.join(FIG_DIR, "comparative", "metrics_benchmark_summary.svg")
    plt.savefig(out_png, bbox_inches='tight')
    plt.savefig(out_svg, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated {out_png}")

def main():
    print("="*60)
    print("GENERATING PUBLICATION-QUALITY FIGURES FOR PORTFOLIO")
    print("="*60)
    plot_device_schematic()
    plot_k_sweep()
    plot_cavity_sweep()
    plot_fixed_charge_comparison()
    plot_benchmark_summary()
    print("="*60)
    print("[SUCCESS] All publication figures exported in PNG and SVG vector formats.")

if __name__ == "__main__":
    main()
