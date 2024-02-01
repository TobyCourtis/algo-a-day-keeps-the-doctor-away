# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        left = root.left
        right = root.right
        root.left = right
        root.right = left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# root = TreeNode(2, TreeNode(1), TreeNode(3))
root = TreeNode(2, left=TreeNode(1))
s = Solution()
out = s.invertTree(root)

print(out.val)
print(f"left: {out.left.val if out.left is not None else None}")
print(f"right: {out.right.val if out.right is not None else None}")
