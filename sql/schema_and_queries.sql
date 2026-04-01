-- schema_and_queries.sql
-- Maak tabel customers en voorbeeld queries

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  signup_date TEXT, -- ISO-YYYY-MM-DD
  country TEXT,
  spend REAL
);

-- Voorbeeld queries:
-- 1) alle klanten uit Nederland (NL)
SELECT * FROM customers WHERE country = 'NL';

-- 2) totale bestede per land
SELECT country, SUM(spend) AS total_spend, COUNT(*) AS customers
FROM customers
GROUP BY country
ORDER BY total_spend DESC;

-- 3) klanten met spend > 100
SELECT id, first_name, last_name, email, spend
FROM customers
WHERE spend > 100
ORDER BY spend DESC;

