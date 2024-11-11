"""
Script to perform linear regression (and plot the line) on RMSE (accuracy/error) vs True Distance
Predict what the RMSE is based on the True Distance
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Compute RMSE 
def rmse(true_distance, estimated_distances):
    return np.sqrt(mean_squared_error([true_distance]*len(estimated_distances), estimated_distances))


def process_files(input_directory):
    rmse_data = []

    for filename in os.listdir(input_directory):
        if filename.startswith("D_cm_") and filename.endswith(".txt"):
            # Extract true distance from filename (e.g., "D_cm_1m.txt")
            true_distance_str = filename.replace("D_cm_", "").replace("m.txt", "")
            true_distance = float(true_distance_str)*100
            
            file_path = os.path.join(input_directory, filename) 
            estimated_distances = np.loadtxt(file_path)
            
            # Store the true distance and its corresponding RMSE
            rmse_data.append((true_distance, rmse(true_distance, estimated_distances)))      
            
    
    return pd.DataFrame(rmse_data, columns=["True Distance", "RMSE"])

def model_accuracy_vs_distance(input_directory):
   df = process_files(input_directory)
   X = df["True Distance"].values.reshape(-1, 1)
   y = df["RMSE"].values

   # Fit a linear regression model
   model = LinearRegression()
   model.fit(X, y)

   # Predict the accuracy across distances
   predicted_accuracy = model.predict(X)

   # R^2
   r_squared = r2_score(y, predicted_accuracy)

   # Plot the results
   plt.scatter(df["True Distance"], df["RMSE"], label="RMSE")
   plt.plot(df["True Distance"], predicted_accuracy, color="red", label="Fitted Model")
   plt.xlabel("True Distance (cm)")
   plt.ylabel("RMSE")
   plt.title("RMSE vs True Distance (Indoors)")
   plt.legend()

   # Add text box with R^2 and RMSE
   stats_text = f'R²: {r_squared:.4f}'
   plt.gca().text(0.05, 0.95, stats_text, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

   plt.savefig("indoor_lr_rmse_vs_dist.png")

if __name__ == "__main__":
    # input_directory = "logs/10_25_2024/D_cm/"
    input_directory = "logs/10_17_2024/D_cm/"
    model_accuracy_vs_distance(input_directory)

