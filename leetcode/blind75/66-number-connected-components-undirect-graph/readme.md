Attempt:

1. For each node
2. Add all neighbors to current visited set
3. Do this recursively for all neighbor's neighbors (dfs())

NB:
- Increment connected component count by 1 when dfs completes 
- When repeating step 1, if node is in visited nodes, do not do dfs() and do not increment conn component count as this node has already been accounted for when recursively searching a previous node

See a.py simple example case. Output = 2 as 2 seperate connected graphs are found


Optimal:

Union find is outlined in iPad notes for this problem and implemented in numberConnectedUnionFind()
