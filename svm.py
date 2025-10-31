import numpy as np

class SVM:
    def __init__(self, lr=0.001, lambda_param=0.01, n_iters=1000):  # ✅ double underscores
        self.lr = lr
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        
        # convert labels from {0,1} → {-1,1}
        y_ = np.where(y <= 0, -1, 1)

        # initialize weights
        self.w = np.zeros(n_features)
        self.b = 0

        # gradient descent
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                condition = y_[idx] * (np.dot(x_i, self.w) + self.b) >= 1
                if condition:
                    dw = 2 * self.lambda_param * self.w
                    db = 0
                else:
                    dw = 2 * self.lambda_param * self.w - np.dot(x_i, y_[idx])
                    db = -y_[idx]

                self.w -= self.lr * dw
                self.b -= self.lr * db

    def predict(self, X):
        approx = np.dot(X, self.w) + self.b
        return np.sign(approx)


# --------- Testing SVM on sample data ---------
if __name__ == "__main__":  # ✅ double underscores
    # Example dataset
    X = np.array([
        [1, 2],
        [2, 3],
        [3, 3],
        [2, 1],
        [3, 2]
    ])

    y = np.array([0, 0, 0, 1, 1])   # labels

    svm = SVM(lr=0.001, lambda_param=0.01, n_iters=1000)
    svm.fit(X, y)
    predictions = svm.predict(X)

    # Convert -1/1 back to 0/1 for display
    predictions_converted = np.where(predictions == -1, 0, 1)

    print("Prediction | Expected")
    print("---------------------")
    for pred, exp in zip(predictions_converted, y):
        print(f"    {pred}      |    {exp}")

    print("\nWeights:", svm.w)
    print("Bias:", svm.b)
