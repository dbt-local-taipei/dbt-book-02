SELECT
  *
FROM
  (
    SELECT
      country,
      city,
      population,
      row_number() OVER (
        PARTITION BY country
        ORDER BY
          population desc
      ) AS country_rank
    FROM
      cities
  ) ranks
WHERE
  country_rank <= 3;
