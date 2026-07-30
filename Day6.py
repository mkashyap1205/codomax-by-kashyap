# ==========================================
# DAY 6 - DATA FILTERING
# ==========================================

import pandas as pd

print("===================================")
print("DAY 6 - DATA FILTERING")
print("===================================")

# Load Dataset
df = pd.read_csv("Amazon.csv")

# ==========================================
# 1. VIEW DATASET
# ==========================================

print("\nFIRST 5 ROWS")
print(df.head())

# ==========================================
# 2. SELECT COLUMNS
# ==========================================

print("\nSELECTED COLUMNS")

selected_columns = df[['TotalAmount', 'Discount']]
print(selected_columns.head())

# ==========================================
# 3. FILTER ROWS
# ==========================================

print("\nFILTERED ROWS")

filtered_df = df[df['Discount'] > 50]

print(filtered_df.head())

# ==========================================
# 4. SORT DATASET
# ==========================================

print("\nSORTED DATASET")

sorted_df = df.sort_values(by='TotalAmount', ascending=False)

print(sorted_df.head())

# ==========================================
# 5. SAVE FILTERED DATASET
# ==========================================

filtered_df.to_csv("amazon_filtered.csv", index=False)

print("\nFiltered dataset saved successfully!")

# ==========================================
# FINAL OUTPUT
# ==========================================

print("\nOriginal Dataset Shape :", df.shape)
print("Filtered Dataset Shape :", filtered_df.shape)

print("\n===================================")
print("DAY 6 COMPLETED SUCCESSFULLY")
print("===================================")