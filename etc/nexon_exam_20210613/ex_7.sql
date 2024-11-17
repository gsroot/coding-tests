SELECT c.country_name, b.city_name, a.count
FROM
(
    SELECT city_id, count
    FROM
    (
        SELECT city_id, COUNT(*) count
        FROM customer
        GROUP BY city_id
    ) a
    WHERE count > (
        SELECT AVG(count) avg_count
        FROM
        (
            SELECT city_id, COUNT(*) count
            FROM customer
            GROUP BY city_id
        ) a
    )
) a JOIN city b ON a.city_id = b.id
JOIN country c ON b.country_id = c.id
ORDER BY c.country_name ASC