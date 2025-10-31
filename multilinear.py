from google.colab import files
uploaded = files.upload()  # upload dataset

import numpy as np
import pandas as pd

df = pd.read_csv("multiple_linear_regression_dataset.csv")

# independent (x1, x2) and dependent (y)
x1 = df['age'].values
x2 = df['experience'].values
y = df['income'].values

# summations
sum_x1 = np.sum(x1)
sum_x2 = np.sum(x2)
sum_y = np.sum(y)
sum_x1y = np.sum(x1 * y)
sum_x2y = np.sum(x2 * y)
sum_x1x2 = np.sum(x1 * x2)
square_x1 = np.sum(x1**2)
square_x2 = np.sum(x2**2)

# means
x1_mean = np.mean(x1)
x2_mean = np.mean(x2)
y_mean = np.mean(y)

# denominator
denominator = (square_x1 * square_x2) - (sum_x1x2 ** 2)

# coefficients
beta_1 = ((square_x2 * sum_x1y) - (sum_x1x2 * sum_x2y)) / denominator
beta_2 = ((square_x1 * sum_x2y) - (sum_x1x2 * sum_x1y)) / denominator
beta_0 = y_mean - beta_1 * x1_mean - beta_2 * x2_mean

# regression equation
print(f"Regression equation: y = {beta_0:.2f} + {beta_1:.2f}x1 + {beta_2:.2f}x2")

# prediction
age_in = float(input("Enter age = "))
exp_in = float(input("Enter experience = "))
predicted_income = beta_0 + beta_1 * age_in + beta_2 * exp_in

print(f"Predicted income is = {predicted_income}")
