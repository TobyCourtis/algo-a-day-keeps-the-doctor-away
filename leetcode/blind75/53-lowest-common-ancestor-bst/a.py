# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[
        TreeNode]:
        return None

    def dfs(self, root: Optional[TreeNode], p, q):
        return self.dfs(root.left, p, q) and self.dfs(root.right, p, q)

    def is_descendant(self, root: Optional[TreeNode], node: Optional[TreeNode]):
        if root is None:
            return False

        if root.val == node.val:
            return True

        return self.is_descendant(root.left, node) or self.is_descendant(root.right, node)


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

s = Solution()
# s.lowestCommonAncestor(root, TreeNode(2), TreeNode(8))

print(s.is_descendant(root, TreeNode(2)))
