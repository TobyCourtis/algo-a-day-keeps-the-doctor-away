
-- determine min No. gold galleons to buy each non-evil wand of high power and age
-- select id,age, coins_needed, power order by power desc, age desc;


-- add a new field to wands "min_coins" which is the minimum value of coins_needed for the distinct pairing of code and power
-- select only the rows where min_coins = coins_needed
CREATE VIEW filtered_wands as
(select * from
    (SELECT ID, CODE, COINS_NEEDED, POWER, MIN(COINS_NEEDED) OVER (PARTITION BY CODE,POWER) AS min_coins FROM wands)
where min_coins = coins_needed);

-- get the additional fields from properties table
-- drop those evil wands
create view main_view as
(select w.id, p.age, w.coins_needed, w.power
from filtered_wands w
         left join Wands_Property p on p.code = w.code
where p.is_evil = 0);

-- do the now trivial ordering
select * from main_view
order by power desc, age desc, coins_needed asc;