import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def process_files(input_directory):
    error_data = []

    for filename in os.listdir(input_directory):
        if filename.startswith("D_cm_") and filename.endswith(".txt"):
            # Extract true distance from filename (e.g., "D_cm_1m.txt.txt")
            true_distance_str = filename.replace("D_cm_", "").replace("m.txt", "")
            true_distance = float(true_distance_str)*100
            
            file_path = os.path.join(input_directory, filename)
            
            estimated_distances = np.loadtxt(file_path)

            error_data.append(np.abs(estimated_distances-true_distance))
            
    
    return np.concatenate(error_data)

def error_hist(input_directory):
    errors = process_files(input_directory)
    
    mean_error = np.mean(errors)
    median_error = np.median(errors)
    std_dev_error = np.std(errors)

    plt.hist(errors, bins='auto', edgecolor='black')
    plt.title('Histogram of Absolute Errors (Outdoors)')
    plt.xlabel('Absolute Error (cm)')
    plt.ylabel('Frequency')

    stats_text = (f"Mean: {mean_error:.2f} cm\n"
                  f"Median: {median_error:.2f} cm\n"
                  f"STDEV: {std_dev_error:.2f} cm")

    plt.gca().text(0.95, 0.95, stats_text, transform=plt.gca().transAxes,
               fontsize=12, verticalalignment='top', horizontalalignment='right',
               bbox=dict(facecolor='white', alpha=0.8))

    plt.savefig('outdoor_hist.png')


if __name__ == "__main__":
    # input_directory = "logs/10_17_2024/D_cm/"
    input_directory = "logs/10_25_2024/D_cm/"
    error_hist(input_directory)

