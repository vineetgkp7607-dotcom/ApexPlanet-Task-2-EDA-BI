-- ApexPlanet Task 2: EDA and Business Intelligence
-- Database: apexplanet_eda
-- Table: sales_data

USE apexplanet_eda;


-- 1. Overall Sales Summary
SELECT
    COUNT(*) AS Total_Orders,
    SUM(Total_Sales) AS Total_Revenue,
    AVG(Total_Sales) AS Average_Order_Value
FROM sales_data;


-- 2. Category-wise Sales
SELECT
    Category,
    SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY Category
ORDER BY Total_Sales DESC;


-- 3. City-wise Sales
SELECT
    City,
    SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY City
ORDER BY Total_Sales DESC;


-- 4. Product-wise Sales
SELECT
    Product,
    SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY Product
ORDER BY Total_Sales DESC;


-- 5. Monthly Sales Trend
SELECT
    DATE_FORMAT(Order_Date, '%Y-%m') AS Sales_Month,
    SUM(Total_Sales) AS Monthly_Sales
FROM sales_data
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY Sales_Month;


-- 6. Gender-wise Sales
SELECT
    Gender,
    COUNT(*) AS Total_Orders,
    SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY Gender;


-- 7. Category-wise Order Count
SELECT
    Category,
    COUNT(*) AS Total_Orders,
    SUM(Quantity) AS Total_Quantity,
    SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY Category
ORDER BY Total_Sales DESC;


-- 8. Top 10 Highest-value Orders
SELECT
    Order_ID,
    Order_Date,
    Customer_ID,
    City,
    Product,
    Quantity,
    Total_Sales
FROM sales_data
ORDER BY Total_Sales DESC
LIMIT 10;


-- 9. City-wise Order Analysis
SELECT
    City,
    COUNT(*) AS Total_Orders,
    SUM(Quantity) AS Total_Quantity,
    ROUND(AVG(Total_Sales), 2) AS Average_Order_Value,
    SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY City
ORDER BY Total_Sales DESC;


-- 10. Category-wise Sales by Gender
SELECT
    Category,
    Gender,
    COUNT(*) AS Total_Orders,
    SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY Category, Gender
ORDER BY Category, Gender;


-- 11. Age Group Sales
SELECT
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        WHEN Age BETWEEN 46 AND 55 THEN '46-55'
        ELSE '56-65'
    END AS Age_Group,
    COUNT(*) AS Total_Orders,
    SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY Age_Group
ORDER BY Age_Group;


-- 12. Quantity Analysis
SELECT
    Quantity,
    COUNT(*) AS Total_Orders,
    SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY Quantity
ORDER BY Quantity;


-- 13. Data Validation
SELECT
    COUNT(*) AS Total_Rows,
    SUM(CASE WHEN Order_ID IS NULL THEN 1 ELSE 0 END) AS Missing_Order_ID,
    SUM(CASE WHEN Order_Date IS NULL THEN 1 ELSE 0 END) AS Missing_Order_Date,
    SUM(CASE WHEN Customer_ID IS NULL THEN 1 ELSE 0 END) AS Missing_Customer_ID,
    SUM(CASE WHEN Age IS NULL THEN 1 ELSE 0 END) AS Missing_Age,
    SUM(CASE WHEN City IS NULL THEN 1 ELSE 0 END) AS Missing_City,
    SUM(CASE WHEN Product IS NULL THEN 1 ELSE 0 END) AS Missing_Product,
    SUM(CASE WHEN Total_Sales IS NULL THEN 1 ELSE 0 END) AS Missing_Total_Sales
FROM sales_data;


-- 14. Data Quality Check
SELECT
    COUNT(*) AS Total_Rows,
    SUM(CASE WHEN Quantity <= 0 THEN 1 ELSE 0 END) AS Invalid_Quantity,
    SUM(CASE WHEN Unit_Price <= 0 THEN 1 ELSE 0 END) AS Invalid_Unit_Price,
    SUM(CASE WHEN Total_Sales <= 0 THEN 1 ELSE 0 END) AS Invalid_Total_Sales,
    SUM(CASE WHEN Order_Date IS NULL THEN 1 ELSE 0 END) AS Missing_Order_Date
FROM sales_data;


-- 15. Top 10 Customers by Sales
SELECT
    Customer_ID,
    Customer_Name,
    COUNT(*) AS Total_Orders,
    SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY Customer_ID, Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;


-- 16. Product Quantity and Average Sales
SELECT
    Product,
    SUM(Quantity) AS Total_Quantity,
    COUNT(*) AS Total_Orders,
    ROUND(AVG(Total_Sales), 2) AS Average_Sales,
    ROUND(SUM(Total_Sales), 2) AS Total_Sales
FROM sales_data
GROUP BY Product
ORDER BY Total_Sales DESC;


-- 17. Repeat Customer Analysis
SELECT
    CASE
        WHEN Order_Count = 1 THEN 'One-Time Customer'
        ELSE 'Repeat Customer'
    END AS Customer_Type,
    COUNT(*) AS Total_Customers,
    SUM(Order_Count) AS Total_Orders
FROM (
    SELECT
        Customer_ID,
        COUNT(*) AS Order_Count
    FROM sales_data
    GROUP BY Customer_ID
) AS Customer_Orders
GROUP BY Customer_Type;