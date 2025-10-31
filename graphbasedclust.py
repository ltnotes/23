import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree

# Graph-based clustering using MST
def mst_clustering(X, k):
    # Step 1: Compute distance matrix
    dist_matrix = squareform(pdist(X))

    # Step 2: Compute MST
    mst = minimum_spanning_tree(dist_matrix).toarray()
    mst = mst + mst.T  # Make symmetric

    # Step 3: Remove (k-1) largest edges
    mst_flat = mst.flatten()
    non_zero_edges = mst_flat[mst_flat > 0]
    threshold = np.sort(non_zero_edges)[- (k - 1)]
    mst[mst > threshold] = 0

    # Step 4: Assign clusters using DFS
    n_samples = X.shape[0]
    visited = [False] * n_samples
    labels = [-1] * n_samples
    cluster_id = 0

    def dfs(node):
        visited[node] = True
        labels[node] = cluster_id
        for neighbor in range(n_samples):
            if mst[node, neighbor] > 0 and not visited[neighbor]:
                dfs(neighbor)

    for i in range(n_samples):
        if not visited[i]:
            dfs(i)
            cluster_id += 1

    return np.array(labels)

# Example usage
if __name__ == "__main__":
    from sklearn.datasets import make_blobs

    # Generate synthetic dataset
    X, _ = make_blobs(n_samples=200, centers=3, random_state=42)

    # Perform graph-based clustering
    labels = mst_clustering(X, k=3)

    # Visualization
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='rainbow', s=50)
    plt.title("Graph-based Clustering using MST")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()
