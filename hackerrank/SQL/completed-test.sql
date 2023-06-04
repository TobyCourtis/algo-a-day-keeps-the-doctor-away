SET NULL "NULL";
SET FEEDBACK OFF;
SET ECHO OFF;
SET HEADING OFF;
SET WRAP OFF;
SET LINESIZE 10000;
SET TAB OFF;
SET PAGES 0;
SET DEFINE OFF;
SET SERVEROUTPUT ON;


/*
    Enter your query below and follow these instructions:
    1. Please append a semicolon ";" at the end of the query
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
*/



-- find pairs of customers and agents who have been in contact more than once

-- for each pair:
-- select user_account.id, user_account.first_name, user_account.last_name, customer.id, customer.customer_name, NO_contact_times()
-- order by user_account.id asc;

-- (userID, customerID) = pair
create view tmp_view as
select user_account_id, customer_id, contact_times from
    (select c.user_account_id, c.customer_id, count(*) as contact_times
     from contact c
     group by c.user_account_id, c.customer_id)
where contact_times > 1;

select t.user_account_id, u.first_name, u.last_name, t.customer_id, c.customer_name, t.contact_times
from tmp_view t
         left join user_account u on u.id = t.user_account_id
         left join customer c on c.id = t.customer_id
order by t.contact_times asc;






exit;
    


-- 2nd question
SET NULL "NULL";
SET FEEDBACK OFF;
SET ECHO OFF;
SET HEADING OFF;
SET WRAP OFF;
SET LINESIZE 10000;
SET TAB OFF;
SET PAGES 0;
SET DEFINE OFF;
SET SERVEROUTPUT ON;

/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/

-- for each country c:
-- c.country_name, total_no_invoices(), avg(round(total_price, 6)),

-- return only countries where avg invoice is GT avg_invoice across ALL invoices.

create view tmp_view as
(select i.id, i.total_price, co.country_name from invoice i
                                                      left join customer cu on cu.id = i.customer_id
                                                      left join city ci on ci.id = cu.city_id
                                                      left join country co on co.id = ci.country_id);


select country_name, total, TO_CHAR(avg_amount, 'FM9999999999999990.000000') from
    (select country_name, count(*) as total, round(sum(total_price) / count(*), 6) as avg_amount
     from tmp_view t
     group by country_name)
where avg_amount > (select sum(total_price) / count(*) from tmp_view t2 where t2.country_name = country_name);

exit;