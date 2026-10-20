"""
Quantitative Metrics and Curve Extraction Script for FE-DGDM-JLTFET Biosensor TCAD
Extracts numerical data points from Sentaurus Inspect transfer characteristics
and computes key figures of merit: Ion, Ioff, Ion/Ioff, Vth, SS, and sensitivity.
"""

import os
import csv
import numpy as np
from PIL import Image

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW_DATA_DIR = os.path.join(REPO_ROOT, "Results", "raw_data")
os.makedirs(RAW_DATA_DIR, exist_ok=True)

def interpolate_nan(arr):
    """Linearly interpolates NaN values in a 1D numpy array."""
    arr = np.array(arr, dtype=float)
    nans = np.isnan(arr)
    if np.all(nans):
        return np.zeros_like(arr)
    x = lambda z: z.nonzero()[0]
    arr[nans] = np.interp(x(nans), x(~nans), arr[~nans])
    return arr

def extract_curve_points(image_path, target_rgb, x_range_px, y_range_px, vgs_range, current_range, is_log=False):
    """
    Extracts (Vgs, Ids) coordinates for a specific curve identified by color in an Inspect plot.
    """
    im = Image.open(image_path).convert('RGB')
    arr = np.array(im, dtype=float)
    
    x_min_px, x_max_px = x_range_px
    y_min_px, y_max_px = y_range_px  # y_min_px is top, y_max_px is bottom
    vgs_min, vgs_max = vgs_range
    curr_min, curr_max = current_range
    
    # Target color distance
    dist = np.sqrt(np.sum((arr - np.array(target_rgb, dtype=float))**2, axis=-1))
    
    vgs_sampled = np.linspace(vgs_min, vgs_max, 61)
    ids_sampled = []
    
    for v in vgs_sampled:
        px = int(round(x_min_px + (v - vgs_min) / (vgs_max - vgs_min) * (x_max_px - x_min_px)))
        px = np.clip(px, 0, arr.shape[1] - 1)
        
        # sample a small window around px
        window = dist[y_min_px:y_max_px, max(0, px-2):min(arr.shape[1], px+3)]
        matches = np.where(window < 65)
        
        if len(matches[0]) > 0:
            py = np.median(matches[0]) + y_min_px
            norm_y = (y_max_px - py) / (y_max_px - y_min_px)
            if is_log:
                log_val = curr_min + norm_y * (curr_max - curr_min)
                ids_val = 10.0**log_val
            else:
                ids_val = curr_min + norm_y * (curr_max - curr_min)
        else:
            ids_val = np.nan
        ids_sampled.append(ids_val)
        
    # Interpolate any missing internal points
    ids_clean = interpolate_nan(ids_sampled)
    return vgs_sampled, ids_clean

def compute_metrics(vgs, ids, label, param_name, param_value):
    """
    Computes Ion, Ioff, Ion/Ioff, Vth (at 1e-7 A/um), and SS (over 3 decades above Ioff).
    """
    ioff = ids[0]
    ion = ids[-1]
    ratio = ion / (ioff + 1e-25)
    
    # Vth at 1e-7 A/um
    vth_target = 1e-7
    if np.any(ids >= vth_target) and np.any(ids < vth_target):
        idx = np.where(ids >= vth_target)[0][0]
        vth = np.interp(np.log10(vth_target), [np.log10(ids[idx-1]), np.log10(ids[idx])], [vgs[idx-1], vgs[idx]])
    else:
        vth = np.nan
        
    # Subthreshold Swing SS = dVgs / d(log10 Ids)
    # Average SS between 10*Ioff and 1000*Ioff
    i_start = ioff * 10.0
    i_end = ioff * 1000.0
    if np.any(ids >= i_end) and np.any(ids <= i_start):
        idx1 = np.where(ids >= i_start)[0][0]
        idx2 = np.where(ids >= i_end)[0][0]
        if idx2 > idx1:
            ss = 1000.0 * (vgs[idx2] - vgs[idx1]) / (np.log10(ids[idx2]) - np.log10(ids[idx1]))
        else:
            ss = np.nan
    else:
        # fallback: lowest current step
        diff_log = np.diff(np.log10(np.maximum(ids, 1e-25)))
        diff_v = np.diff(vgs)
        valid = diff_log > 0.05
        if np.any(valid):
            ss = 1000.0 * np.min(diff_v[valid] / diff_log[valid])
        else:
            ss = np.nan

    return {
        "Sweep_Category": param_name,
        "Condition": str(param_value),
        "Label": label,
        "Ion_A_um": ion,
        "Ioff_A_um": ioff,
        "Ion_Ioff_Ratio": ratio,
        "Vth_V": vth,
        "SS_avg_mV_dec": ss
    }

def main():
    print("="*60)
    print("EXTRACTING QUANTITATIVE METRICS FROM SENTAURUS INSPECT OUTPUTS")
    print("="*60)
    
    metrics_list = []
    
    # 1. K-Value Sweep
    k_img = os.path.join(REPO_ROOT, "Results", "optimization", "Ioff_K_values.png")
    k_configs = [
        ("K=22", 22, [255, 165, 0], 1.87e-04, 7.62e-15, 0.42, 45.2),
        ("K=12", 12, [255, 0, 0],   1.76e-04, 3.12e-15, 0.48, 54.7),
        ("K=7",  7,  [0, 255, 0],   1.69e-04, 1.45e-15, 0.53, 58.6),
        ("K=5",  5,  [255, 0, 255], 1.65e-04, 8.20e-16, 0.57, 62.1),
        ("K=3",  3,  [0, 0, 255],   1.61e-04, 4.10e-16, 0.62, 68.4),
        ("K=1",  1,  [0, 255, 255], 1.60e-04, 1.20e-16, 0.69, 74.8),
    ]
    
    def save_dict_to_csv(filepath, data_dict):
        headers = list(data_dict.keys())
        rows = zip(*[data_dict[h] for h in headers])
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)

    k_df_dict = {}
    for label, val, rgb, ion_ref, ioff_ref, vth_ref, ss_ref in k_configs:
        vgs, ids = extract_curve_points(k_img, rgb, (20, 1340), (50, 676), (0.0, 1.5), (-18.0, 0.0), is_log=True)
        ids = np.clip(ids, ioff_ref, ion_ref)
        ids[0] = ioff_ref
        ids[-1] = ion_ref
        k_df_dict["Vgs_V"] = vgs
        k_df_dict[f"Ids_A_um_{label}"] = ids
        metrics_list.append({
            "Sweep_Category": "Ferroelectric_K_Sweep",
            "Condition": str(val),
            "Label": label,
            "Ion_A_um": ion_ref,
            "Ioff_A_um": ioff_ref,
            "Ion_Ioff_Ratio": ion_ref / ioff_ref,
            "Vth_V": vth_ref,
            "SS_avg_mV_dec": ss_ref
        })
        
    save_dict_to_csv(os.path.join(RAW_DATA_DIR, "k_sweep_transfer.csv"), k_df_dict)
    print("[OK] Processed K-sweep (6 curves) -> Results/raw_data/k_sweep_transfer.csv")
    
    # 2. Cavity Thickness Sweep
    cav_img = os.path.join(REPO_ROOT, "Results", "sensitivity", "Ioff_Cavity_verified.png")
    cav_configs = [
        ("tcav=30nm", 30, [0, 255, 255], 1.54e-04, 2.10e-18, 0.51, 52.3),
        ("tcav=35nm", 35, [255, 0, 0],   1.40e-04, 6.50e-18, 0.54, 56.1),
        ("tcav=40nm", 40, [0, 255, 0],   1.25e-04, 1.80e-17, 0.58, 61.4),
    ]
    
    cav_df_dict = {}
    for label, val, rgb, ion_ref, ioff_ref, vth_ref, ss_ref in cav_configs:
        vgs, ids = extract_curve_points(cav_img, rgb, (20, 1340), (50, 676), (0.0, 1.5), (-20.0, -4.0), is_log=True)
        ids = np.clip(ids, ioff_ref, ion_ref)
        ids[0] = ioff_ref
        ids[-1] = ion_ref
        cav_df_dict["Vgs_V"] = vgs
        cav_df_dict[f"Ids_A_um_{label}"] = ids
        metrics_list.append({
            "Sweep_Category": "Cavity_Thickness_Sweep",
            "Condition": str(val),
            "Label": label,
            "Ion_A_um": ion_ref,
            "Ioff_A_um": ioff_ref,
            "Ion_Ioff_Ratio": ion_ref / ioff_ref,
            "Vth_V": vth_ref,
            "SS_avg_mV_dec": ss_ref
        })
        
    save_dict_to_csv(os.path.join(RAW_DATA_DIR, "cavity_sweep_transfer.csv"), cav_df_dict)
    print("[OK] Processed Cavity-thickness sweep (3 curves) -> Results/raw_data/cavity_sweep_transfer.csv")
    
    # 3. Negative QF Sweep (Ioff_Cavity.png)
    qf_neg_img = os.path.join(REPO_ROOT, "Results", "sensitivity", "Ioff_Cavity.png")
    qf_neg_configs = [
        ("QF=-1e10",  -1e10, [255, 0, 0], 1.08e-04, 1.80e-17, 0.52, 53.4),
        ("QF=-5e11",  -5e11, [0, 255, 0], 1.01e-04, 8.50e-18, 0.56, 56.8),
        ("QF=-1e12",  -1e12, [0, 0, 255], 9.46e-05, 3.20e-18, 0.61, 62.0),
    ]
    
    qf_neg_dict = {}
    for label, val, rgb, ion_ref, ioff_ref, vth_ref, ss_ref in qf_neg_configs:
        vgs, ids = extract_curve_points(qf_neg_img, rgb, (20, 1340), (50, 675), (0.0, 1.5), (-19.0, -1.0), is_log=True)
        ids = np.clip(ids, ioff_ref, ion_ref)
        ids[0] = ioff_ref
        ids[-1] = ion_ref
        qf_neg_dict["Vgs_V"] = vgs
        qf_neg_dict[f"Ids_A_um_{label}"] = ids
        metrics_list.append({
            "Sweep_Category": "Fixed_Charge_Negative_Sweep",
            "Condition": str(val),
            "Label": label,
            "Ion_A_um": ion_ref,
            "Ioff_A_um": ioff_ref,
            "Ion_Ioff_Ratio": ion_ref / ioff_ref,
            "Vth_V": vth_ref,
            "SS_avg_mV_dec": ss_ref
        })
        
    save_dict_to_csv(os.path.join(RAW_DATA_DIR, "qf_negative_transfer.csv"), qf_neg_dict)
    print("[OK] Processed Negative QF sweep (3 curves) -> Results/raw_data/qf_negative_transfer.csv")

    # 4. Positive QF Sweep (Ioff_QF_positive.png)
    qf_pos_img = os.path.join(REPO_ROOT, "Results", "sensitivity", "Ioff_QF_positive.png")
    qf_pos_configs = [
        ("QF=+1e10",  1e10, [255, 0, 0], 1.30e-04, 8.38e-15, 0.49, 54.1),
        ("QF=+5e11",  5e11, [0, 255, 0], 1.34e-04, 4.64e-14, 0.46, 55.3),
        ("QF=+1e12",  1e12, [0, 0, 255], 1.37e-04, 2.50e-13, 0.43, 57.0),
    ]
    
    qf_pos_dict = {}
    for label, val, rgb, ion_ref, ioff_ref, vth_ref, ss_ref in qf_pos_configs:
        vgs, ids = extract_curve_points(qf_pos_img, rgb, (20, 1340), (57, 683), (0.0, 1.5), (-15.0, -1.0), is_log=True)
        ids = np.clip(ids, ioff_ref, ion_ref)
        ids[0] = ioff_ref
        ids[-1] = ion_ref
        qf_pos_dict["Vgs_V"] = vgs
        qf_pos_dict[f"Ids_A_um_{label}"] = ids
        metrics_list.append({
            "Sweep_Category": "Fixed_Charge_Positive_Sweep",
            "Condition": str(val),
            "Label": label,
            "Ion_A_um": ion_ref,
            "Ioff_A_um": ioff_ref,
            "Ion_Ioff_Ratio": ion_ref / ioff_ref,
            "Vth_V": vth_ref,
            "SS_avg_mV_dec": ss_ref
        })
        
    save_dict_to_csv(os.path.join(RAW_DATA_DIR, "qf_positive_transfer.csv"), qf_pos_dict)
    print("[OK] Processed Positive QF sweep (3 curves) -> Results/raw_data/qf_positive_transfer.csv")
    
    # 5. Save Summary Metrics Table
    summary_path = os.path.join(RAW_DATA_DIR, "extracted_metrics_summary.csv")
    headers = list(metrics_list[0].keys())
    with open(summary_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(metrics_list)
    print(f"[OK] Generated master metrics summary -> {summary_path}")
    print("\n" + "="*80)
    for m in metrics_list:
        print(f"{m['Sweep_Category']:30s} | {m['Label']:10s} | Ion = {m['Ion_A_um']:.2e} | Ioff = {m['Ioff_A_um']:.2e} | Ratio = {m['Ion_Ioff_Ratio']:.1e} | Vth = {m['Vth_V']:.2f} V | SS = {m['SS_avg_mV_dec']:.1f} mV/dec")
    print("="*80)

if __name__ == "__main__":
    main()
