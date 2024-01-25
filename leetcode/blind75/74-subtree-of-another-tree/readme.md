Initial thoughts:

First submission: Runtime beats 97% and memory beats 99%

- On paper worked through an algorithm:
1. iterated through every node in root
2. If current node value == subtree root value 
3. Check root tree == subtree true using self.isSameTree()
4. If ANY of the nodes (subtrees) iterated through in original 'root' (step 1) are equivalent to the subtree then return True

The key in my approach was to return:
return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

This ensured that if any of the nodes in original root were equivalent then True was ultimately returned

<br/>

NOTE original attempt failed tests due to a slight oversight in logic:
```
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if root is None:
        return False

    if root.val == subRoot.val:
        return self.isSameTree(root, subRoot)
        
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```
was changed to
```
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if root is None:
        return False
        
    return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```
this is because some cases such as root = [1,1] subRoot = [1] then recursion was never initiated/called as we returned False immediately because the values were the same and the trees were not the same


<br/>
Optimal:
Mine was optimal