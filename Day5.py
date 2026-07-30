# ==========================================
# DAY 5 - DATA CLEANING
# ==========================================

import pandas as pd

print("===================================")
print("DAY 5 - DATA CLEANING")
print("===================================")

# Load Dataset
df = pd.read_csv("quikr_car.csv")

# ==========================================
# 1. VIEW DATASET
# ==========================================

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

# ==========================================
# 2. CHECK MISSING VALUES
# ==========================================

print("\nMISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

# Fill missing values
df.fillna("Unknown", inplace=True)

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

# ==========================================
# 3. REMOVE DUPLICATES
# ==========================================

duplicates = df.duplicated().sum()

print("\nDUPLICATE ROWS BEFORE:", duplicates)

df.drop_duplicates(inplace=True)

duplicates_after = df.duplicated().sum()

print("DUPLICATE ROWS AFTER :", duplicates_after)

# ==========================================
# 4. CHECK DATA TYPES
# ==========================================

print("\nDATA TYPES BEFORE")
print(df.dtypes)

# Convert object columns to string
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str)

print("\nDATA TYPES AFTER")
print(df.dtypes)

# ==========================================
# 5. SAVE CLEAN DATASET
# ==========================================

df.to_csv("quikr_car_cleaned.csv", index=False)

print("\nCLEAN DATASET SAVED AS:")
print("quikr_car_cleaned.csv")

# ==========================================
# FINAL OUTPUT
# ==========================================

print("\nFINAL DATASET SHAPE")
print(df.shape)

print("\n===================================")
print("DAY 5 COMPLETED SUCCESSFULLY")
print("===================================")