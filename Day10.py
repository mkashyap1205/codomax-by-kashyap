# ==========================================
# DAY 10 - EXPORT DATA
# ==========================================

import pandas as pd

print("===================================")
print("DAY 10 - EXPORT DATA")
print("===================================")

# Load Dataset
df = pd.read_csv("employee_data.csv")

# ==========================================
# DATA CLEANING
# ==========================================

print("\nDataset Shape Before Cleaning:")
print(df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

print("\nDataset Shape After Cleaning:")
print(df.shape)

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# ==========================================
# EXPORT CLEANED DATASET
# ==========================================

output_file = "amazon_cleaned_dataset.csv"

df.to_csv(output_file, index=False)

print("\nCleaned dataset exported successfully!")
print("File Name:", output_file)

print("\n===================================")
print("DAY 10 COMPLETED SUCCESSFULLY")
print("===================================")