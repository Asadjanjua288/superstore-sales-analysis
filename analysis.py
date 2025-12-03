# ---------------------------------------------
#   Superstore Sales Data Analysis - Step 1
#   Load & Inspect Dataset
# ---------------------------------------------

import pandas as pd

# --- Step 1: Load your dataset ---
file_path = r"C:\Users\Pc\Downloads\Sample_-_Superstore.csv"

try:
    df = pd.read_csv(file_path, encoding='latin1')   # handles special characters
    print("Dataset loaded successfully!")
except Exception as e:
    print("Error loading the dataset:", e)
# ---------------------------------------------
#   STEP 2: Data Cleaning & Preprocessing
# ---------------------------------------------

# Convert Order Date & Ship Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Add Year, Month, and Quarter columns
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Month Name'] = df['Order Date'].dt.strftime('%B')
df['Quarter'] = df['Order Date'].dt.quarter

print("\n--- Date Columns Converted & Time Features Added ---")
print(df[['Order Date', 'Year', 'Month', 'Month Name', 'Quarter']].head())

# Check duplicates
duplicates = df.duplicated().sum()
print(f"\n--- Number of Duplicate Rows: {duplicates} ---")

# Remove duplicates if any
if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicates removed.")
else:
    print("No duplicates found.")

# Basic statistics summary
print("\n--- Statistical Summary (Numeric Columns) ---")
print(df[['Sales', 'Quantity', 'Discount', 'Profit']].describe())

# Check for negative profits (common but useful)
negative_profits = df[df['Profit'] < 0].shape[0]
print(f"\n--- Rows with Negative Profit: {negative_profits} ---")

# ---------------------------------------------
#   STEP 3: Exploratory Data Analysis (EDA)
# ---------------------------------------------

print("\n=== TOTAL SALES BY YEAR ===")
sales_by_year = df.groupby('Year')['Sales'].sum().sort_index()
print(sales_by_year)

print("\n=== TOTAL PROFIT BY YEAR ===")
profit_by_year = df.groupby('Year')['Profit'].sum().sort_index()
print(profit_by_year)

print("\n=== MONTHLY SALES TREND (All Years Combined) ===")
monthly_sales = df.groupby('Month')['Sales'].sum().sort_index()
print(monthly_sales)

print("\n=== SALES BY CATEGORY ===")
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(category_sales)

print("\n=== SALES BY REGION ===")
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(region_sales)

print("\n=== TOP 10 PRODUCTS BY SALES ===")
top_products_sales = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_products_sales)

print("\n=== TOP 10 PRODUCTS BY PROFIT ===")
top_products_profit = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
print(top_products_profit)

print("\n=== WORST 10 PRODUCTS (MOST NEGATIVE PROFIT) ===")
worst_products_profit = df.groupby('Product Name')['Profit'].sum().sort_values().head(10)
print(worst_products_profit)

# --- Step 2: Show dataset info ---
print("\n--- Dataset Info ---")
print(df.info())

# --- Step 3: Show top 5 rows ---
print("\n--- First 5 Rows ---")
print(df.head())

# --- Step 4: Check missing values ---
print("\n--- Missing Values ---")
print(df.isnull().sum())
