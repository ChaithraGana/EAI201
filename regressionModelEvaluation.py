from sklearn.metrics import mean_absolute_error, mean_squared_error

print("\n" + "="*50 + "\n")
print("--- 2. Regression Model Evaluation Metrics (MAE & MSE) ---")

# Data from the slide example [cite: 1074]
y_actual = np.array([250, 300, 200, 400, 350])
y_predicted = np.array([240, 310, 210, 380, 340])

# Calculate Mean Absolute Error (MAE) [cite: 1075]
# MAE is the average magnitude of the errors, in the same units as the target variable.
mae = mean_absolute_error(y_actual, y_predicted)

# Calculate Mean Squared Error (MSE) [cite: 1076]
# MSE penalizes larger errors more heavily because the differences are squared.
mse = mean_squared_error(y_actual, y_predicted)

print(f"Actual Values (y):     {y_actual}")
print(f"Predicted Values (ŷ):  {y_predicted}")
print(f"\nMean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE):  {mse:.2f}")

# Note: The differences are: [-10, 10, 10, -20, -10]
# MAE calculation: (| -10 | + | 10 | + | 10 | + | -20 | + | -10 |) / 5 = 60 / 5 = 12.00
# MSE calculation: ((-10)^2 + (10)^2 + (10)^2 + (-20)^2 + (-10)^2) / 5 = 800 / 5 = 160.00