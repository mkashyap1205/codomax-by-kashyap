# ==========================================
# DAY 9 - MINI DASHBOARD
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

print("===================================")
print("DAY 9 - MINI DASHBOARD")
print("===================================")

# Load Dataset
df = pd.read_csv("Amazon.csv")

# ==========================================
# DATASET PREVIEW
# ==========================================

print("\nFIRST 5 ROWS")
print(df.head())

print("\nLAST 5 ROWS")
print(df.tail())

# ==========================================
# DATASET INFORMATION
# ==========================================

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATASET INFO")
df.info()

# ==========================================
# DATA CLEANING
# ==========================================

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("\nDATASET SHAPE AFTER CLEANING")
print(df.shape)

# ==========================================
# DATA TYPE CONVERSION
# ==========================================

df["TotalAmount"] = pd.to_numeric(df["TotalAmount"], errors="coerce")
df["TotalAmount"] = (
    df["TotalAmount"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

df["TotalAmount"] = pd.to_numeric(df["TotalAmount"], errors="coerce")

# ==========================================
# DATA ANALYSIS
# ==========================================

print("\n========== DATA ANALYSIS ==========")

print("Total Amount :", df["TotalAmount"].sum())
print("Average Rating :", round(df["TotalAmount"].mean(),2))
print("Minimum Rating :", df["TotalAmount"].min())
print("Maximum Rating :", df["TotalAmount"].max())
print("Total Products :", df["TotalAmount"].count())

# ==========================================
# BAR CHART
# ==========================================

top10 = df.head(10)

plt.figure(figsize=(10,5))
plt.bar(top10["City"], top10["TotalAmount"])
plt.title("Top 10 Product Ratings")
plt.xlabel("Product ID")
plt.ylabel("Rating")
plt.xticks(rotation=90)
plt.show()

# ==========================================
# LINE CHART
# ==========================================

plt.figure(figsize=(10,5))
plt.plot(top10["TotalAmount"], marker="o")
plt.title("Product Rating Trend")
plt.xlabel("Index")
plt.ylabel("Rating")
plt.show()

# ==========================================
# PIE CHART
# ==========================================

rating_distribution = df["TotalAmount"].value_counts().head(5)

plt.figure(figsize=(7,7))
plt.pie(
    rating_distribution,
    labels=rating_distribution.index,
    autopct="%1.1f%%"
)
plt.title("Rating Distribution")
plt.show()

# ==========================================
# BUSINESS INSIGHTS
# ==========================================

print("\n========== BUSINESS INSIGHTS ==========")

print("Total Products :", len(df))
print("Average Rating :", round(df["TotalAmount"].mean(),2))
print("Highest Rating :", df["TotalAmount"].max())
print("Lowest Rating :", df["TotalAmount"].min())
print("Most Used Payment Method :", df.loc[df["PaymentMethod"].idxmax(), "ProductName"])
print("Highest Rating Count :", int(df["TotalAmount"].max()))

# ==========================================
# DASHBOARD COMPLETED
# ==========================================

print("\n===================================")
print("MINI DASHBOARD COMPLETED SUCCESSFULLY")
print("===================================")