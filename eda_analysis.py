import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "sales_cleaned.csv"
CHART_DIR = BASE_DIR / "charts"
REPORT_DIR = BASE_DIR / "report"

CHART_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)

print("=" * 50)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# Load cleaned data
df = pd.read_csv(DATA_FILE)
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# 1. Dataset overview
print("\n1. DATASET OVERVIEW")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. Descriptive statistics
print("\n2. DESCRIPTIVE STATISTICS")
print(df.describe().round(2))

# 3. Sales by category
print("\n3. SALES BY CATEGORY")
category_sales = df.groupby("Category")["Total_Sales"].sum()
print(category_sales.sort_values(ascending=False).round(2))

plt.figure(figsize=(10, 6))
category_sales.sort_values().plot(kind="barh")
plt.title("Total Sales by Category")
plt.xlabel("Total Sales")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig(CHART_DIR / "sales_by_category.png", dpi=300)
plt.close()

# 4. Sales by city
print("\n4. SALES BY CITY")
city_sales = df.groupby("City")["Total_Sales"].sum()
print(city_sales.sort_values(ascending=False).round(2))

plt.figure(figsize=(10, 6))
city_sales.sort_values().plot(kind="barh")
plt.title("Total Sales by City")
plt.xlabel("Total Sales")
plt.ylabel("City")
plt.tight_layout()
plt.savefig(CHART_DIR / "sales_by_city.png", dpi=300)
plt.close()

# 5. Product sales
print("\n5. SALES BY PRODUCT")
product_sales = df.groupby("Product")["Total_Sales"].sum()
print(product_sales.sort_values(ascending=False).round(2))

plt.figure(figsize=(10, 6))
product_sales.sort_values().plot(kind="barh")
plt.title("Total Sales by Product")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(CHART_DIR / "sales_by_product.png", dpi=300)
plt.close()

# 6. Monthly sales trend
print("\n6. MONTHLY SALES")
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("Month")["Total_Sales"].sum()
print(monthly_sales.round(2))

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(CHART_DIR / "monthly_sales_trend.png", dpi=300)
plt.close()

# 7. Correlation analysis
print("\n7. CORRELATION MATRIX")
numeric_cols = ["Age", "Quantity", "Unit_Price", "Total_Sales"]
correlation = df[numeric_cols].corr()
print(correlation.round(3))

plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(CHART_DIR / "correlation_heatmap.png", dpi=300)
plt.close()

# 8. Save summary statistics
summary = df.describe().round(2)
summary.to_csv(REPORT_DIR / "descriptive_statistics.csv")

# Save category sales
category_sales.to_csv(REPORT_DIR / "category_sales.csv")

# Save city sales
city_sales.to_csv(REPORT_DIR / "city_sales.csv")

# Save product sales
product_sales.to_csv(REPORT_DIR / "product_sales.csv")

# Save monthly sales
monthly_sales.to_csv(REPORT_DIR / "monthly_sales.csv")

print("\nEDA COMPLETED SUCCESSFULLY!")
print("Charts saved in:", CHART_DIR)
print("Reports saved in:", REPORT_DIR)