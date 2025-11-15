from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier # Using this model as suggested in the homework [cite: 993]

print("\n" + "="*50 + "\n")
print("--- 3. K-Fold Cross-Validation ---")

# Define the model and the number of folds (k=5 is a common choice [cite: 971])
model_cv = RandomForestClassifier(random_state=42)
k_folds = 5

# Perform 5-Fold Cross-Validation
# The cross_val_score function automatically handles the splitting, training, and testing
cv_scores = cross_val_score(model_cv, X, y, cv=k_folds, scoring='accuracy')

print(f"K-Fold (k={k_folds}) Cross-Validation Scores (Accuracy for each fold):")
for i, score in enumerate(cv_scores):
    print(f"Fold {i+1} Accuracy: {score:.4f}")

# Calculate the mean cross-validation accuracy [cite: 939]
mean_cv_accuracy = np.mean(cv_scores)
print(f"\nMean Cross-Validation Accuracy (Robust Estimate): {mean_cv_accuracy:.4f}")