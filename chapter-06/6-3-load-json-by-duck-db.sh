duckdb -c "                      
SELECT product, SUM(quantity * price) AS total_sales
FROM read_json_auto('sales.json')
GROUP BY product;"
