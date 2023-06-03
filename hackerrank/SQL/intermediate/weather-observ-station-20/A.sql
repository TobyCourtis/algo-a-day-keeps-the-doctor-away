-- first attempt to get middle value of ordered table or (lowerMiddle + upperMiddle / 2)
CREATE VIEW your_view AS
SELECT ROW_NUMBER() OVER (ORDER BY LAT_N) AS row_number, LAT_N
FROM station order by LAT_N;

SELECT CASE
    WHEN mod(COUNT(*), 2) = 0 THEN
    (
        ROUND(
            (select LAT_N from your_view where row_number = FLOOR((select count(*) from your_view) / 2))
         +
         (select LAT_N from station where row_number = FLOOR((select count(*) from your_view) + 1 ))
         / 2
     , 4)
    )
    ELSE round(
            (select LAT_N from station where row_number = FLOOR((select count(*) from your_view) / 2))
        , 4)
END AS new_lat_n
FROM your_view;


-- simpler way in Oracle:
SELECT ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY LAT_N), 4) AS rounded_median FROM station;

-- OR
SELECT ROUND(MEDIAN(LAT_N), 4) AS median_rating FROM station;