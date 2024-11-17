SELECT a.first_name, a.last_name, a.vpa, b.got_paid - a.paid, IF(a.paid - b.got_paid >= a.credit_limit, 'YES', 'NO')
FROM
(
    SELECT a.*, SUM(b.amount) paid
    FROM user_financial_detail a
             JOIN transaction_log b ON a.vpa = b.paid_by
    GROUP BY a.vpa
) a JOIN (
    SELECT a.*, SUM(b.amount) got_paid
    FROM user_financial_detail a
             JOIN transaction_log b ON a.vpa = b.paid_to
    GROUP BY a.vpa
) b ON a.vpa = b.vpa
