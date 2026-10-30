import pandas as pd
from pathlib import Path

# Project folder ka path
BASE_DIR = Path(__file__).resolve().parent.parent

# Input aur output files
INPUT_FILE = BASE_DIR / "data" / "ApexPlanet_DataAnalytics_Dataset (1).xlsx"
OUTPUT_FILE = BASE_DIR / "data" / "sales_cleaned.csv"

print("=" * 50)
print("DATA CLEANING STARTED")
print("=" * 50)

# Original dataset load karna
df = pd.read_excel(INPUT_FILE, sheet_name="Sales_Dataset")

print("\nOriginal dataset shape:", df.shape)

# Cleaning se pehle missing values check karna
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Age ki missing values ko median se fill karna
age_median = df["Age"].median()
df["Age"] = df["Age"].fillna(age_median)

print("\nMissing Age values filled with median:", age_median)

# City ki missing values ko Unknown se fill karna
df["City"] = df["City"].fillna("Unknown")

print("Missing City values filled with: Unknown")

# Order_Date ko date format mein convert karna
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

invalid_dates = df["Order_Date"].isnull().sum()
print("Invalid or missing dates:", invalid_dates)

# Exact duplicate rows remove karna
duplicates_before = df.duplicated().sum()
df = df.drop_duplicates()

print("Duplicate rows removed:", duplicates_before)

# Cleaned dataset ko CSV mein save karna
df.to_csv(OUTPUT_FILE, index=False, date_format="%Y-%m-%d")

# Final results
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nFinal dataset shape:", df.shape)
print("\nCleaned dataset saved at:")
print(OUTPUT_FILE)

print("\nDATA CLEANING COMPLETED")
