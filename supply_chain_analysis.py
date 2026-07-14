"""
LogicStack Data Analysis Internship - Week 3 Task
Supply Chain Analytics Challenge (Part 1: Python)
Dataset: SCMS_Delivery_History_Dataset.csv
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
plt.rcParams["figure.dpi"] = 110

# ----------------------------------------------------------------------
# TASK 1: LOAD DATASET
# ----------------------------------------------------------------------
df = pd.read_csv("SCMS_Delivery_History_Dataset.csv", sep="\t")

print("=" * 60)
print("TASK 1: LOAD DATASET")
print("=" * 60)
print("\nFirst 10 rows:\n", df.head(10))
print("\nShape:", df.shape)
print("\nColumns:\n", df.columns.tolist())

# ----------------------------------------------------------------------
# TASK 2: DATA CLEANING
# ----------------------------------------------------------------------
print("\n" + "=" * 60)
print("TASK 2: DATA CLEANING")
print("=" * 60)

# 2.1 Convert date columns to datetime (mixed formats -> errors='coerce')
date_cols = [
    "PQ First Sent to Client Date",
    "PO Sent to Vendor Date",
    "Scheduled Delivery Date",
    "Delivered to Client Date",
    "Delivery Recorded Date",
]
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce", format="mixed")

# 2.2 Identify missing values
print("\nMissing values before cleaning:\n", df.isna().sum()[df.isna().sum() > 0])

# 2.3 Convert numeric-looking text columns, coercing non-numeric labels
#     (e.g. "Freight Included in Commodity Cost", "Weight Captured Separately")
#     to NaN, then fill with the column median.
numeric_text_cols = ["Freight Cost (USD)", "Weight (Kilograms)", "Unit Price"]
for col in numeric_text_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    median_val = df[col].median()
    df[col] = df[col].fillna(median_val)

# 2.4 Handle remaining missing values
#     - Shipment Mode: unknown category -> "Unknown"
#     - Dosage: not applicable for many items -> "N/A"
#     - Line Item Insurance: not always charged -> fill with 0
#     - Dates that failed to parse (e.g. "Pre-PQ Process") -> leave as NaT (not usable)
df["Shipment Mode"] = df["Shipment Mode"].fillna("Unknown")
df["Dosage"] = df["Dosage"].fillna("N/A")
df["Line Item Insurance (USD)"] = df["Line Item Insurance (USD)"].fillna(0)

print("\nMissing values after cleaning:\n", df.isna().sum()[df.isna().sum() > 0])

# ----------------------------------------------------------------------
# TASK 3: EXPLORATORY DATA ANALYSIS (EDA)
# ----------------------------------------------------------------------
print("\n" + "=" * 60)
print("TASK 3: EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# --- Shipment Analysis ---
most_common_mode = df["Shipment Mode"].mode()[0]
shipments_per_country = df["Country"].value_counts()

print("\nMost common shipment mode:", most_common_mode)
print("\nTotal shipments per country (top 10):\n", shipments_per_country.head(10))

# --- Delivery Performance ---
df["Delivery Delay (Days)"] = (
    df["Delivered to Client Date"] - df["Scheduled Delivery Date"]
).dt.days

avg_delivery_delay = df["Delivery Delay (Days)"].mean()
delayed_shipments = df[df["Delivery Delay (Days)"] > 0]

print(f"\nAverage delivery delay: {avg_delivery_delay:.2f} days")
print(f"Number of delayed shipments: {len(delayed_shipments)} "
      f"({len(delayed_shipments)/len(df)*100:.1f}% of total)")

# --- Cost Analysis ---
total_freight_cost = df["Freight Cost (USD)"].sum()
avg_line_item_value = df["Line Item Value"].mean()
total_insurance_cost = df["Line Item Insurance (USD)"].sum()

print(f"\nTotal Freight Cost: ${total_freight_cost:,.2f}")
print(f"Average Line Item Value: ${avg_line_item_value:,.2f}")
print(f"Total Insurance Cost: ${total_insurance_cost:,.2f}")

# ----------------------------------------------------------------------
# TASK 4: GROUP-BASED ANALYSIS
# ----------------------------------------------------------------------
print("\n" + "=" * 60)
print("TASK 4: GROUP-BASED ANALYSIS")
print("=" * 60)

country_shipments = df.groupby("Country").size().sort_values(ascending=False)
vendor_cost = df.groupby("Vendor")["Freight Cost (USD)"].sum().sort_values(ascending=False)
product_group_value = df.groupby("Product Group")["Line Item Value"].sum().sort_values(ascending=False)
shipment_mode_delay = df.groupby("Shipment Mode")["Delivery Delay (Days)"].mean().sort_values(ascending=False)

print("\nCountry vs Total Shipments (top 5):\n", country_shipments.head())
print("\nVendor vs Total Cost (top 5):\n", vendor_cost.head())
print("\nProduct Group vs Total Value:\n", product_group_value)
print("\nShipment Mode vs Average Delay:\n", shipment_mode_delay)

# ----------------------------------------------------------------------
# TASK 5: VISUALIZATIONS
# ----------------------------------------------------------------------
print("\n" + "=" * 60)
print("TASK 5: VISUALIZATIONS")
print("=" * 60)

# 1. Bar chart: Country vs Shipments (Top 10)
plt.figure(figsize=(10, 6))
country_shipments.head(10).plot(kind="bar", color="#4C72B0")
plt.title("Top 10 Countries by Total Shipments")
plt.xlabel("Country")
plt.ylabel("Number of Shipments")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("chart1_country_vs_shipments.png")
plt.close()

# 2. Pie chart: Shipment Mode distribution
plt.figure(figsize=(7, 7))
df["Shipment Mode"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", startangle=90
)
plt.title("Shipment Mode Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("chart2_shipment_mode_distribution.png")
plt.close()

# 3. Line chart: Delivery trend over time (monthly shipment volume)
monthly_trend = (
    df.dropna(subset=["Delivered to Client Date"])
    .set_index("Delivered to Client Date")
    .resample("ME")
    .size()
)
plt.figure(figsize=(12, 6))
monthly_trend.plot(kind="line", color="#DD8452")
plt.title("Delivery Trend Over Time (Monthly)")
plt.xlabel("Month")
plt.ylabel("Number of Deliveries")
plt.tight_layout()
plt.savefig("chart3_delivery_trend.png")
plt.close()

print("\nCharts saved: chart1_country_vs_shipments.png, "
      "chart2_shipment_mode_distribution.png, chart3_delivery_trend.png")

# ----------------------------------------------------------------------
# EXPORT CLEANED DATASET (for Power BI - Part 2)
# ----------------------------------------------------------------------
df.to_csv("SCMS_Delivery_History_Cleaned.csv", index=False)
print("\nCleaned dataset exported: SCMS_Delivery_History_Cleaned.csv")
