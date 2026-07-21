CREATE DATABASE logicstack_week4;
USE logicstack_week4;
CREATE DATABASE logicstack_week4;
USE logicstack_week4;

CREATE TABLE client_site_dataset (
    User_ID VARCHAR(20),
    Session_ID VARCHAR(20),
    Event_Time VARCHAR(20),
    Event VARCHAR(30),
    Device VARCHAR(20),
    Region VARCHAR(20),
    Channel VARCHAR(30),
    Product_Category VARCHAR(30),
    Revenue DECIMAL(10,2),
    Bonus_Flag VARCHAR(5)
);
select * from client_site_dataset;


--                                    Data_Exploration

-- 1. Total rows in dataset

SELECT COUNT(*) FROM client_site_dataset;

-- 2. Unique users
SELECT COUNT(DISTINCT `User_ID`) AS Unique_Users FROM client_site_dataset;

-- 3. Unique sessions
SELECT COUNT(DISTINCT `Session_ID`) AS Unique_Sessions FROM client_site_dataset;

-- 4. List all event types
SELECT DISTINCT `Event` FROM client_site_dataset;

---                             Funnel Stage Analysis 

-- 1. Count total events by type
SELECT `Event`, COUNT(*) AS Total_Events
FROM client_site_dataset
GROUP BY `Event`
ORDER BY Total_Events DESC;

-- 2. Count users per event type
SELECT `Event`, COUNT(DISTINCT `User_ID`) AS Unique_Users
FROM client_site_dataset
GROUP BY `Event`
ORDER BY Unique_Users DESC;

-- 3. Conversion from Browse → Purchase
SELECT 
    (SELECT COUNT(DISTINCT `Session_ID`) FROM client_site_dataset WHERE `Event`='Browse') AS Browsed,
    (SELECT COUNT(DISTINCT `Session_ID`) FROM client_site_dataset WHERE `Event`='Purchase') AS Purchased,
    ROUND((SELECT COUNT(DISTINCT `Session_ID`) FROM client_site_dataset WHERE `Event`='Purchase')*100.0
    /(SELECT COUNT(DISTINCT `Session_ID`) FROM client_site_dataset WHERE `Event`='Browse'), 2) AS Conversion_Rate;
    
 ---                            Revenue Analysis
    
    -- 1. Total revenue
SELECT SUM(Revenue) AS Total_Revenue FROM client_site_dataset;

-- 2. Revenue by region
SELECT Region, SUM(Revenue) AS Total_Revenue
FROM client_site_dataset GROUP BY Region ORDER BY Total_Revenue DESC;

-- 3. Revenue by channel
SELECT Channel, SUM(Revenue) AS Total_Revenue
FROM client_site_dataset GROUP BY Channel ORDER BY Total_Revenue DESC;
    
    -- 4. Revenue by device
SELECT Device, SUM(Revenue) AS Total_Revenue
FROM client_site_dataset GROUP BY Device ORDER BY Total_Revenue DESC;

---                         Business Insights Queries


 ---     Top 5 users by revenue
SELECT `User_ID`, SUM(Revenue) AS Total_Revenue
FROM client_site_dataset
GROUP BY `User_ID`
ORDER BY Total_Revenue DESC
LIMIT 5;
    
   ---  Best performing channel
   SELECT Channel, SUM(Revenue) AS Total_Revenue
FROM client_site_dataset
GROUP BY Channel
ORDER BY Total_Revenue DESC
LIMIT 1;

---    Highest revenue region
SELECT Region, SUM(Revenue) AS Total_Revenue
FROM client_site_dataset
GROUP BY Region
ORDER BY Total_Revenue DESC
LIMIT 1;

---  Device with highest conversion rate
SELECT 
    Device,
    COUNT(DISTINCT `Session_ID`) AS Total_Sessions,
    COUNT(DISTINCT CASE WHEN `Event`='Purchase' THEN `Session_ID` END) AS Purchase_Sessions,
    ROUND(COUNT(DISTINCT CASE WHEN `Event`='Purchase' THEN `Session_ID` END)*100.0
    / COUNT(DISTINCT `Session_ID`), 2) AS Conversion_Rate_Percent
FROM client_site_dataset
GROUP BY Device
ORDER BY Conversion_Rate_Percent DESC;

---                                     --Drop off Analysis 

 --- Count sessions reaching each funnel stage
 
 SELECT `Event`, COUNT(DISTINCT `Session_ID`) AS Sessions_Reached
FROM client_site_dataset
GROUP BY `Event`
ORDER BY FIELD(`Event`, 'Browse', 'Add to Cart', 'Checkout', 'Purchase');

---    Find event type with lowest conversion

SELECT 
    `Event`,
    COUNT(DISTINCT `Session_ID`) AS Sessions,
    ROUND(COUNT(DISTINCT `Session_ID`)*100.0 
    / (SELECT COUNT(DISTINCT `Session_ID`) FROM client_site_dataset WHERE `Event`='Browse'), 2) AS Percent_of_Browsers
FROM client_site_dataset
GROUP BY `Event`
ORDER BY Percent_of_Browsers ASC;


    
    
    
    
    
    
    
    
    
    
    