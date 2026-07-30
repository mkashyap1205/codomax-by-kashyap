# import pandas

print("=======import pandas=======")

# Step 1: Import Pandas
import pandas as pd

# Step 2: Load CSV dataset
# Replace 'data.csv' with your CSV file name
df=pd.read_csv("data.csv")

# Step 3: Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Step 4: Display last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Step 5: Display column names
print("\nColumns:")
print(df.columns)

# Step 6: Display dataset information
print("\nDataset Information:")
print(df.info())

# Step 7: Display dataset shape
print("\nShape of Dataset:")
print(df.shape)

# Step 8: Display summary statistics
print("\nSummary Statistics:")
print(df.describe())