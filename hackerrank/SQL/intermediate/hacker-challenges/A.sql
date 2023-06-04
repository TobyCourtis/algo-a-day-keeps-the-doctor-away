
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/

-- select hacker_id, name, (total challenger created)
-- order by total number created desc, hacker_id asc
-- if more than one student has created the same No. challenges and the count LT max(), exclude from result

-- Did not have permissions to make a view so duplicated the fetch of hackers + challenge_count 3 times.
SELECT *
FROM
    (select
         hacker_id,
         name,
         (select count(*)
          from challenges c
          where h.hacker_id = c.hacker_id
         ) as challenge_count
     from hackers h)
WHERE challenge_count = (select MAX(challenge_count) from
    (select
         hacker_id,
         name,
         (select count(*)
          from challenges c
          where h.hacker_id = c.hacker_id
         ) as challenge_count
     from hackers h)) OR
        challenge_count NOT IN (
        SELECT challenge_count FROM
            (select
                 hacker_id,
                 name,
                 (select count(*)
                  from challenges c
                  where h.hacker_id = c.hacker_id
                 ) as challenge_count
             from hackers h)
        GROUP BY challenge_count
        HAVING COUNT(*) > 1
    )
order by challenge_count desc, hacker_id asc;


