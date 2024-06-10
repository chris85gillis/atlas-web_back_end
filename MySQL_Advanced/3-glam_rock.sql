
-- this script will calculate the lifespan of metal bands that have a specific style
-- and sort them in descending order.
-- the lifespan is the number of years a band has been active.
-- the IFNULL function is used to get the current year if the band is still active.


SELECT band_name, IFNULL(split, 2020) - formed AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;
