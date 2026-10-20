"""
Publication-Quality Scientific Figure Generator for FE-DGDM-JLTFET Biosensor TCAD
Generates high-resolution publication plots (PNG + PDF/SVG) using Matplotlib from extracted TCAD data.
Calibrated to the exact Sentaurus Structure Editor geometry and internship report results.
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
    """
    Generates the exact cross-sectional schematic of the FE-DGDM-JLTFET biosensor
    grounded directly in the Sentaurus Structure Editor (sde_dvs.tcl) coordinates.
    All dimensions in nanometers:
    - Transport length X: 0 to 158 nm
    - Y-axis: -14 to +14 nm
    """
    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    
    # 1. Silicon Channel (T-shaped body)
    # Thin channel: X in [10, 103], Y in [-5, 5] (Tch = 10 nm, As = 1e15 cm^-3)
    ax.add_patch(patches.Rectangle((10, -5), 93, 10, facecolor='#A8DADC', edgecolor='#1D3557', lw=1.2,
                                   label='Channel Body (Si, As: $10^{15}\\ \\mathrm{cm^{-3}}$)'))
    
    # Channel Drain Extension (channelde): X in [103, 148], Y in [-8, 8] (Text = 16 nm, As = 1e15 cm^-3)
    ax.add_patch(patches.Rectangle((103, -8), 45, 16, facecolor='#C5EAEB', edgecolor='#1D3557', lw=1.2,
                                   label='Channel Drain Ext (Si, As: $10^{15}\\ \\mathrm{cm^{-3}}$)'))
    
    # 2. Silicon Source & Source Wings (T-shaped Source)
    # Main source: X in [0, 10], Y in [-11, 11] (Height = 22 nm, As = 1e19 cm^-3)
    ax.add_patch(patches.Rectangle((0, -11), 10, 22, facecolor='#457B9D', edgecolor='#1D3557', lw=1.2,
                                   label='Source (Si, As: $10^{19}\\ \\mathrm{cm^{-3}}$)'))
    # Top source wing (sourcet): X in [10, 55], Y in [-11, -9]
    ax.add_patch(patches.Rectangle((10, -11), 45, 2, facecolor='#457B9D', edgecolor='#1D3557', lw=1.2))
    # Bottom source wing (sourceb): X in [10, 55], Y in [9, 11]
    ax.add_patch(patches.Rectangle((10, 9), 45, 2, facecolor='#457B9D', edgecolor='#1D3557', lw=1.2))
    
    # 3. Silicon Drain: X in [148, 158], Y in [-9, 9] (Height = 18 nm, As = 1e20 cm^-3)
    ax.add_patch(patches.Rectangle((148, -9), 10, 18, facecolor='#1D3557', edgecolor='black', lw=1.2,
                                   label='Drain (Si, As: $10^{20}\\ \\mathrm{cm^{-3}}$)'))
    
    # 4. Interfacial Oxide (SiO2, 1 nm)
    # Top: X in [10, 103], Y in [-6, -5]
    ax.add_patch(patches.Rectangle((10, -6), 93, 1, facecolor='#E0E0E0', edgecolor='#9E9E9E', lw=0.8,
                                   label='Interfacial $\\mathrm{SiO_2}$ ($1\\ \\mathrm{nm}$)'))
    # Bottom: X in [10, 103], Y in [5, 6]
    ax.add_patch(patches.Rectangle((10, 5), 93, 1, facecolor='#E0E0E0', edgecolor='#9E9E9E', lw=0.8))
    
    # 5. Gate Underlap Oxide (SiO2, 3 nm under source wings)
    # Top: X in [10, 45], Y in [-9, -6]
    ax.add_patch(patches.Rectangle((10, -9), 35, 3, facecolor='#CFD8DC', edgecolor='#78909C', lw=0.8,
                                   label='Underlap $\\mathrm{SiO_2}$ ($3\\ \\mathrm{nm}$)'))
    # Bottom: X in [10, 45], Y in [6, 9]
    ax.add_patch(patches.Rectangle((10, 6), 35, 3, facecolor='#CFD8DC', edgecolor='#78909C', lw=0.8))
    
    # 6. Inverted-T Nanocavity (Sensing Region, 3 nm thick, 30 nm length)
    # Top: X in [45, 75], Y in [-9, -6]
    ax.add_patch(patches.Rectangle((45, -9), 30, 3, facecolor='#FFF3E0', edgecolor='#E65100', hatch='///', lw=1.2,
                                   label='Nanocavity ($L_{cav}=30\\ \\mathrm{nm}, t_{cav}=3\\ \\mathrm{nm}$, Analytes)'))
    # Bottom: X in [45, 75], Y in [6, 9]
    ax.add_patch(patches.Rectangle((45, 6), 30, 3, facecolor='#FFF3E0', edgecolor='#E65100', hatch='///', lw=1.2))
    
    # 7. Ferroelectric Gate Stack (Si:HfO2, 3 nm thick, 28 nm length)
    # Top: X in [75, 103], Y in [-9, -6]
    ax.add_patch(patches.Rectangle((75, -9), 28, 3, facecolor='#F39C12', edgecolor='#D35400', lw=1.2,
                                   label='Ferroelectric $\\mathrm{Si:HfO_2}$ ($L_{FE}=28\\ \\mathrm{nm}, t_{FE}=3\\ \\mathrm{nm}$)'))
    # Bottom: X in [75, 103], Y in [6, 9]
    ax.add_patch(patches.Rectangle((75, 6), 28, 3, facecolor='#F39C12', edgecolor='#D35400', lw=1.2))
    
    # 8. Drain Extension Oxide (SiO2, 1 nm)
    ax.add_patch(patches.Rectangle((103, -9), 45, 1, facecolor='#E0E0E0', edgecolor='#9E9E9E', lw=0.8))
    ax.add_patch(patches.Rectangle((103, 8), 45, 1, facecolor='#E0E0E0', edgecolor='#9E9E9E', lw=0.8))
    
    # 9. Gate Electrodes (Top and Bottom Gates, length = 58 nm covering cavity + HfO2)
    # Top Gate: X in [45, 103], Y in [-13, -9]
    ax.add_patch(patches.Rectangle((45, -13), 58, 4, facecolor='#E63946', edgecolor='darkred', lw=1.2,
                                   label='Top / Bottom Gate Electrodes ($L_G=58\\ \\mathrm{nm}$)'))
    # Bottom Gate: X in [45, 103], Y in [9, 13]
    ax.add_patch(patches.Rectangle((45, 9), 58, 4, facecolor='#E63946', edgecolor='darkred', lw=1.2))
    
    # 10. Source & Drain Terminal Contact Plates
    # Source terminal plate: X = -3 to 0, Y in [-11, 11]
    ax.add_patch(patches.Rectangle((-3, -11), 3, 22, facecolor='#2B2D42', edgecolor='black', lw=1.0))
    # Drain terminal plate: X = 158 to 161, Y in [-9, 9]
    ax.add_patch(patches.Rectangle((158, -9), 3, 18, facecolor='#2B2D42', edgecolor='black', lw=1.0))
    
    # Annotations & Region Labels
    ax.text(5, 0, 'Source (S)\n$N_D=10^{19}$', ha='center', va='center', fontsize=8, color='white', weight='bold')
    ax.text(32.5, -10, 'Source Wing', ha='center', va='center', fontsize=6.5, color='white')
    ax.text(32.5, 10, 'Source Wing', ha='center', va='center', fontsize=6.5, color='white')
    ax.text(56.5, 0, 'Silicon Channel ($T_{ch}=10\\ \\mathrm{nm}$)\n$N_D=10^{15}\\ \\mathrm{cm^{-3}}$',
            ha='center', va='center', fontsize=8, color='#1D3557', weight='bold')
    ax.text(125.5, 0, 'Drain Extension ($16\\ \\mathrm{nm}$)\n$N_D=10^{15}\\ \\mathrm{cm^{-3}}$',
            ha='center', va='center', fontsize=7.5, color='#1D3557', weight='bold')
    ax.text(153, 0, 'Drain (D)\n$10^{20}$', ha='center', va='center', fontsize=7.5, color='white', weight='bold')
    
    # Cavity & Ferroelectric Labels
    ax.text(60, -7.5, 'Cavity ($30\\ \\mathrm{nm}$)', ha='center', va='center', fontsize=7, color='#B78103', weight='bold')
    ax.text(60, 7.5, 'Cavity ($30\\ \\mathrm{nm}$)', ha='center', va='center', fontsize=7, color='#B78103', weight='bold')
    ax.text(89, -7.5, '$\\mathrm{Si:HfO_2}$ ($28\\ \\mathrm{nm}$)', ha='center', va='center', fontsize=7, color='#5D3800', weight='bold')
    ax.text(89, 7.5, '$\\mathrm{Si:HfO_2}$ ($28\\ \\mathrm{nm}$)', ha='center', va='center', fontsize=7, color='#5D3800', weight='bold')
    ax.text(74, -11, 'Top Gate ($G_1$)', ha='center', va='center', fontsize=8, color='white', weight='bold')
    ax.text(74, 11, 'Bottom Gate ($G_2$)', ha='center', va='center', fontsize=8, color='white', weight='bold')
    
    # BTBT Tunneling Interface Arrow
    ax.annotate('BTBT Tunnel Junction\n($X = 10\\ \\mathrm{nm}$ Interface)', xy=(10, 0), xytext=(22, -18),
                arrowprops=dict(facecolor='red', edgecolor='darkred', shrink=0.08, width=1.5, headwidth=6),
                color='red', weight='bold', fontsize=8.5, ha='center')
    
    # Total Transport Dimension Bar
    ax.annotate('', xy=(0, -22), xytext=(158, -22),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.4))
    ax.text(79, -24.5, 'Total Device Length = 158 nm (Verified from SDE Script)',
            ha='center', va='center', fontsize=9.5, weight='bold')
    
    # Nanocavity Dimension Callout
    ax.annotate('', xy=(45, 14.5), xytext=(75, 14.5),
                arrowprops=dict(arrowstyle='<->', color='#E65100', lw=1.2))
    ax.text(60, 16.5, '$L_{cav} = 30\\ \\mathrm{nm}$', ha='center', va='center', fontsize=8, color='#E65100', weight='bold')
    
    ax.set_xlim(-12, 175)
    ax.set_ylim(-28, 20)
    ax.axis('off')
    ax.set_title('FE-DGDM-JLTFET Biosensor Architecture (Grounded in Verified SDE Model)',
                 pad=14, weight='bold', fontsize=12)
    
    # Legend placement outside at bottom
    ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.22), ncol=3, frameon=True, fontsize=8)
    
    out_png = os.path.join(FIG_DIR, "device", "device_architecture_schematic.png")
    out_svg = os.path.join(FIG_DIR, "device", "device_architecture_schematic.svg")
    plt.tight_layout()
    plt.savefig(out_png, bbox_inches='tight')
    plt.savefig(out_svg, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated verified {out_png}")

def plot_k_sweep():
    """Generates dual-panel transfer curves for Biomolecule Dielectric Constant K-sweep."""
    data = read_csv_columns(os.path.join(RAW_DATA_DIR, "k_sweep_transfer.csv"))
    vgs = data["Vgs_V"]
    
    k_labels = [
        ("Ids_A_um_K=22", "K = 22 (MDA-MB-231 Breast Cancer)", "#D32F2F"),
        ("Ids_A_um_K=12", "K = 12 (Amino Acids)",              "#E65100"),
        ("Ids_A_um_K=7",  "K = 7 (Zein Protein)",              "#388E3C"),
        ("Ids_A_um_K=5",  "K = 5 (Carbohydrates)",             "#7B1FA2"),
        ("Ids_A_um_K=3",  "K = 3 (Lipids)",                    "#1976D2"),
        ("Ids_A_um_K=1",  "K = 1 (Air Reference)",             "#455A64")
    ]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.4))
    
    # Panel (a): Log scale
    for col, lbl, clr in k_labels:
        ax1.semilogy(vgs, data[col], label=lbl, color=clr, lw=1.8)
    ax1.set_xlabel('Gate-to-Source Voltage $V_{GS}$ (V)')
    ax1.set_ylabel('Drain Current $I_{DS}$ (A/μm)')
    ax1.set_title('(a) Subthreshold Characteristics (Log Scale)', weight='bold')
    ax1.grid(True, which='both', linestyle=':')
    ax1.set_ylim(1e-16, 5e-4)
    ax1.legend(loc='lower right', frameon=True, fontsize=8)
    
    # Panel (b): Linear scale
    for col, lbl, clr in k_labels:
        ax2.plot(vgs, data[col] * 1e6, label=lbl, color=clr, lw=1.8)
    ax2.set_xlabel('Gate-to-Source Voltage $V_{GS}$ (V)')
    ax2.set_ylabel('Drain Current $I_{DS}$ (μA/μm)')
    ax2.set_title('(b) ON-State Drive Current (Linear Scale)', weight='bold')
    ax2.grid(True, linestyle=':')
    ax2.set_ylim(0, 250)
    ax2.legend(loc='upper left', frameon=True, fontsize=8)
    
    plt.suptitle('Biomolecule Dielectric Constant ($K$) Modulation Analysis', weight='bold', y=1.02)
    plt.tight_layout()
    
    out_png = os.path.join(FIG_DIR, "electrical", "k_sweep_transfer_characteristics.png")
    out_svg = os.path.join(FIG_DIR, "electrical", "k_sweep_transfer_characteristics.svg")
    plt.savefig(out_png, bbox_inches='tight')
    plt.savefig(out_svg, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated {out_png}")

def plot_cavity_sweep():
    """Generates dual-panel transfer curves for Cavity-length variation."""
    data = read_csv_columns(os.path.join(RAW_DATA_DIR, "cavity_sweep_transfer.csv"))
    vgs = data["Vgs_V"]
    
    cav_labels = [
        ("Ids_A_um_tcav=30nm", "$L_{cav} = 30$ nm ($I_{ON} = 0.8040$ mA)", "#0288D1"),
        ("Ids_A_um_tcav=35nm", "$L_{cav} = 35$ nm ($I_{ON} = 0.1970$ mA)", "#D32F2F"),
        ("Ids_A_um_tcav=40nm", "$L_{cav} = 40$ nm ($I_{ON} = 0.1908$ mA)", "#388E3C")
    ]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.4))
    
    for col, lbl, clr in cav_labels:
        ax1.semilogy(vgs, data[col], label=lbl, color=clr, lw=2.0)
        ax2.plot(vgs, data[col] * 1e6, label=lbl, color=clr, lw=2.0)
        
    ax1.set_xlabel('Gate-to-Source Voltage $V_{GS}$ (V)')
    ax1.set_ylabel('Drain Current $I_{DS}$ (A/μm)')
    ax1.set_title('(a) Subthreshold Current vs Cavity Length', weight='bold')
    ax1.grid(True, which='both', linestyle=':')
    ax1.set_ylim(1e-19, 1e-3)
    ax1.legend(loc='lower right', frameon=True, fontsize=8.5)
    
    ax2.set_xlabel('Gate-to-Source Voltage $V_{GS}$ (V)')
    ax2.set_ylabel('Drain Current $I_{DS}$ (μA/μm)')
    ax2.set_title('(b) ON-State Current vs Cavity Length', weight='bold')
    ax2.grid(True, linestyle=':')
    ax2.set_ylim(0, 850)
    ax2.legend(loc='upper left', frameon=True, fontsize=8.5)
    
    plt.suptitle('Nanocavity Length Variation ($L_{cav} = 30, 35, 40$ nm)', weight='bold', y=1.02)
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
    ax1.semilogy(vgs, neg_data["Ids_A_um_QF=-1e12"], label="$Q_F = -10^{12}\\ \\mathrm{cm^{-2}}$", color="#D32F2F", lw=2.0)
    ax1.set_xlabel('Gate Voltage $V_{GS}$ (V)')
    ax1.set_ylabel('Drain Current $I_{DS}$ (A/μm)')
    ax1.set_title('(a) Negative Charge: DNA/Acidic Proteins ($Q_F < 0$)', weight='bold')
    ax1.grid(True, which='both', linestyle=':')
    ax1.set_ylim(1e-18, 5e-4)
    ax1.legend(loc='lower right', frameon=True, fontsize=8.5)
    
    # Panel (b): Positive QF (e.g. Basic Proteins / Poly-L-lysine)
    ax2.semilogy(vgs, pos_data["Ids_A_um_QF=+1e10"], label="$Q_F = +10^{10}\\ \\mathrm{cm^{-2}}$", color="#0288D1", lw=2.0)
    ax2.semilogy(vgs, pos_data["Ids_A_um_QF=+5e11"], label="$Q_F = +5\\times 10^{11}\\ \\mathrm{cm^{-2}}$", color="#F57C00", lw=2.0)
    ax2.semilogy(vgs, pos_data["Ids_A_um_QF=+1e12"], label="$Q_F = +10^{12}\\ \\mathrm{cm^{-2}}$", color="#7B1FA2", lw=2.0)
    ax2.set_xlabel('Gate Voltage $V_{GS}$ (V)')
    ax2.set_ylabel('Drain Current $I_{DS}$ (A/μm)')
    ax2.set_title('(b) Positive Charge: Basic Proteins ($Q_F > 0$)', weight='bold')
    ax2.grid(True, which='both', linestyle=':')
    ax2.set_ylim(1e-15, 5e-4)
    ax2.legend(loc='lower right', frameon=True, fontsize=8.5)
    
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
    
    # 1. Cavity length ION vs IOFF
    cav_rows = [r for r in rows if r["Sweep_Category"] == "Cavity_Length"]
    l_cav = [30, 35, 40]
    ion_cav = [float(r["ION_mA"]) for r in cav_rows]
    ion_ioff = [float(r["ION_IOFF_ratio"]) for r in cav_rows]
    
    axs[0, 0].bar([str(x) + " nm" for x in l_cav], ion_cav, color=['#0288D1', '#D32F2F', '#388E3C'], edgecolor='black', width=0.5)
    axs[0, 0].set_ylabel('$I_{ON}$ (mA)')
    axs[0, 0].set_title('(a) $I_{ON}$ vs Cavity Length ($L_{cav}$)', weight='bold')
    axs[0, 0].grid(True, linestyle=':', axis='y')
    for i, v in enumerate(ion_cav):
        axs[0, 0].text(i, v + 0.02, f"{v:.4f} mA", ha='center', fontsize=8.5, weight='bold')
    axs[0, 0].set_ylim(0, 1.0)
    
    # 2. Sensitivity vs K
    k_rows = [r for r in rows if r["Sweep_Category"] == "Dielectric_Constant"]
    k_vals = [1, 3, 5, 7, 12, 22]
    sens = [float(r["Sensitivity_Pct"]) for r in k_rows]
    axs[0, 1].plot(k_vals, sens, marker='s', color='#D32F2F', lw=2.2, markersize=7)
    axs[0, 1].set_xlabel('Dielectric Constant ($K$)')
    axs[0, 1].set_ylabel('Current Sensitivity (%)')
    axs[0, 1].set_title('(b) Current Sensitivity vs Analyte $K$', weight='bold')
    axs[0, 1].grid(True, linestyle=':')
    for x, y in zip(k_vals[1:], sens[1:]):
        axs[0, 1].annotate(f"{y:.2f}%", (x, y), textcoords="offset points", xytext=(0, 7), ha='center', fontsize=8.5)
    axs[0, 1].set_ylim(-1, 22)
    
    # 3. Vth shift with K
    vth_k = [float(r["Vth_V"]) for r in k_rows if r["Vth_V"] != "N/A"]
    k_vth_vals = [3, 5, 7, 12, 22]
    axs[1, 0].plot(k_vth_vals, vth_k, marker='o', color='#1976D2', lw=2.0, markersize=7)
    axs[1, 0].set_xlabel('Dielectric Constant ($K$)')
    axs[1, 0].set_ylabel('Threshold Voltage $V_{th}$ (V)')
    axs[1, 0].set_title('(c) $V_{th}$ Modulation with Biomolecule $K$', weight='bold')
    axs[1, 0].grid(True, linestyle=':')
    for x, y in zip(k_vth_vals, vth_k):
        axs[1, 0].annotate(f"{y:.4f}V", (x, y), textcoords="offset points", xytext=(0, 6), ha='center', fontsize=8)
    axs[1, 0].set_ylim(0.38, 0.43)
    
    # 4. Transconductance gm vs K
    gm_k = [float(r["gm_mS"]) for r in k_rows if r["gm_mS"] != "N/A"]
    k_gm_vals = [5, 7, 12, 22]
    axs[1, 1].plot(k_gm_vals, gm_k, marker='^', color='#388E3C', lw=2.0, markersize=7)
    axs[1, 1].set_xlabel('Dielectric Constant ($K$)')
    axs[1, 1].set_ylabel('Transconductance $g_m$ (mS)')
    axs[1, 1].set_title('(d) Transconductance Gain $g_m$ vs $K$', weight='bold')
    axs[1, 1].grid(True, linestyle=':')
    for x, y in zip(k_gm_vals, gm_k):
        axs[1, 1].annotate(f"{y:.3f}", (x, y), textcoords="offset points", xytext=(0, 6), ha='center', fontsize=8)
    axs[1, 1].set_ylim(0.35, 0.72)
    
    plt.suptitle('FE-DGDM-JLTFET Performance Benchmark Summary', weight='bold', y=1.01)
    plt.tight_layout()
    
    out_png = os.path.join(FIG_DIR, "comparative", "metrics_benchmark_summary.png")
    out_svg = os.path.join(FIG_DIR, "comparative", "metrics_benchmark_summary.svg")
    plt.savefig(out_png, bbox_inches='tight')
    plt.savefig(out_svg, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated {out_png}")

if __name__ == '__main__':
    print("Generating publication figures...")
    plot_device_schematic()
    plot_k_sweep()
    plot_cavity_sweep()
    plot_fixed_charge_comparison()
    plot_benchmark_summary()
    print("All figures successfully regenerated.")
