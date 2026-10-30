import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "ApexPlanet_DataAnalytics_Dataset (1).xlsx"

df = pd.read_excel(DATA_FILE, sheet_name="Sales_Dataset")

print("=" * 50)
print("DATASET BASIC INFORMATION")
print("=" * 50)

print("\n1. Dataset Shape:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n2. Column Names:")
print(df.columns.tolist())

print("\n3. Data Types:")
print(df.dtypes)

print("\n4. Missing Values:")
print(df.isnull().sum())

print("\n5. Duplicate Rows:")
print(df.duplicated().sum())

print("\n6. Statistical Summary:")
print(df.describe())

print("\nAnalysis completed successfully!")