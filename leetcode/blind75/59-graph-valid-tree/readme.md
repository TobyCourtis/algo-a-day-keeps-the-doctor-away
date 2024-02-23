Attempt:

attempted looping through all siblings of siblings and making sure none of them were connected.

E.g If 0 -> 1 and 2, none of 1's siblings or 2's siblings can be connected OR connected back to 0.

Code was too complex, time limit exceeded.

<br>

Neetcode (O(E + V)):

DFS() visit all siblings of current node, if we visit the same node twice then we have a loop and return False. Also we
must verify we have a connected graph so len(visited) == n must be true.

1. Build node value : set(siblings) list. e.g 0: {1, 2 , 3}
2. dfs(), ensuring if we visit a node we do not immediately go back to the node we just came from
    3. append current value to visited
    4. dfs for all siblings of current node
    5. if value already in visited - return False (loop)
3. Return True if no loops at the end of dfs()
4. return dfs() and len(visited) == n

Could not run as leetcode premium problem.