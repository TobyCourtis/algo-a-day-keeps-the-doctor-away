attempt:

attempted to reverse dfs() but missed the fact that null nodes are needed to indicate one section of tree has
terminated.

<br>

neetcode (preorder traversal dfs()):

General idea, we want to know when to stop building one side of the tree. Modified serialize code so that when a node is
None we append "N" to our output string.

In deserialize, we use dfs again and return None when the current value = "N".

deserialize:

1. self.i = 0
2. dfs()
    3. If vals[self.i] == "N": return None
    4. else: node = Treenode(vals[self.i])
3. return output of dfs() which ends up being the returning the first node created which is the root node.

Runtime beat 81%, memory beat 38%

