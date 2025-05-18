SELECT
    c1,
    c2,
    aggregate(c3)
FROM
    table_name
GROUP BY
    ROLLUP(c1, c2);
