# Retail Sales Analysis — LogicStack Data Analysis Internship

This repository contains my work for the Data Analysis Internship at **LogicStack** (July 2026), analyzing a 1,000-row retail sales dataset using Excel and Power BI.

## 📁 Dataset

`retail_sales_dataset.csv` — 1,000 retail transactions with the following fields:
Transaction ID, Date, Customer ID, Gender, Age, Product Category, Quantity, Price per Unit, Total Amount

## 🗂️ Repository Structure

```
├── retail_sales_dataset.csv
├── Week2_Retail_Sales_Analysis.xlsx     # Raw Data, Pivot Tables, KPI Summary, Insights
├── powerbi_dashboard.png                # Power BI dashboard screenshot
└── README.md
```

---

## Week 1 — Excel Fundamentals

Performed an initial exploratory analysis of the dataset in Excel:
- Applied core formulas (SUM, AVERAGE, COUNT, MIN, MAX) to summarize sales data
- Built basic charts to visualize sales patterns
- Uploaded findings to GitHub and shared progress on LinkedIn

---

## Week 2 — Advanced Excel Analysis + Power BI Dashboard

**Tools used:** Microsoft Excel, Power BI
**Duration:** 7 Days

### Task 1: Pivot Tables

Built four pivot tables in Excel:

| Analysis | Result |
|---|---|
| Total Sales by Product Category | Electronics: 156,905 · Clothing: 155,580 · Beauty: 143,515 |
| Total Sales by Gender | Female: 232,840 · Male: 223,160 |
| Total Quantity by Product Category | Clothing: 894 · Electronics: 849 · Beauty: 771 |
| Average Age by Product Category | Clothing: 42.0 · Electronics: 41.7 · Beauty: 40.4 |

### Task 2: KPI Calculations

| KPI | Value |
|---|---|
| Total Sales | 456,000 |
| Total Transactions | 1,000 |
| Average Sales | 456.00 |
| Total Quantity Sold | 2,514 |
| Highest Transaction Value | 2,000 |
| Lowest Transaction Value | 25 |

### Task 3: Insights

- Electronics is the strongest category by revenue (156,905), narrowly ahead of Clothing (155,580) and Beauty (143,515) — even though Clothing sells the most units, meaning Electronics carries a higher price point per item.
- Spending is fairly balanced across gender, with Female customers slightly ahead (232,840) of Male customers (223,160).
- Average customer age is highest among Clothing buyers (~42) and lowest among Beauty buyers (~40).
- Transaction values range widely, from 25 to 2,000, showing a mix of small and large purchases.
- The average basket size is about 2.5 items per transaction across the dataset.

### Task 4: Power BI Dashboard

Built an interactive one-page dashboard following the top-to-bottom KPI → Analysis → Trend layout:

- **KPI Cards (top row):** Total Sales, Total Transactions, Total Quantity Sold, Average Sales
- **Analysis (middle row):** Bar chart — Sales by Product Category · Pie chart — Sales by Gender · Column chart — Quantity Sold by Category
- **Trend (bottom row):** Line chart — Sales Trend by Date
- **Slicers:** Gender, Product Category, Age Group

![Power BI Dashboard](powerbi_dashboard.png)

---

## 🔧 Tools & Skills Demonstrated

- Excel: SUMIF, AVERAGEIF, pivot tables, KPI design
- Power BI: data modeling, DAX measures, dashboard design, slicers
- Business analysis: category performance, customer segmentation, trend analysis

## 📌 About This Internship

This project is part of the LogicStack Data Analysis Internship (July 2026), a weekly-task-based program building practical data analyst skills from Excel fundamentals through to interactive BI dashboards.
