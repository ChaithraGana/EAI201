from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.datasets import load_iris

# Load a built-in dataset for classification (Iris is multi-class, but we'll focus on two)
iris = load_iris()
X, y = iris.data, iris.target

# Use only the first two features and two classes for simplicity
X = X[y != 2, :2]
y = y[y != 2]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("\n--- Logistic Regression Concept ---")
print(f"Accuracy: {accuracy:.4f}")
print("Confusion Matrix:")
# [[True Negatives, False Positives],
#  [False Negatives, True Positives]]
print(conf_matrix)

