
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/

-- Plan:
-- N = value of node
-- P = parent of N >> the value of

-- print node type ordered by value of the node N
-- Root: has no parent
-- Leaf: is not parent of another node
-- Inner: has parent and is parent of another node
SELECT N,
       CASE
           WHEN P IS NULL THEN 'Root'
           WHEN N IN (SELECT DISTINCT P FROM BST WHERE P IS NOT NULL) THEN 'Inner'
           ELSE 'Leaf'
           END AS node_type
FROM BST order by N;
