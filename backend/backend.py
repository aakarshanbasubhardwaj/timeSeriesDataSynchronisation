import os
import pandas as pd
import numpy as np
from tqdm import tqdm
import csv
from dtaidistance import dtw
from concurrent.futures import ProcessPoolExecutor, as_completed
import sys

def calculateMagnitude(inputFile): 
    df = pd.read_csv(inputFile, low_memory=False)
    mag_df = pd.DataFrame()
    
    x = df.iloc[:, 0].astype(float)
    y = df.iloc[:, 1].astype(float)
    z = df.iloc[:, 2].astype(float)

    magnitude = np.sqrt(x**2 + y**2 + z**2)
    mag_df['magnitude'] = magnitude
    filename = os.path.basename(inputFile)
    output_filename = filename.replace(".csv", "_magnitude.csv")
    mag_df.to_csv(output_filename, index=False)
    print(f"Saved magnitude files", file=sys.stderr)
    return output_filename        

def compute_variance(input_csv, window_size=50):
    print("computing varaince", file=sys.stderr)
    df = pd.read_csv(input_csv, low_memory=False)

    n = len(df)
    
    if n < window_size:
        raise ValueError("Window size must be less than or equal to length of signal.")

    var_data = {'index': np.arange(window_size // 2, n - window_size // 2 +1)}

    signal = df.to_numpy(dtype=float)

    cumsum = np.cumsum(np.insert(signal, 0, 0))
    cumsum_sq = np.cumsum(np.insert(signal**2, 0, 0))

    sum_x = cumsum[window_size:] - cumsum[:-window_size]
    sum_x2 = cumsum_sq[window_size:] - cumsum_sq[:-window_size]

    mean_x = sum_x / window_size
    mean_x2 = sum_x2 / window_size

    variance = mean_x2 - mean_x**2

    var_data[f'{input_csv.replace('_magnitude.csv', '_variance')}'] = variance

    var_df = pd.DataFrame(var_data)
    var_df.to_csv(input_csv.replace('_magnitude', '_variance'), index=False)
    return var_df

def label_rest_motion(magnitudeFile, var_df, threshold=0.002):
    var_col = magnitudeFile.replace('_magnitude.csv', '_variance')
    
    var_indices = var_df['index'].values
    variances = var_df[var_col].values

    mag_df = pd.read_csv(magnitudeFile)
    n = len(mag_df)

    positions = np.searchsorted(var_indices, np.arange(n))

    left_indices = np.clip(positions - 1, 0, len(var_indices) - 1)
    right_indices = np.clip(positions, 0, len(var_indices) - 1)

    left_distances = np.abs(var_indices[left_indices] - np.arange(n))
    right_distances = np.abs(var_indices[right_indices] - np.arange(n))

    closest_var_idx = np.where(left_distances <= right_distances, left_indices, right_indices)

    labels = np.where(variances[closest_var_idx] > threshold, 'motion', 'rest')

    return labels.tolist()

def get_balanced_windows(labels, window_size=200):
    print("computing balanced window", file=sys.stderr)
    windows = []
    n = len(labels)

    if n < window_size:
        return windows

    window_labels = labels[:window_size]
    rest_count = window_labels.count('rest')
    motion_count = window_size - rest_count

    i = 0
    while i + window_size <= n:
        if abs(rest_count - motion_count) <= window_size * 0.1:
            windows.append((i, i + window_size))
            i += window_size
            if i + window_size <= n:
                window_labels = labels[i:i+window_size]
                rest_count = window_labels.count('rest')
                motion_count = window_size - rest_count
        else:
            if i + window_size == n:
                break

            left_label = labels[i]
            right_label = labels[i + window_size]

            if left_label == 'rest':
                rest_count -= 1
            else:
                motion_count -= 1

            if right_label == 'rest':
                rest_count += 1
            else:
                motion_count += 1

            i += 1

    return windows


def process_single_window(args):

    reference_magnitudes_values, target_search_segment, window_indices, idx, target_search_start = args
    win_start, win_end = window_indices

    min_distance = float('inf')
    best_start_idx = None

    window = reference_magnitudes_values[win_start:win_end]    
    window_size = len(window)

    for start_idx in range(len(target_search_segment) - window_size + 1):
        candidate = target_search_segment[start_idx:start_idx + window_size]
        distance = dtw.distance_fast(window, candidate)
        
        if distance < min_distance:
            min_distance = distance
            best_start_idx = start_idx

    if best_start_idx is None:
        print(f"No DTW match found for window {win_start}-{win_end}", file=sys.stderr)
        return None
    
    target_start = target_search_start + best_start_idx
    target_end = target_start + window_size

    return [
        win_start,
        win_end,
        target_start,
        target_end,
        min_distance
    ]

def run_dtw_matching_parallel(reference_magnitudes, target_magnitudes_values, balanced_windows, reference_labels, target_labels, max_workers=4):

    results_csv = "dtw_results.csv"

    if not os.path.exists(results_csv):
        with open(results_csv, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                "Ref Start",
                "Ref End",
                "Target Start",
                "Target End",
                "DTW Distance"
            ])

    args_list = []
    reference_magnitudes_values = pd.read_csv(reference_magnitudes)['magnitude'].values
    target_magnitudes_values = pd.read_csv(target_magnitudes_values)['magnitude'].values

    for idx, (win_start, win_end) in enumerate(balanced_windows):
        target_search_start = max(win_start - 400, 0)
        target_search_end = min(win_start - 400 + 1000, len(target_magnitudes_values))
        target_search_segment = target_magnitudes_values[target_search_start:target_search_end]

        args = (
            reference_magnitudes_values,
            target_search_segment,
            (win_start, win_end),
            idx,
            target_search_start
        )
        args_list.append(args)

    results = []

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_single_window, args) for args in args_list]
        for f in tqdm(as_completed(futures), total=len(futures), desc="Processing windows"):
            try:
                res = f.result()
                if res:
                    results.append(res)
            except Exception as e:
                print(f"Task failed: {e}", file=sys.stderr)

    with open(results_csv, mode='a', newline='') as f:
        writer = csv.writer(f)
        for res in results:
            writer.writerow(res)

def getMedianOffset(resultsCSV):
    df = pd.read_csv(resultsCSV)

    filtered = df[df['DTW Distance'] < 10].copy()

    filtered['Offset'] = filtered['Target Start'] - filtered['Ref Start']

    median_offset = filtered['Offset'].median()

    if pd.isna(median_offset):
        return 0

    return round(median_offset)

def make_synced_filename(file_path):
    base = os.path.basename(file_path)
    ext = os.path.splitext(file_path)[1]
    return f"{base}_sync{ext}"

def trim_csv(file_path, medianOffset, output_path):
    df = pd.read_csv(file_path)
    trimmed_df = df.iloc[medianOffset:] if medianOffset > 0 else df
    trimmed_df.to_csv(output_path, index=False)

def clearFiles():
    for filename in os.listdir('.'):
        if filename.endswith('.csv'):
            try:
                os.remove(filename)
                print(f"Deleted {filename}", file=sys.stderr)
            except Exception as e:
                print(f"Error deleting {filename}: {e}", file=sys.stderr)

def sync(file1, file2):

    reference_file = file1
    target_file = file2 

    reference_magnitudes= calculateMagnitude(reference_file)
    target_magnitudes = calculateMagnitude(target_file)

    reference_var_df = compute_variance(reference_magnitudes, window_size=50)
    target_var_df = compute_variance(target_magnitudes, window_size=50)

    reference_labels = label_rest_motion(reference_magnitudes, reference_var_df, threshold=0.002)
    target_labels = label_rest_motion(target_magnitudes, target_var_df, threshold=0.002)

    balanced_windows = get_balanced_windows(reference_labels, window_size=200)

    run_dtw_matching_parallel(reference_magnitudes, target_magnitudes, balanced_windows, reference_labels, target_labels)

    medianOffset = getMedianOffset("dtw_results.csv")

    clearFiles()

    return medianOffset

if __name__ == "__main__":

    file1, file2 = sys.argv[1], sys.argv[2]

    medianOffset1 = sync(file1, file2)
    medianOffset2 = sync(file2, file1)
    finalOffset = 0

    if medianOffset1 > medianOffset2 :
        finalOffset = medianOffset1
    else :
        finalOffset = medianOffset2

    print(finalOffset)

    sync_dir = "sync"
    os.makedirs(sync_dir, exist_ok=True)

    file1_out = os.path.join(sync_dir, make_synced_filename(file1))
    file2_out = os.path.join(sync_dir, make_synced_filename(file2))

    trim_csv(file1, finalOffset, file1_out)
    trim_csv(file2, finalOffset, file2_out)