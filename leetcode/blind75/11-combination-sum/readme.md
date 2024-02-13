Attempt:


Recursive solution but contained duplicates, if I changed the approach to remove duplicates at the end then I would have very poor performance


Optimal (see solution in a.py):

Backtracking approach by neetcode. See iPad notes and a.py solution with comments. Fairy simple to code in the end.

General approach, if we go left in the decision tree, keep the pool of elements we can use the same, if we go right, do not use the same element we just used again.