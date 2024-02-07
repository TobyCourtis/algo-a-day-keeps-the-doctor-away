First attempt:

- Good approach, poor runtime
- Memory beat 90%, runtime beat 5%
- O(n^2)

Second attempt:

- At first marginally better (simple cleaned existing code)
- Implemented solution looking for cycles in pre-requisites e. if 1 depdends on 2 which depends on 1 then False (cycle found).
  - If 1 -> 2 -> 3 and 3 is possible then deem 1 and 2 possible.


Optimal

- Decided to watch a video on the solution approach (not actual code) and implement after seeing the approach (Khan's algorith documented in Notion)
- Implementation was good but my while q loop initially had two loops of all nodes which was not needed
  - Refactored into one loop of adj nodes

- Khan's algorithm works to look for a topological order in the graph
- Correctly realised in attempt 2 that we should be looking for no cycles in the graph in order to return true


Beat 88% runtime and 80% memory