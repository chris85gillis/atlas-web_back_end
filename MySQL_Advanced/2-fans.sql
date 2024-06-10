-- This script ranks country origins of bands, ordered by the number of (non-unique) fans

-- Ensure the database is selected
USE metal_bands.sql;

-- Select the origin and sum of fans, grouping by origin and ordering by the sum of fans in descending order
SELECT 
    origin AS origin,
    SUM(fans) AS nb_fans 
FROM 
    metal_bands 
GROUP BY 
    origin 
ORDER BY 
    nb_fans DESC;
