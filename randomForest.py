from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Generate a synthetic dataset
X, y = make_classification(n_samples=100, n_features=5, n_informative=3, n_redundant=0, 
                           random_state=42)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the Random Forest model
# n_estimators is the number of trees
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Get feature importances (a key advantage of RF)
feature_importances = model.feature_importances_
importance_df = pd.DataFrame({
    'Feature': [f'Feature_{i}' for i in range(X.shape[1])],
    'Importance': feature_importances
}).sort_values(by='Importance', ascending=False)

print("\n--- Random Forest Concept ---")
print(f"Test Accuracy: {model.score(X_test, y_test):.4f}")
print("\nTop 3 Feature Importances:")
print(importance_df.head(3))