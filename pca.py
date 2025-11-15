from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

# Create a dataset with 5 features
data = np.random.rand(10, 5) # 10 samples, 5 features
df = pd.DataFrame(data, columns=[f'F{i}' for i in range(1, 6)])

# 1. Standardize the data (A crucial step for PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# 2. Apply PCA to reduce to 2 components
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_scaled)

# Create a new DataFrame for the principal components
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

print("\n--- Principal Component Analysis (PCA) Concept ---")
print("Original Data Shape:", df.shape)
print("PCA Reduced Data Shape:", pca_df.shape)
print(f"\nVariance Explained by PC1: {pca.explained_variance_ratio_[0]:.4f}")
print(f"Variance Explained by PC2: {pca.explained_variance_ratio_[1]:.4f}")
print(f"Cumulative Variance Explained: {pca.explained_variance_ratio_.sum():.4f}")
print("\nFirst 3 rows of Principal Components:")
print(pca_df.head(3))