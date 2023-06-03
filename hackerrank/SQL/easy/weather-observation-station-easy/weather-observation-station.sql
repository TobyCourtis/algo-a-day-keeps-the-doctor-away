/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

CREATE VIEW tmp_view AS
SELECT city, LENGTH(city) AS length_of_city FROM station;

select *
from
    ( SELECT * from tmp_view order by length_of_city asc, city asc )
where ROWNUM = 1;

select *
from
    ( SELECT * from tmp_view order by length_of_city desc, city desc )
where ROWNUM = 1;

-- alternate:
SELECT CITY, LENGTH(CITY) AS NAME_LENGTH
FROM STATION
WHERE LENGTH(CITY) IN (
    SELECT MIN(LENGTH(CITY)) AS MIN_LENGTH
    FROM STATION
    UNION ALL
    SELECT MAX(LENGTH(CITY)) AS MAX_LENGTH
    FROM STATION
)
ORDER BY NAME_LENGTH, CITY