-- This SQL query selects the band name and calculates the lifespan of glam metal bands in the metal_bands table.
-- The lifespan is calculated by subtracting the release date from the farewell date and displaying the result as a year.
-- The result is ordered by lifespan in descending order.


SELECT band_name, IFNULL(split, 2020) - formed AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;
