/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

-- assemble leaderboard
-- select hacker_id, nameHacker where (acheived full score in more than one challenge)
-- order by desc total No challenges in which hacker got full score

create view extended_submissions as
select
    s.hacker_id,
    s.challenge_id,
    h.name,
    s.score,
    CASE
        WHEN (select score from difficulty d where d.difficulty_level = c.difficulty_level) = s.score THEN 1
        ELSE 0
        END AS full_marks
from submissions s
         left join challenges c on c.challenge_id = s.challenge_id
         left join hackers h on h.hacker_id = s.hacker_id;


select hacker_id, name, full_marks_count from
    (select
         e.hacker_id,
         e.name,
         sum(e.full_marks) as full_marks_count
     from extended_submissions e
     group by e.hacker_id, e.name)
where full_marks_count > 1
order by full_marks_count desc, hacker_id asc;