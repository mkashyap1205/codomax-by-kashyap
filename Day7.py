# ==========================================
# DAY 7 - DATA ANALYSIS
# ==========================================

import pandas as pd

print("===================================")
print("DAY 7 - DATA ANALYSIS")
print("===================================")

# Load Dataset
df = pd.read_csv("Amazon.csv")

# Convert rating_count to numeric
df['TotalAmount'] = pd.to_numeric(df['TotalAmount'], errors='coerce')

# ==========================================
# TOTAL
# ==========================================

print("\n1. TOTAL RATING COUNT")
print(df['TotalAmount'].sum())

# ==========================================
# AVERAGE
# ==========================================

print("\n2. AVERAGE RATING COUNT")
print(df['TotalAmount'].mean())

# ==========================================
# MINIMUM
# ==========================================

print("\n3. MINIMUM RATING COUNT")
print(df['TotalAmount'].min())

# ==========================================
# MAXIMUM
# ==========================================

print("\n4. MAXIMUM RATING COUNT")
print(df['TotalAmount'].max())

# ==========================================
# COUNT
# ==========================================

print("\n5. TOTAL RECORDS")
print(df['TotalAmount'].count())

# ==========================================
# BUSINESS INSIGHTS
# ==========================================

print("\n6. BUSINESS INSIGHTS")

print("Most Reviewed Product Count :", df['TotalAmount'].max())
print("Least Reviewed Product Count:", df['TotalAmount'].min())
print("Average Reviews Per Product :", round(df['TotalAmount'].mean(), 2))

# ==========================================
# FINAL OUTPUT
# ==========================================

print("\n===================================")
print("DAY 7 COMPLETED SUCCESSFULLY")
print("===================================")