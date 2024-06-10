-- This SQL script shows the number of fans per country_origin for each metal band.
-- It uses a subquery to count the number of fans per band, and then groups by country_origin.
-- The result is ordered by the number of fans in descending order.


SELECT
    country_origin AS origin,
    COUNT(DISTINCT(id_fan)) AS nb_fans
FROM
    metal_bands
GROUP BY
    country_origin
ORDER BY
    nb_fans DESC;
