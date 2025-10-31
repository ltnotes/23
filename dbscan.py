import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from collections import deque

# ----- DBSCAN Implementation -----
class DBSCAN:
    def __init__(self, eps=0.5, min_samples=5):
        self.eps = eps
        self.min_samples = min_samples
        self.labels_ = None

    def fit(self, X):
        n_samples = X.shape[0]
        self.labels_ = np.full(n_samples, -1)  # Initialize all points as noise (-1)
        cluster_id = 0

        for i in range(n_samples):
            if self.labels_[i] != -1:
                continue  # already labeled
            neighbors = self._region_query(X, i)
            if len(neighbors) < self.min_samples:
                self.labels_[i] = -1  # Mark as noise
            else:
                self._expand_cluster(X, i, neighbors, cluster_id)
                cluster_id += 1

    def _expand_cluster(self, X, point_idx, neighbors, cluster_id):
        self.labels_[point_idx] = cluster_id
        queue = deque(neighbors)

        while queue:
            idx = queue.popleft()
            if self.labels_[idx] == -1:  # Previously marked as noise
                self.labels_[idx] = cluster_id
            if self.labels_[idx] != -1:
                continue
            self.labels_[idx] = cluster_id
            new_neighbors = self._region_query(X, idx)
            if len(new_neighbors) >= self.min_samples:
                queue.extend(new_neighbors)

    def _region_query(self, X, point_idx):
        distances = np.linalg.norm(X - X[point_idx], axis=1)
        neighbors = np.where(distances <= self.eps)[0]
        return neighbors


# ----- Example 2: Using make_blobs -----
if __name__ == "__main__":
    # Generate sample data with 3 clusters
    X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.5, random_state=42)

    # Run DBSCAN
    dbscan = DBSCAN(eps=0.4, min_samples=5)
    dbscan.fit(X)
    labels = dbscan.labels_

    # Plot results
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='plasma', s=50)
    plt.title("DBSCAN Clustering (3 Blobs Example)")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()
