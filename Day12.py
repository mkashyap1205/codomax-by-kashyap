# ==========================================
# DAY 12 - PROJECT IMPROVEMENT
# Project: Amazon Sales Data Analysis
# ==========================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 50)
print("      DAY 12 - PROJECT IMPROVEMENT")
print("=" * 50)

# ------------------------------------------
# Load Dataset
# ------------------------------------------
print("\nLoading Amazon Sales Dataset...")

df = pd.read_csv("amazon.csv")

print("Dataset Loaded Successfully!")

# ------------------------------------------
# Display Basic Information
# ------------------------------------------
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

# ------------------------------------------
# Data Cleaning
# ------------------------------------------
print("\nChecking Missing Values...")

print(df.isnull().sum())

# ------------------------------------------
# Improve Data Types
# ------------------------------------------
# Convert TotalAmount to numeric
df['TotalAmount'] = pd.to_numeric(df['TotalAmount'], errors='coerce')

top10 = df.head(10)

plt.figure(figsize=(10,5))
plt.bar(top10['ProductName'], top10['TotalAmount'])

plt.title("Top 10 Product Sales")
plt.xlabel("Product Name")
plt.ylabel("Total Amount")

plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig("Improved_Bar_Chart.png")
plt.show()

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("Improved_Bar_Chart.png")

plt.show()

# ------------------------------------------
# Summary
# ------------------------------------------
print("\nSummary Statistics")

print(df.describe())

# ------------------------------------------
# Final Message
# ------------------------------------------
print("\nProject Improved Successfully!")

print("\nProfessional Notebook Completed!")

print("=" * 50)
print("DAY 12 COMPLETED SUCCESSFULLY")
print("=" * 50)