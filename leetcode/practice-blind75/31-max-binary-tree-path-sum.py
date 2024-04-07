# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total = 0

        def dfs(root):
            nonlocal total

            if root is None:
                return 0

            path_left = dfs(root.left)
            path_right = dfs(root.right)

            path_left = max(path_left, 0)  # if left/right path was negative, don't include so return 0
            path_right = max(path_right, 0)

            # check if we should use cur node as root and take left/right path
            total = max(total, root.val + path_left + path_right)

            return root.val + max(path_left, path_right)

        dfs(root)
        return total


s = Solution()
print(s.maxPathSum(TreeNode(1,
                            left=TreeNode(2),
                            right=TreeNode(3))))
print(s.maxPathSum(TreeNode(-10,
                            left=TreeNode(9),
                            right=TreeNode(20,
                                           left=TreeNode(15),
                                           right=TreeNode(7)))))
