import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def process_files(input_directory):
    accuracy_data = []

    for filename in os.listdir(input_directory):
        if filename.startswith("D_cm_") and filename.endswith(".txt"):
            # Extract true distance from filename (e.g., "D_cm_1m.txt")
            true_distance_str = filename.replace("D_cm_", "").replace("m.txt", "")
            true_distance = float(true_distance_str)*100
            
            file_path = os.path.join(input_directory, filename)
            
            estimated_distances = np.loadtxt(file_path)
            
            average = np.mean(estimated_distances)
            
            # Store the true distance and its corresponding RMSE
            accuracy_data.append((true_distance, average))
    
    return pd.DataFrame(accuracy_data, columns=["True Distance", "Estimated Distance"])

def model_accuracy_vs_distance(input_directory):
   df = process_files(input_directory)
   X = df["True Distance"].values.reshape(-1, 1)
   y = df["Estimated Distance"].values

   # Fit a linear regression model for simplicity
   model = LinearRegression()
   model.fit(X, y)

   # Predict the accuracy across distances
   predicted_accuracy = model.predict(X)

   # R^2
   r_squared = r2_score(y, predicted_accuracy)

   # Plot the results
   plt.scatter(df["True Distance"], df["Estimated Distance"], label="Average of Distance Estimations")
   plt.plot(df["True Distance"], predicted_accuracy, color="red", label="Fitted Model")
   plt.xlabel("True Distance (m)")
   plt.ylabel("Estimated Distance (m)")
   plt.title("Estimated Distance vs True Distance (Outdoors)")
   plt.legend()

   # Add text box with R^2 and RMSE
   stats_text = f'R²: {r_squared:.4f}'
   plt.gca().text(0.05, 0.95, stats_text, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

   plt.savefig("outdoor_lr_estimated_vs_true.png")

if __name__ == "__main__":
    input_directory = "logs/10_25_2024/D_cm/"
    model_accuracy_vs_distance(input_directory)

