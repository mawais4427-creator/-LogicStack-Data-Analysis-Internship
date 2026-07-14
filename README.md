# Supply Chain Performance Analysis — Week 3 Task (LogicStack Internship)

Analysis of the SCMS Delivery History Dataset (10,324 shipment records) using Python
(Pandas, Matplotlib) and Power BI.

## Files
- `supply_chain_analysis.py` — full Python script (load, clean, EDA, grouping, charts)
- `SCMS_Delivery_History_Cleaned.csv` — cleaned dataset (import this into Power BI)
- `chart1_country_vs_shipments.png` — bar chart
- `chart2_shipment_mode_distribution.png` — pie chart
- `chart3_delivery_trend.png` — line chart

## Data Cleaning Notes
- Date columns converted to `datetime` with mixed-format parsing; unparseable values
  (e.g. `"Pre-PQ Process"`, `"Date Not Captured"`) become `NaT` rather than being guessed.
- `Freight Cost (USD)`, `Weight (Kilograms)`, `Unit Price` had text placeholders
  (`"Freight Included in Commodity Cost"`, `"Weight Captured Separately"`,
  `"See ASN-93 (ID#:1281)"`) — coerced to numeric and filled with the column median.
- `Shipment Mode` missing → labeled `"Unknown"`; `Dosage` missing → `"N/A"` (not
  applicable for test kits); `Line Item Insurance` missing → filled with `0`
  (no insurance was charged on that line).

## 5 Insights from Python Analysis
1. **Air is the dominant shipment mode**, used in ~6,100 of 10,324 shipments (~59%),
   far ahead of Truck (~27%) and Ocean/Air Charter combined (<10%).
2. **South Africa, Nigeria, and Côte d'Ivoire** are the top three destination
   countries by shipment volume, together accounting for over a third of all shipments.
3. **On average, deliveries arrive ~6 days *before* the scheduled date**, meaning the
   supply chain is generally ahead of schedule; still, **11.5% of shipments (1,186)**
   were delivered late.
4. **Air Charter shipments show the largest average delay variance** (~19 days early
   on average) despite being the most expensive mode — suggesting it's used
   specifically for urgent orders, while **Ocean freight is the only mode that is late
   on average** (~5.9 days), consistent with longer transit times.
5. **ARV (antiretroviral) products dominate total line item value** (~$1.41B), more
   than 6x the next-largest category (HRDT, ~$213M), showing the dataset is heavily
   weighted toward HIV/AIDS treatment supply chains.

## 3 Insights from Power BI Dashboard *(fill in after building your dashboard)*
1. _e.g. "Total Freight Cost of $93M is concentrated in a handful of vendors — SCMS from RDC alone accounts for over half."_
2. _e.g. "The delivery trend line shows shipment volume peaked in [month/year] and declined afterward."_
3. _e.g. "[Top country] consistently shows the lowest average delay, making it the most reliable delivery destination."_

## 2 Business Recommendations
1. **Consolidate freight spend with top-performing vendors** (e.g., SCMS from RDC,
   Orgenics) and renegotiate rates, since a small group of vendors drives the majority
   of freight cost.
2. **Shift more Ocean-bound shipments to advance planning or Truck/Air alternatives**,
   since Ocean is the only mode that is late on average — better lead-time buffers or
   mode selection could reduce the 11.5% delayed-shipment rate.

---

## Part 2: Power BI Dashboard (build locally)
1. Open Power BI Desktop → **Get Data → Text/CSV** → import `SCMS_Delivery_History_Cleaned.csv`.
2. Create KPI cards: **Total Shipments**, **Total Freight Cost**, **Average Delivery
   Delay**, **Total Line Item Value** (use `COUNTROWS`, `SUM`, `AVERAGE` DAX measures).
3. Add the required visuals: Bar (Country vs Shipments), Line (Delivery trend over
   time using `Delivered to Client Date`), Pie (Shipment Mode), Column (Vendor vs
   Total Cost).
4. Add a KPI Insight Panel with text cards for: average delay status, cost efficiency
   insight, top performing country.
5. Keep the layout clean, use one consistent color theme, and title every visual.

## Submission Checklist
- [ ] GitHub repository is public
- [ ] README (this file) filled in with your own Power BI insights and observations
- [ ] LinkedIn post includes GitHub project link and mentions LogicStack
- [ ] All 5 tasks (Python) + dashboard (Power BI) completed, nothing left incomplete
