import numpy as np

area = np.array([340, 340, 640, 880, 990, 510])
rent = np.array([500, 1700, 1100, 800, 1400, 500])

x_mean = np.mean(area)
y_mean = np.mean(rent)


numerator = np.sum((area - x_mean) * (rent - y_mean))
denominator = np.sum((area - x_mean) ** 2)
beta1 = numerator / denominator

beta0 = y_mean - beta1 * x_mean

predicted_rent = beta0 + beta1 * area

print(f"β1 (slope): {beta1}")
print(f"β0 (intercept): {beta0}")
print(f"Regression equation: y = {beta0:.2f} + {beta1:.2f}x")
x = float(input(f"enter Area(x) = "))
predicted_rent = beta0 + beta1 * x
print(f"Predicted rent is = {predicted_rent}")


----------------------------------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd

from google.colab import files
uploaded = files.upload()

x = df['Attendance_Hours'].values
y = df['Final_Marks'].values

df = pd.read_csv("Study_vs_Score_data.csv")

x_mean = np.mean(x)
y_mean = np.mean(y)


numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
beta1 = numerator / denominator

beta0 = y_mean - beta1 * x_mean

predicted_rent = beta0 + beta1 * x

print(f"β1 (slope): {beta1}")
print(f"β0 (intercept): {beta0}")
print(f"Regression equation: y = {beta0:.2f} + {beta1:.2f}x")
x_in = float(input(f"Enter Area = "))
predicted_rent = beta0 + beta1 * x_in
print(f"Predicted rent is = {predicted_rent}")
