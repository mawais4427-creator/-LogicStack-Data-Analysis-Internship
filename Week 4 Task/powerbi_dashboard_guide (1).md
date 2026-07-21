# Power BI Dashboard Build Guide – Week 4 Funnel Analysis

Use `client_site_dataset_PowerBI_ready.csv` as your data source (Get Data → Text/CSV).

## Step 1 — Load & check data types
- User ID, Session ID, Event, Device, Region, Channel, Product Category, Bonus Flag → Text
- Revenue → Decimal Number
- Event Time → Text (this dataset only stores mm:ss, not a full date/time, so don't
  convert it to a Date type — it will error or misparse)

## Step 2 — Create measures (DAX)
```
Total Users = DISTINCTCOUNT('client_site_dataset'[User ID])

Total Events = COUNTROWS('client_site_dataset')

Total Purchases = CALCULATE(COUNTROWS('client_site_dataset'), 'client_site_dataset'[Event] = "Purchase")

Total Revenue = CALCULATE(SUM('client_site_dataset'[Revenue]), 'client_site_dataset'[Event] = "Purchase")
```
Expected values to check against: Total Users = 10,000 | Total Events = 21,409 |
Total Purchases = 1,004 | Total Revenue = $277,323.06

## Step 3 — KPI Cards (top of dashboard)
Add 4 Card visuals using the measures above: Total Users, Total Revenue,
Total Events, Total Purchases.

## Step 4 — Funnel Chart (main visual)
- Visual: Funnel
- Category: Event
- Values: Count of User ID (distinct)
- **Important:** the funnel order must be manually sorted to
  Browse → Add to Cart → Checkout → Purchase (Power BI will otherwise sort
  alphabetically). Right-click the Event field → Sort by Column, or add a
  helper column: `Stage Order = SWITCH('client_site_dataset'[Event], "Browse",1,
  "Add to Cart",2, "Checkout",3, "Purchase",4)` and sort Event by Stage Order.
- Expected bars: 10,000 → 6,949 → 3,456 → 1,004

## Step 5 — Bar Chart: Revenue by Channel
- Visual: Bar chart (horizontal)
- Axis: Channel | Values: Total Revenue measure
- Filter: Event = Purchase
- Expected order: Google Ads ($73,862) > Email ($69,126) > Social Media ($68,361)
  > Organic ($65,973)

## Step 6 — Column Chart: Revenue by Region
- Visual: Column chart
- Axis: Region | Values: Total Revenue measure
- Filter: Event = Purchase
- Expected order: South ($77,421) > North ($68,645) > East ($66,116) > West ($65,140)

## Step 7 — Pie Chart: Device Distribution
- Visual: Pie chart
- Legend: Device | Values: Count of Event (or Total Users)
- Use the full dataset (not filtered to Purchase) to show overall device split,
  or filter to Purchase to show device split of buyers specifically — decide
  based on whether you want traffic mix or buyer mix.

## Step 8 — Line Chart: Revenue Trend
- The dataset's Event Time field is only mm:ss (no date), so a true calendar
  trend isn't possible here. Two options:
  - Add an Index column in Power Query (over the Purchase rows in file order)
    and plot Revenue against that index to show a sequence trend.
  - Alternatively, extract the "seconds" component of Event Time and bucket into
    minute-of-hour groups to show an intraday pattern.
  - Either way, note in your dashboard that this is a proxy trend, not a true
    date-based one — mention this in your README so reviewers aren't confused
    by the axis.

## Step 9 — Insight Panel (Text Box, mandatory)
Add a text box with the 3 required lines — copy from `business_insights.md`:
- Biggest drop-off point: Checkout → Purchase (70.95%)
- Best performing channel: Google Ads
- Most valuable user segment: Desktop users via Google Ads

## Step 10 — Polish & publish
- Apply a consistent theme/color palette.
- Add slicers for Region, Channel, and Device so the dashboard is interactive.
- Save as .pbix, then export to PDF for your GitHub repo if a static preview is needed.
