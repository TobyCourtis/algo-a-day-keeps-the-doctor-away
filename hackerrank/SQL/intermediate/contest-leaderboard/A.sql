/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

-- total_score() = sum(max(score for each challenge))
-- select hacker_id, name, total_score()
-- where total_score > 0
-- order by total_score desc, hacker_id asc;

create view totals as
select hacker_id, sum(maximum) as total from
    (select hacker_id, challenge_id, max(score) as maximum from submissions
     group by hacker_id, challenge_id)
group by hacker_id;

select t.hacker_id, h.name, t.total from totals t
                                             join hackers h on h.hacker_id = t.hacker_id
where t.total > 0
order by t.total desc, t.hacker_id asc;
