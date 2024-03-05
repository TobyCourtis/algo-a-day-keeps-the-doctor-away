attempt:

naive:

1. For each node in tree, do dfs()
2. If we hit a negative we can either 
   1. start again from LHS
   2. start again from RHS
   3. Continue with negative in the path
   4. End without including the negative result
3. Save max result



Neetcode (O(n) dfs):

1. dfs through each node
   1. return max(left, right side, 0)  # 0 is the case both left and right are negative so we would take neither
   2. maximum = max(maximum, left + cur + right)  # case we want to set maximum in case current subtree is maximal. Imagine the parents of cur are all negative so we want to capture the current maximal subtree.
2. Return maximum


See code for simple breakdown. Fairly intuitive problem. 


Runtime beat 59%, memory 83%
