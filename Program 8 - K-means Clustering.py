import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

X = load_iris().data


class KMeansClusterer:
    def __init__(self, k=3, max_iter=100, tol=1e-4):
        self.k = k
        self.max_iter = max_iter
        self.tol = tol
        self.centroids = None

    def fit(self, X):
        self.centroids = self.__get_random_centroids(X)

        for i in range(self.max_iter):
            clusters = self.__assign_clusters(X)

            new_centroids = self.__update_centroids(X, clusters)

            if np.linalg.norm(new_centroids - self.centroids) < self.tol:
                print(f"Converged after {i} iterations")
                break

            self.centroids = new_centroids

        return clusters

    def __get_random_centroids(self, X):
        n = X.shape[0]
        return X[np.random.choice(n, self.k, replace=False)]

    def __assign_clusters(self, X):
        distances = np.linalg.norm(X[:, None] - self.centroids, axis=2)

        labels = np.argmin(distances, axis=1)
        return labels

    def __update_centroids(self, X, clusters):
        new_centroids = np.array([X[clusters == i].mean(axis=0) for i in range(self.k)])
        return new_centroids


kmeans = KMeansClusterer(k=3)
clusters = kmeans.fit(X)

print(kmeans.centroids)

print(clusters[:5])

plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap="viridis")
plt.scatter(
    kmeans.centroids[:, 0],
    kmeans.centroids[:, 1],
    c="red",
    s=200,
    marker="x",
    label="Centroids",
)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-means clustering")
plt.legend()
plt.show()
