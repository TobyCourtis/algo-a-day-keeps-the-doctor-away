attempt:


My attempt found all the rules as tuples but would require slow and complex parsing of the tuples to deduce an output.

1. Loop through all words
2. For word i and word i + 1, the first different character in the two words is a rule.
   1. e.g wrt, wrf -> t < f



<br>

Neetcode (topological sort of graph):

1. Go through all words and build nodes
   1. if t < f then t -> f in graph
   2. if r < t then r -> t -> f
2. Traverse graph
   1. a loop means a contradiction (invalid) f -> w -> f 
   2. if disconnected graph then we can add all components in any order.


<br>


Post order dfs() (how to traverse graph):

- do dfs() but only append to output string when we've reached max depth
- build result in reverse
- need 'visit' tracked and current 'path' tracked
- See code comments for details and an example


<br>

Runtime - could not run as it's a premium problem