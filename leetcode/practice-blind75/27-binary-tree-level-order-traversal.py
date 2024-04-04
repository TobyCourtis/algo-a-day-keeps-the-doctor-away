# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = []

        def dfs(root, lvl):
            if root is None:
                return

            if len(level) == lvl:
                level.append([])

            level[lvl].append(root.val)

            dfs(root.left, lvl + 1)
            dfs(root.right, lvl + 1)

        dfs(root, 0)
        return level


s = Solution()

tree = TreeNode(3,
                left=TreeNode(9),
                right=TreeNode(20,
                               left=TreeNode(15),
                               right=TreeNode(7)))

print(s.levelOrder(tree))
