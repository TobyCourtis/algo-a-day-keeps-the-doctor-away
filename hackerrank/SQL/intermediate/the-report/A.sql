-- report:
-- name, grade, mark order by grade desc, name asc;
-- if grade LT 8 use "NULL" as their name and list them by their grades desc;
-- if null and grade same, order by marks;

CREATE VIEW your_view AS
select name,
       (select grade from grades g where g.min_mark <= s.marks and g.max_mark >= s.marks) as grade,
       marks
from students s;

select
    CASE
        WHEN GRADE < 8 THEN 'NULL'
        ELSE name
        END AS name_or_null,
    grade,
    marks
from your_view order by grade desc, name asc, marks asc;