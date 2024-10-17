import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def calculate_rmse(true_distance, estimated_distances):
    # Calculate Root Mean Squared Error (RMSE)
    rmse = np.sqrt(mean_squared_error([true_distance] * len(estimated_distances), estimated_distances))
    return rmse

def process_files(input_directory):
    accuracy_data = []

    for filename in os.listdir(input_directory):
        if filename.startswith("D_cm_") and filename.endswith(".txt.txt"):
            # Extract true distance from filename (e.g., "D_cm_1m.txt.txt")
            true_distance_str = filename.replace("D_cm_", "").replace("m.txt.txt", "")
            true_distance = float(true_distance_str)
            
            file_path = os.path.join(input_directory, filename)
            
            estimated_distances = np.loadtxt(file_path)
            
            rmse = calculate_rmse(true_distance, estimated_distances)
            
            # Store the true distance and its corresponding RMSE
            accuracy_data.append((true_distance, rmse))
    
    return pd.DataFrame(accuracy_data, columns=["True Distance", "RMSE"])

def model_accuracy_vs_distance(input_directory):
   df = process_files(input_directory)
   X = df["True Distance"].values.reshape(-1, 1)
   y = df["RMSE"].values

   # Fit a linear regression model for simplicity
   model = LinearRegression()
   model.fit(X, y)

   # Predict the accuracy across distances
   predicted_accuracy = model.predict(X)

   # Plot the results
   plt.scatter(df["True Distance"], df["RMSE"], label="Observed RMSE")
   plt.plot(df["True Distance"], predicted_accuracy, color="red", label="Fitted Model")
   plt.xlabel("True Distance (m)")
   plt.ylabel("Accuracy (RMSE)")
   plt.title("Accuracy (RMSE) vs True Distance")
   plt.legend()

   plt.savefig("accuracy_vs_distance.png")

if __name__ == "__main__":
    input_directory = "logs/10_17_2024/D_cm/"
    model_accuracy_vs_distance(input_directory)

