import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# -------------------------------
# PCA Implementation
# -------------------------------
class PCA:
    def __init__(self, n_components):   # ✅ Fixed: __init__
        self.n_components = n_components
        self.components_ = None
        self.mean_ = None

    def fit(self, X):
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_
        cov_matrix = np.cov(X_centered, rowvar=False)
        eigen_values, eigen_vectors = np.linalg.eigh(cov_matrix)
        idxs = np.argsort(eigen_values)[::-1]
        self.components_ = eigen_vectors[:, idxs[:self.n_components]]

    def transform(self, X):
        X_centered = X - self.mean_
        return np.dot(X_centered, self.components_)

# -------------------------------
# LDA Implementation
# -------------------------------
class LDA:
    def __init__(self, n_components):   # ✅ Fixed: __init__
        self.n_components = n_components
        self.scalings_ = None

    def fit(self, X, y):
        n_features = X.shape[1]
        class_labels = np.unique(y)
        mean_overall = np.mean(X, axis=0)

        SW = np.zeros((n_features, n_features))
        SB = np.zeros((n_features, n_features))

        for c in class_labels:
            X_c = X[y == c]
            mean_c = np.mean(X_c, axis=0)
            SW += (X_c - mean_c).T @ (X_c - mean_c)
            n_c = X_c.shape[0]
            mean_diff = (mean_c - mean_overall).reshape(n_features, 1)
            SB += n_c * (mean_diff @ mean_diff.T)

        eig_vals, eig_vecs = np.linalg.eig(np.linalg.inv(SW).dot(SB))
        idxs = np.argsort(np.abs(eig_vals))[::-1]
        self.scalings_ = eig_vecs[:, idxs[:self.n_components]]

    def transform(self, X):
        return np.dot(X, self.scalings_)

# -------------------------------
# SVD Example
# -------------------------------
def compute_svd(X):
    U, S, VT = np.linalg.svd(X - np.mean(X, axis=0), full_matrices=False)
    return U[:, :2] @ np.diag(S[:2])   # ✅ Fixed SVD output shape

# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":   # ✅ Fixed: __name__
    iris = load_iris()
    X, y = iris.data, iris.target

    # PCA
    pca = PCA(n_components=2)
    pca.fit(X)
    X_pca = pca.transform(X)
    print("PCA Transformed Data (first 5 rows):\n", X_pca[:5])

    # LDA
    lda = LDA(n_components=2)
    lda.fit(X, y)
    X_lda = lda.transform(X)
    print("\nLDA Transformed Data (first 5 rows):\n", X_lda[:5])

    # SVD
    X_svd = compute_svd(X)
    print("\nSVD Transformed Data (first 5 rows):\n", X_svd[:5])

    # -------------------------------
    # Visualizations
    # -------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    axes[0].scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='rainbow', s=50)
    axes[0].set_title("PCA Projection")

    axes[1].scatter(X_lda[:, 0], X_lda[:, 1], c=y, cmap='rainbow', s=50)
    axes[1].set_title("LDA Projection")

    axes[2].scatter(X_svd[:, 0], X_svd[:, 1], c=y, cmap='rainbow', s=50)
    axes[2].set_title("SVD Projection")

    for ax in axes:
        ax.set_xlabel("Component 1")
        ax.set_ylabel("Component 2")

    plt.tight_layout()
    plt.show()

