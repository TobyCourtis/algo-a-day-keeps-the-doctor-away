Attempt:

1. if root is None then return the depth
2. return max(self(root.left, depth + 1), self(root.right, depth + 1))

 
<br>
Initially was confused in implementation around how to recursively return the end depth.


- max(left, right) will return:
- max(max(left, right), max(left, right)) L
- Which ultimately returns the maximum of all depths in tree

Submission:
Beat 54% runtime, 71% memory

Optimal:
Mine was optimal

