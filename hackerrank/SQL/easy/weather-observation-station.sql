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