Initial thoughts:

- Iterate through each node in the tree
- node.left = node.right and node.right = node.left

Implementation:

Submission beat 94% runtime, 61% memory

- The only tricky part was thinking recursively how to return the correct results
- Main logic below returns root which is ultimately the highest level call which is the starting root node:
```
self.invertTree(root.left)
self.invertTree(root.right)
return root
```

- Note nothing is done with the result of self.invertTree() because we only need it to be called




Optimal:
- Mine was optimal