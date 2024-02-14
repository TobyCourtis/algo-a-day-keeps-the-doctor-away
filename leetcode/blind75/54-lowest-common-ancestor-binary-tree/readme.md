Attempt:

Naive attempt at a nested dfs().
1. For each node, check if current node has p AND q as descendants
2. If True, output = current_node
3. If false, return output

This approach will return the last node that had p and q as descendants.

Correct approach - Time Limit Exceeded.

<br>
Attempt 2 (after reading solution algorithm):

1) For all nodes
   2) If LHS contains p or q AND RHS contains p or q then return current node
   3) if node == p or q, return node
   4) If one side contained neither, return the result of the other side

See lowestCommonAncestor() solution for simple algorithm

Beat 76% runtime, 87% memory