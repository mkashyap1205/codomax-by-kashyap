# ==========================================
# DAY 8 - DATA VISUALIZATION
# ==========================================
import pandas as pd
import matplotlib.pyplot as plt

print("===================================")
print("DAY 8 - DATA VISUALIZATION")
print("===================================")

# Load Dataset
df = pd.read_csv("Amazon.csv")
print(df.columns)
print(df.head())
# ------------------------------------------
# Clean Data
# ------------------------------------------

df['TotalAmount'] = pd.to_numeric(df['TotalAmount'], errors='coerce')

# Take Top 10 Products
top10 = df.head(10)

# ==========================================
# 1. BAR CHART
# ==========================================
print("=============BAR CHART==================")
plt.figure(figsize=(10,5))
plt.bar(top10['City'], top10['TotalAmount'])
plt.title("Product TotalAmount - Bar Chart")
plt.xlabel("City")
plt.ylabel("TotalAmount")
plt.xticks(rotation=90)

plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# ==========================================
# 2. LINE CHART
# ==========================================
print("=============LINE CHART==================")
plt.figure(figsize=(10,5))
plt.plot(top10['TotalAmount'], marker='o')

plt.title("TotalAmount Trend - Line Chart")
plt.xlabel("Index")
plt.ylabel("TotalAmount")

plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

# ==========================================
# 3. PIE CHART
# ==========================================
print("=============PIE CHART==================")
rating_counts = df['TotalAmount'].value_counts().head(5)

plt.figure(figsize=(7,7))
plt.pie(
    rating_counts,
    labels=rating_counts.index,
    autopct='%1.1f%%'
)

plt.title("Top Ratings Distribution")

plt.savefig("pie_chart.png")
plt.show()

# ==========================================
# FINAL OUTPUT
# ==========================================

print("\nCharts created successfully!")
print("Saved Files:")
print("1. bar_chart.png")
print("2. line_chart.png")
print("3. pie_chart.png")

print("\n===================================")
print("DAY 8 COMPLETED SUCCESSFULLY")
print("===================================")