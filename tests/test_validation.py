import pandas as pd

# Load dataset
df = pd.read_csv("data/heart_disease_uci.csv")

print("=" * 40)
print("HEART DISEASE DATA VALIDATION REPORT")
print("=" * 40)

# Missing values
print("\n1. Missing Values")
print(df.isnull().sum())

# Duplicate rows
print("\n2. Duplicate Rows")
print(df.duplicated().sum())

# Data types
print("\n3. Data Types")
print(df.dtypes)

# Value ranges
print("\n4. Value Range")

if "age" in df.columns:
    print("Age:", df["age"].min(), "-", df["age"].max())

if "chol" in df.columns:
    print("Cholesterol:", df["chol"].min(), "-", df["chol"].max())

print("\nValidation Completed Successfully.")
