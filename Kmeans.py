from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate synthetic data for clustering
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=42)

# --- Elbow Method to find optimal K ---
wcss = []
k_values = range(1, 11)

for i in k_values:
    # Set n_init='auto' to silence warnings in newer scikit-learn versions
    kmeans = KMeans(n_clusters=i, random_state=42, n_init='auto') 
    kmeans.fit(X)
    wcss.append(kmeans.inertia_) # inertia_ is the WCSS

# Plotting the elbow (you must describe this plot in your exam)
plt.figure(figsize=(6, 4))
plt.plot(k_values, wcss, marker='o', linestyle='--')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.show()

# --- Apply K-Means with the chosen K (let's assume K=4 from the plot) ---
kmeans = KMeans(n_clusters=4, random_state=42, n_init='auto')
cluster_labels = kmeans.fit_predict(X)

print("\n--- K-Means Clustering Concept ---")
print("WCSS values for K=1 to 10:", [f"{w:.0f}" for w in wcss])
print("First 10 Data Points' Cluster Labels:", cluster_labels[:10])