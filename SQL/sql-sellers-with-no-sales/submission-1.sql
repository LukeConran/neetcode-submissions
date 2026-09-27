-- Write your query below
SELECT s.seller_name
FROM seller s
LEFT JOIN orders o ON s.seller_id = o.seller_id
GROUP BY s.seller_id, s.seller_name
HAVING COUNT(CASE WHEN EXTRACT(YEAR FROM o.sale_date) = 2020 THEN 1 END) = 0
ORDER BY seller_name ASC