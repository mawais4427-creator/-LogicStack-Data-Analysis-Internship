# Business Insights – Week 4 Funnel Analysis
**LogicStack Data Analysis Internship | July 2026**

## Insight Panel (Mandatory)

**Biggest drop-off point:** Checkout → Purchase. Of the 3,456 users who reach
checkout, only 1,004 complete a purchase — a 70.95% drop-off, the single largest
leak anywhere in the funnel.

**Best performing channel:** Google Ads. It brings in $73,862.32 in revenue from
268 purchases, more than any other channel, even though Organic brings in the most
raw traffic (Browse events).

**Most valuable user segment:** Desktop users arriving through Google Ads. Desktop
has the highest browse-to-purchase conversion rate of any device (10.58%), and
Google Ads is the top revenue channel overall — together they represent the
platform's most efficient acquisition path.

---

## 5 SQL Insights

1. **The funnel loses users at every stage, but unevenly.** Browse → Add to Cart
   loses 30.51% of users, Add to Cart → Checkout loses 50.27%, and Checkout →
   Purchase loses 70.95%. The drop-off gets worse the further users go, meaning
   the platform is best at getting people to look, and worst at getting people who
   are already at checkout to actually pay.

2. **Only 1 in 10 users who browse ever complete a purchase.** The overall
   Browse → Purchase conversion rate is 10.04% (1,004 of 10,000 users), which is
   the number to beat in future optimization work.

3. **Revenue is fairly evenly spread across channels, but Google Ads leads.**
   Google Ads ($73,862.32), Email ($69,126.46), Social Media ($68,361.24), and
   Organic ($65,973.04) are all within about $8,000 of each other, but Google Ads
   consistently comes out on top in both total revenue and purchase count (268).

4. **Desktop slightly outperforms Tablet and Mobile on conversion.** Desktop
   converts at 10.58%, Tablet at 10.06%, and Mobile at 9.47% — a gap that is small
   in percentage terms but adds up to dozens of extra purchases at this scale.

5. **South is the strongest region for revenue.** South generated $77,421.45,
   noticeably ahead of North ($68,645.13), East ($66,116.01), and West
   ($65,140.47), suggesting South-based customers or region-specific promotions
   are worth a closer look.

---

## 5 Dashboard Insights

1. The funnel chart visually confirms that the widest bar-to-bar drop happens
   between Checkout and Purchase, not earlier in the journey — this is the visual
   the whole dashboard should be read around.

2. The Revenue by Channel bar chart shows all four channels clustered closely
   together, meaning no single channel dominates — a "quick win" campaign in any
   channel is unlikely to move total revenue much on its own.

3. The Device Distribution pie chart shows purchases split almost evenly across
   Desktop, Tablet, and Mobile, so any redesign of the checkout flow needs to work
   well on all three, not just desktop.

4. The Revenue by Region column chart highlights South as a standout performer,
   useful for deciding where to prioritize regional marketing spend.

5. The revenue trend line (plotted across the purchase sequence, since the
   dataset does not contain full calendar timestamps) is essentially flat, with no
   strong upward or downward pattern — revenue generation appears stable rather
   than trending in either direction over the observed period.

---

## 3 Business Recommendations

1. **Fix the checkout experience first.** Since Checkout → Purchase is by far the
   biggest leak (70.95% drop-off), even a modest improvement here — simplifying
   payment steps, adding trust badges, reducing form fields, or offering
   guest checkout — would likely produce the largest revenue lift of any single
   change.

2. **Double down on Google Ads while testing why Organic underperforms.**
   Google Ads is the top revenue channel despite not having the most traffic,
   which suggests strong intent among paid-search visitors. Increasing Google Ads
   spend, and investigating why Organic traffic converts to revenue less
   efficiently, are both worth prioritizing.

3. **Invest further in the South region and mobile checkout.** South already
   leads on revenue and could be grown further with region-targeted promotions,
   while Mobile's lower conversion rate (9.47% vs. 10.58% on Desktop) points to an
   opportunity to streamline the mobile purchase flow specifically.
