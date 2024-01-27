Initial thoughts:
- RTFQ - misunderstood that we were using a binary search tree in which nodes on the left are lower than nodes on the right
- This led to an incorrect attempt at solving.

Optimal Solution:
- Very trivial in the end
- If p and q are both left of root, recursive call to the left
- If p and q are both right of root, recursive call to the right
- If neither of the above are true then p is on one side and q is on the other
  - Therfore return current node 'root'