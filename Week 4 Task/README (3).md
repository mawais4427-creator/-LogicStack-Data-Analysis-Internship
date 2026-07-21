# Week 4 Final Project – Funnel Analysis (SQL + Power BI)
**LogicStack Data Analysis Internship | July 2026**

## Overview
This project analyzes user behavior on a digital platform using a client-side event
tracking dataset (21,409 events / 10,000 users / 10,000 sessions). The goal is to
understand how users move through the conversion funnel, identify where they drop
off, and generate business recommendations using SQL and Power BI.

## Tools Used
- MySQL (data exploration, funnel analysis, revenue analysis)
- Power BI (interactive dashboard)

## Dataset
`client_site_dataset.csv` — 10 columns: User ID, Session ID, Event Time, Event,
Device, Region, Channel, Product Category, Revenue, Bonus Flag.

The funnel in this dataset has 4 recorded stages: **Browse → Add to Cart →
Checkout → Purchase**.

## Funnel Results

| Stage | Users | Stage Conversion | Drop-off |
|---|---|---|---|
| Browse | 10,000 | — | — |
| Add to Cart | 6,949 | 69.49% | 30.51% |
| Checkout | 3,456 | 49.73% | 50.27% |
| Purchase | 1,004 | 29.05% | 70.95% |

**Overall Browse → Purchase conversion: 10.04%**

## Key Findings
- **Biggest drop-off point:** Checkout → Purchase (70.95% of users who reach
  checkout never complete a purchase). This is the single largest leak in the funnel.
- **Best performing channel:** Google Ads, generating $73,862.32 in revenue from
  268 purchases — the highest of all four channels.
- **Highest revenue region:** South ($77,421.45).
- **Device with highest conversion rate:** Desktop (10.58%), narrowly ahead of
  Tablet (10.06%) and Mobile (9.47%).
- **Total revenue:** $277,323.06 across 1,004 purchases.

## Repository Contents
- `funnel_analysis_queries.sql` — all SQL queries (data exploration, funnel
  analysis, revenue analysis, business insights, drop-off analysis)
- `client_site_dataset_PowerBI_ready.csv` — cleaned dataset for Power BI import
- `business_insights.md` — 5 SQL insights, 5 dashboard insights, 3 business
  recommendations
- `powerbi_dashboard_guide.md` — step-by-step instructions to rebuild the dashboard
- `README.md` — this file

## Dashboard
The Power BI dashboard includes:
- KPI cards: Total Users, Total Revenue, Total Events, Total Purchases
- Funnel chart (main visual): Browse → Add to Cart → Checkout → Purchase
- Bar chart: Revenue by Channel
- Column chart: Revenue by Region
- Pie chart: Device Distribution
- Line chart: Revenue trend across the purchase sequence

## Author
Awais — Junior Data Analyst, LogicStack Internship (July 2026 cohort)
