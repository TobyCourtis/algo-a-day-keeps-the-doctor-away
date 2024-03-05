class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
import math


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = -math.inf

        def dfs(node: Optional[TreeNode]):
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
# print(s.maxPathSum(TreeNode(-10, left=TreeNode(3), right=TreeNode(5))))
print(s.maxPathSum(TreeNode(2, left=TreeNode(-1), right=None)))
