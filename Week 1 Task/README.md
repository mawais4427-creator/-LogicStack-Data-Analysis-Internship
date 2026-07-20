# Week 1 – Retail Sales Data Cleaning & Basic Analysis in Excel

**Internship:** LogicStack Data Analysis Internship (July 2026 Cohort)
**Role:** Junior Data Analyst Intern
**Tool Used:** Microsoft Excel
**Duration:** 7 Days

## 📌 Project Overview
This project is part of Week 1 of the LogicStack Data Analysis Internship. The goal was to work with a real-world retail sales dataset in Excel — understanding its structure, cleaning and formatting it properly, running basic quality checks, calculating key metrics with formulas, applying sorting/filtering, building charts, and documenting data-driven observations.

## 📂 Dataset
- **File:** `retail_sales_dataset.csv`
- **Description:** Retail sales transaction records including Transaction ID, Date, Customer ID, Gender, Age, Product Category, Quantity, Price per Unit, and Total Amount.
- **Rows:** _[fill in]_
- **Columns:** 9

## 🛠️ Work Completed

### 1. Dataset Understanding
Documented in the **Dataset Understanding** sheet — row/column counts, data types for Date, Product Category, and Total Amount, unique product categories, and the min/max customer age.

### 2. Data Cleaning & Formatting (Cleaned Data sheet)
- Converted the data range into an Excel Table
- Bolded column headers and adjusted column widths
- Formatted the Date column as a proper date
- Formatted Price per Unit and Total Amount as currency
- Froze the top row for easier scrolling

### 3. Data Quality Check (Data Quality Check sheet)
- Checked for blank cells and duplicate rows
- Validated Quantity and Price per Unit values
- Added a **Calculated Total** column (`=Quantity * Price per Unit`)
- Added an **Amount Check** column comparing Calculated Total to Total Amount using `IF()`

### 4. Basic Analysis (Basic Analysis sheet)
Calculated using `SUM`, `AVERAGE`, `MIN`, `MAX`, and `COUNT`:

| Metric | Value |
|---|---|
| Total Sales Amount | _[fill in]_ |
| Average Sales Amount | _[fill in]_ |
| Minimum Sales Amount | _[fill in]_ |
| Maximum Sales Amount | _[fill in]_ |
| Total Quantity Sold | _[fill in]_ |
| Average Customer Age | _[fill in]_ |
| Youngest Customer Age | _[fill in]_ |
| Oldest Customer Age | _[fill in]_ |
| Total Transactions | _[fill in]_ |
| Unique Product Categories | _[fill in]_ |

Also included category-based summary tables (Sales by Product Category, Quantity Sold by Product Category, Sales by Gender) built with `SUMIF`.

### 5. Sorting & Filtering
Applied sorting and filtering in the Cleaned Data sheet to identify highest/lowest transactions, filter by Product Category (Clothing), Gender (Female), and Quantity > 2, plus full sorts by Total Amount and customer age. Screenshots are saved in the **Sorting and Filtering Screenshots** sheet.

### 6. Charts
Built in the **Charts** sheet:
- Bar chart — Total Sales by Product Category
- Column chart — Total Quantity Sold by Product Category
- Pie chart — Total Sales by Gender

### 7. Observations
Five-plus data-driven observations recorded in the **Observations** sheet, covering top/bottom performing categories, sales split by gender, average customer age, total quantity sold, and the highest transaction value.

### 8. Bonus: Age Group Segmentation
Added an **Age Group** column classifying customers as Young Adult (18–25), Adult (26–40), Senior Adult (41–60), or Older Customer (60+), with total sales broken down by group.

## 📁 Repository Structure
```
week-1-retail-sales-excel-analysis/
│
├── retail_sales_analysis.xlsx     # Completed Excel file (all 8 sheets)
├── retail_sales_dataset.csv       # Original dataset
├── screenshots/                   # Dashboard/chart screenshots
└── README.md                      # This file
```

