Attempt 1:

A recursive attempt:

1. at each step take either
    2. single character
    3. Two characters if `int(string[0:2]) <= 26`
2. If next char == "0", return 0
3. if len(input_string) == 0, return 1 (one more decode solution was found)

Time limit exceeded.

<br>

Attempt 2 (backtrack with caching):

Same as attempt 1 but back track such that we can cache. e.g 1 returns 1 solution, 11 returns 2 solutions.

input string '11111111' caches all strings combos in reverse order so 1, 11, 111 etc.

Runtime beat 80%, memory 81%





Neetcode:

Similar approach to mine, begins at start and either takes step 1 or step 2 if next two chars are <= 26.

It passes an index to dfs() which is used to look at current character.


A cache of previous solutions to dfs(i) is kept in dictionary dp. If dp[i] has been computed before, return the cached value.

This means we only compute the possible decode count from a specific index once. If at index 5 we've computed that there are 5 possible solutions, any other recursive calls that pass dfs(5) return the cache.


Runtime 77%, memory 83% 