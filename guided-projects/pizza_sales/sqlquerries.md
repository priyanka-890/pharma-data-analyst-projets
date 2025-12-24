//total revenue
# select sum(total_price::numeric) as total_revenue from pizza_sales_staging;
![alt text](image-1.png)

-- average Order Value
# select Round(sum(total_price::numeric)/count(distinct order_id),2) as avg_order_value from pizza_sales_staging
![alt text](image-2.png)

-- Total Pizzas Sold
# select sum(quantity::numeric) as Total_Pizzas_Sold from pizza_sales_staging;
![alt text](image-3.png)

-- Total Orders
# SELECT count(DISTINCT ORDER_ID::NUMERIC) AS TOTAL_ORDERS FROM PIZZA_SALES_STAGING;
![alt text](image-6.png)

-- Average Pizzas per Order
# SELECT Round(sum(QUANTITY::numeric) / COUNT(DISTINCT ORDER_ID),2) AS AVG_PIZZA_PER_ORDER FROM PIZZA_SALES_STAGING;
![alt text](image-5.png)

# Daily Trend for Total Orders
SELECT
  TO_CHAR(order_date::date, 'Day') AS day_name,
  COUNT(DISTINCT order_id) AS total_orders
FROM pizza_sales_staging
GROUP BY
  TO_CHAR(order_date::date, 'Day'),
  EXTRACT(DOW FROM order_date::date)
ORDER BY
  EXTRACT(DOW FROM order_date::date);
  ![alt text](image-7.png)

  ** You cannot use EXTRACT(DOW FROM order_date) only in ORDER BYbecause after GROUP BY, order_date no longer exists as a single value ** 







