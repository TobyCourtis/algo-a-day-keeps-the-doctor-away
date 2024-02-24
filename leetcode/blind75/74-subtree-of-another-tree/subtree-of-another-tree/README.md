Notes:

In general, nailed the approach but l33tcode seemed to have some non-reproducible problem with recursion.

Approach:
1. Gather all nodes in the tree
2. For each node in the tree, check equivalence with the sub_tree input (two layers of recursion)
3. Return True if match else fallback on None