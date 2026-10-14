-- Write your query below
SELECT s.seller_name
FROM seller as s
LEFT JOIN orders as o 
on s.seller_id = o.seller_id
and o.sale_date >= '2020-01-01'
and o.sale_date < '2021-01-01'
WHERE o.order_id is NULL
order by s.seller_name ASC;