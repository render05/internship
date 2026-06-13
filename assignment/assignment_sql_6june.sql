-- A1. How many unique nodes are there on the Data Bank system?

SELECT COUNT(DISTINCT node_id) AS unique_nodes
FROM customer_nodes;



-- A2. What is the number of nodes per region?

SELECT
    r.region_name,
    COUNT(DISTINCT c.node_id) AS total_nodes
FROM customer_nodes c
JOIN regions r
    ON c.region_id = r.region_id
GROUP BY r.region_name
ORDER BY r.region_name;



-- A3. How many customers are allocated to each region?

SELECT
    r.region_name,
    COUNT(DISTINCT c.customer_id) AS total_customers
FROM customer_nodes c
JOIN regions r
    ON c.region_id = r.region_id
GROUP BY r.region_name
ORDER BY r.region_name;



-- A4. How many days on average are customers reallocated to a different node?

SELECT
    ROUND(AVG(end_date - start_date), 2) AS avg_reallocation_days
FROM customer_nodes
WHERE end_date <> '9999-12-31';



-- A5. What is the median, 80th and 95th percentile for this same reallocation days metric for each region?

WITH node_days AS (
    SELECT
        region_id,
        end_date - start_date AS days_in_node
    FROM customer_nodes
    WHERE end_date <> '9999-12-31'
)
SELECT
    r.region_name,
    PERCENTILE_CONT(0.5)
        WITHIN GROUP (ORDER BY days_in_node) AS median_days,
    PERCENTILE_CONT(0.8)
        WITHIN GROUP (ORDER BY days_in_node) AS percentile_80,
    PERCENTILE_CONT(0.95)
        WITHIN GROUP (ORDER BY days_in_node) AS percentile_95
FROM node_days nd
JOIN regions r
    ON nd.region_id = r.region_id
GROUP BY r.region_name
ORDER BY r.region_name;



-- B1. What is the unique count and total amount for each transaction type?

SELECT
    txn_type,
    COUNT(*) AS transaction_count,
    SUM(txn_amount) AS total_amount
FROM customer_transactions
GROUP BY txn_type
ORDER BY txn_type;



-- B2. What is the average total historical deposit counts and amounts for all customers?

WITH customer_deposits AS (
    SELECT
        customer_id,
        COUNT(*) AS deposit_count,
        SUM(txn_amount) AS deposit_amount
    FROM customer_transactions
    WHERE txn_type = 'deposit'
    GROUP BY customer_id
)
SELECT
    ROUND(AVG(deposit_count), 2) AS avg_deposit_count,
    ROUND(AVG(deposit_amount), 2) AS avg_deposit_amount
FROM customer_deposits;



-- B3. For each month, how many Data Bank customers make more than
-- 1 deposit and either 1 purchase or 1 withdrawal in a single month?

WITH monthly_transactions AS (
    SELECT
        customer_id,
        EXTRACT(MONTH FROM txn_date) AS month_num,
        SUM(CASE WHEN txn_type = 'deposit' THEN 1 ELSE 0 END) AS deposit_count,
        SUM(CASE WHEN txn_type = 'purchase' THEN 1 ELSE 0 END) AS purchase_count,
        SUM(CASE WHEN txn_type = 'withdrawal' THEN 1 ELSE 0 END) AS withdrawal_count
    FROM customer_transactions
    GROUP BY customer_id,
             EXTRACT(MONTH FROM txn_date)
)
SELECT
    month_num,
    COUNT(*) AS customer_count
FROM monthly_transactions
WHERE deposit_count > 1
  AND (purchase_count >= 1 OR withdrawal_count >= 1)
GROUP BY month_num
ORDER BY month_num;