-- write your code in PostgreSQL 9.4
SELECT plays.id, plays.title, COALESCE(SUM(reservations.number_of_tickets), 0) AS reserved_tickets
FROM plays
         LEFT JOIN reservations ON plays.id = reservations.play_id
GROUP BY plays.id, plays.title
ORDER BY reserved_tickets DESC, id ASC
