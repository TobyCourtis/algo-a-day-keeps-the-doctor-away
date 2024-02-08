attempt 1:

- incorrect approach taking away from amount by the largest coin value
  - [1,2,5], amount=11
  - 11 - 5 = 6 
  - 6 - 5 = 1
  - 1 - 1 = 0
- Incorrect and wouldn't find optimal solution
- Should have tried a memoized dfs approach. Essentially brute force at each step take away each possible coin value. 
  - 11 - 1 = 10
  - 11 - 2 = 9
  - 11 - 5 = 6
    - Then for each of these subtract every coin in the list again.
    - caching ensures that we don't recompute nodes in the dfs tree twice
    - e.g remainder 3 can be 1,1,1 or 1,2. if we cache 1,2 we never compute remainder 3 again



Optimal:

- See iPad notes on dynamic programming bottom up approach
- Beat 71% runtime, 88% memory