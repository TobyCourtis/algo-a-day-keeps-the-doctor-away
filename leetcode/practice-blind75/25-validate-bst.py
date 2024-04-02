# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, left, right):
            if root is None:
                return True
            if (left is not None and root.val >= left) or (right is not None and root.val <= right):
                return False

            return dfs(root.left, root.val, right) and dfs(root.right, left, root.val)

        return dfs(root, None, None)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, left, right):
            if root is None:
                return True
            if root.val >= left or root.val <= right:
                return False

            return dfs(root.left, root.val, right) and dfs(root.right, left, root.val)

        return dfs(root, math.inf, -math.inf)


s = Solution()
print(s.isValidBST(TreeNode(2,
                            left=TreeNode(1),
                            right=TreeNode(3))))

print(s.isValidBST(TreeNode(5,
                            left=TreeNode(6),
                            right=TreeNode(7))))

print(s.isValidBST(TreeNode(0,
                            left=None,
                            right=TreeNode(-1))))
