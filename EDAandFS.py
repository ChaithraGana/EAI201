import pandas as pd
import numpy as np

# Create a simple, self-contained dataset
data = {
    'OrderID': range(101, 106),
    'Age': [25, 30, 45, 22, np.nan], # Missing value
    'City': ['Mumbai', 'Delhi', 'Mumbai', 'Chennai', 'Delhi'],
    'Revenue': [1500.50, 750.00, 3200.00, 500.00, 950.00]
}
df = pd.DataFrame(data)

print("--- EDA: Initial Exploration ---")

# 1. Check shape and column names
print(f"Shape (Rows, Columns): {df.shape}")

# 2. Check data types and non-null counts
print("\nColumn Info:")
df.info()

# 3. Check for missing values (crucial step)
print("\nMissing Values Count:")
print(df.isnull().sum())

# 4. Descriptive statistics for numerical data
print("\nRevenue Statistics:")
print(df['Revenue'].describe())

#feature engineering

import pandas as pd

# Use a sample dataset with a Date column and a categorical feature
data = {
    'Purchase_Date': ['2023-01-05', '2023-01-10', '2023-02-15', '2023-02-28'],
    'Service_Tier': ['Basic', 'Premium', 'Pro', 'Basic'],
    'Price': [100, 200, 300, 100]
}
df_fe = pd.DataFrame(data)
df_fe['Purchase_Date'] = pd.to_datetime(df_fe['Purchase_Date'])

print("--- Feature Engineering Code ---")

# 1. Feature Creation from Date/Time
df_fe['Purchase_Month'] = df_fe['Purchase_Date'].dt.month
df_fe['Day_of_Week'] = df_fe['Purchase_Date'].dt.day_name()

# 2. Ordinal Encoding (Mapping) for 'Service_Tier'
# Assign numerical values based on the inherent order (Basic < Premium < Pro)
tier_mapping = {'Basic': 1, 'Premium': 2, 'Pro': 3}
df_fe['Tier_Encoded'] = df_fe['Service_Tier'].map(tier_mapping)

# 3. One-Hot Encoding (for Day_of_Week)
df_encoded = pd.get_dummies(df_fe, columns=['Day_of_Week'], drop_first=True)

print("\nEngineered Data (Showing new columns):")
print(df_encoded[['Purchase_Date', 'Purchase_Month', 'Tier_Encoded', 'Day_of_Week_Sunday', 'Day_of_Week_Wednesday']])

#scenario based 
"""Scenario-Based Question (EDA & FE)
A dataset has an Employee_ID column (unique string), an Annual_Salary column (numeric with a few negative values due to error), and a Department column (categorical with 'IT', 'HR', 'Sales').

What is the first EDA step to identify the erroneous salary entries?

What Feature Engineering step is needed for the Department column before feeding it to a Linear Regression model?"""

# Scenario Data
data = {'Employee_ID': ['A101', 'A102', 'A103', 'A104'],
        'Annual_Salary': [60000, 75000, -5000, 90000], # Error
        'Department': ['IT', 'HR', 'Sales', 'IT']}
scenario_df = pd.DataFrame(data)

print("\n--- Scenario Solution: EDA & FE ---")

# 1. EDA Step: Identifying Erroneous Salary
# Use descriptive statistics and filtering to spot the anomaly.
print("1. Identifying Error (Negative Salary):")
print(scenario_df['Annual_Salary'].describe())
print(scenario_df[scenario_df['Annual_Salary'] < 0])


# 2. Feature Engineering Step: Encoding Categorical 'Department'
from sklearn.preprocessing import OneHotEncoder

print("\n2. One-Hot Encoding for 'Department':")
# One-Hot Encoding is used to convert categorical strings into a numerical format 
# that models can understand, without implying any ordering.
df_encoded = pd.get_dummies(scenario_df, columns=['Department'], prefix='Dept', drop_first=True)

print(df_encoded)