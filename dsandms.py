import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# --- 1. Data Splitting (Train/Test/Validation) ---
print("--- 1. Data Splitting and Classification Metrics ---")

# Load a sample dataset (Iris, as suggested in the homework [cite: 993])
data = load_iris()
X, y = data.data, data.target

# Split the data into Training (70%) and Testing (30%) sets [cite: 927]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print(f"Total samples: {len(X)}")
print(f"Training samples (70%): {len(X_train)}")
print(f"Testing samples (30%): {len(X_test)}\n")

# --- 2. Classification Model Training and Evaluation ---

# Train a simple classification model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate and display metrics
print("Evaluation Metrics on the Test Set:")
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# Confusion Matrix [cite: 1043]
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)
# The matrix rows represent Actual classes, and columns represent Predicted classes.

# Display individual metrics (using the second class for a binary view, where available)
# In multi-class, these are usually calculated with 'weighted' or 'macro' averaging
print("\nMetrics (Macro Average for Multi-Class):")
print(f"Precision: {precision_score(y_test, y_pred, average='macro'):.4f}")
print(f"Recall:    {recall_score(y_test, y_pred, average='macro'):.4f}")
print(f"F1 Score:  {f1_score(y_test, y_pred, average='macro'):.4f}")