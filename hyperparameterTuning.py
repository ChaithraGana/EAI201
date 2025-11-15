from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import time

print("\n" + "="*50 + "\n")
print("--- 4. Hyperparameter Tuning (Grid Search & Randomized Search) ---")

# Use the Iris data (X, y) from Section 1

# Define the hyperparameter search space (range of 'K' values to test)
param_grid = {
    'n_neighbors': np.arange(1, 20), # Test K from 1 up to 19
    'weights': ['uniform', 'distance'] # Test two different weighting schemes
}
model_knn = KNeighborsClassifier()

# --- Grid Search Implementation [cite: 1239] ---
# Grid Search exhaustively tests ALL possible combinations.
print("Starting Grid Search...")
start_time = time.time()
grid_search = GridSearchCV(
    estimator=model_knn,
    param_grid=param_grid,
    cv=5, # Use 5-fold CV for evaluation
    scoring='accuracy'
)
grid_search.fit(X_train, y_train)
end_time = time.time()

print(f"Time taken (Grid Search, {len(grid_search.cv_results_['params'])} combinations): {end_time - start_time:.2f} seconds")
print(f"Best parameters found (Grid Search): {grid_search.best_params_}")
print(f"Best cross-validation accuracy (Grid Search): {grid_search.best_score_:.4f}\n")


# --- Randomized Search Implementation [cite: 1245] ---
# Randomized Search samples a fixed number of combinations from the search space.
print("Starting Randomized Search...")
start_time = time.time()
random_search = RandomizedSearchCV(
    estimator=model_knn,
    param_distributions=param_grid,
    n_iter=10, # Only test 10 random combinations (much faster)
    cv=5,
    scoring='accuracy',
    random_state=42
)
random_search.fit(X_train, y_train)
end_time = time.time()

print(f"Time taken (Randomized Search, 10 combinations): {end_time - start_time:.2f} seconds")
print(f"Best parameters found (Randomized Search): {random_search.best_params_}")
print(f"Best cross-validation accuracy (Randomized Search): {random_search.best_score_:.4f}")