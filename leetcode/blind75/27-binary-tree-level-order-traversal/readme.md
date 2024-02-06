Initial attempt:

- Time expired attempting recursive solutions that do not keep a counter or some external variable updated
- I should embrace that keeping a global var updated outside of a recursive function is okay

Attempt 2:

- Implement solution that keeps global var updated

1. create initial output list [] and set count (for level/depth) to 0
2. create a recursive function which appends an empty list to output for each new level encountered in the tree.
3. For each node we append root.val to the corresponding list in output
4. We recursively call level() first with root.left then root.right. This ensures the LHS is appended to each list in output first.
5. Base case root = None
6. increment count for each new level we traverse


Runtime beat 58% users, memory beat 72% users