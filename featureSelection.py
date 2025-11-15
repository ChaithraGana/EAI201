# Scenario Solution: Simulate Forward Selection
initial_accuracy = 0.0
# Step 1: Start with the best single feature
best_single = ('B', 0.85) # Best is Feature B (85%)
if best_single[1] - initial_accuracy >= 0.03: # 0.85 - 0.00 = 0.85 (>= 0.03)
    selected_features = [best_single[0]]
    current_accuracy = best_single[1]
    
# Step 2: Check combinations with the current set {B}
combination_BA = 0.88 # 88%
combination_BC = 0.86 # 86%

# Test Feature A: Improvement = 0.88 - 0.85 = 0.03
if combination_BA - current_accuracy >= 0.03: # 0.03 (>= 0.03) -> Add A
    selected_features.append('A')
    current_accuracy = combination_BA
    
# Test Feature C (B+C is not the next best, but let's check B+A+C)
# Improvement from B+A to B+A+C: 0.885 - 0.880 = 0.005
combination_BAC = 0.885
if combination_BAC - current_accuracy >= 0.03: # 0.005 is NOT >= 0.03
    stop_selection = True
else:
    stop_selection = True

print("\n--- Scenario Solution: Forward Selection ---")
print(f"Step 1: Select {best_single[0]}. Improvement: 85% - 0% = 85.0%")
print(f"Step 2: Test combinations with B. Best is B+A (88%). Improvement: 88% - 85% = 3.0%")
print(f"Since 3.0% >= 3.0%, ADD Feature A. Current features: {selected_features}")
print(f"Step 3: Test adding C (B+A+C). Accuracy: 88.5%. Improvement: 88.5% - 88.0% = 0.5%")
print(f"Since 0.5% is < 3.0%, STOP selection.")
print(f"Final Selected Features: {selected_features}")