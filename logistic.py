import numpy as np

# Example dataset
x = np.array([1, 2, 3, 4, 5])          # Feature (e.g., study hours)
y = np.array([0, 0, 0, 1, 1])          # Labels (0 = fail, 1 = pass)

# Initialize parameters
b0, b1 = 0, 0
lr = 0.1                               # Learning rate
epochs = 1000                          # Number of iterations

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Training using Gradient Descent
for _ in range(epochs):
    z = b0 + b1 * x
    y_pred = sigmoid(z)
    
    # Compute gradients
    db0 = np.sum(y_pred - y) / len(y)
    db1 = np.sum((y_pred - y) * x) / len(y)
    
    # Update parameters
    b0 -= lr * db0
    b1 -= lr * db1

# Final equation
print(f"β0 (intercept): {b0:.3f}")
print(f"β1 (slope): {b1:.3f}")
print(f"Equation: p = 1 / (1 + exp(-({b0:.3f} + {b1:.3f}x)))")

# Prediction
x_in = float(input("Enter study hours: "))
z = b0 + b1 * x_in
prob = sigmoid(z)
print(f"Probability of passing (y=1): {prob:.3f}")
