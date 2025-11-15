from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Generate synthetic data
X = np.array([5, 15, 25, 35, 45, 55]).reshape(-1, 1) # Study Hours
y = np.array([5, 20, 14, 32, 22, 38]) # Exam Scores

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("--- Linear Regression Concept ---")
print(f"Coefficients (Slope): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2): {r2:.2f}")

# Scenario Solution: Linear Regression Prediction
m = 150.0 # Slope (Coefficient)
c = 50000 # Intercept
sq_footage = 1800

# Prediction formula: Price = m * Sq_Footage + c
predicted_price = m * sq_footage + c

print("\n--- Scenario Solution: Linear Regression ---")
print(f"The predicted house price for 1800 sq. ft. is: ${predicted_price:.2f}")