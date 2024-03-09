# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = 0

        def dfs(node):
            nonlocal maximum

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left = max(left, 0)
            right = max(right, 0)

            maximum = max(maximum, (node.val + left + right))

            return node.val + max(left, right)

        dfs(root)
        return maximum


s = Solution()
print(s.maxPathSum(TreeNode(3, TreeNode(1), TreeNode(2))))
