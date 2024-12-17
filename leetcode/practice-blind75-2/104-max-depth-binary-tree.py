from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def dfs(r, depth):
            nonlocal max_depth
            if r is None:
                if depth > max_depth:
                    max_depth = depth
                return
            depth += 1

            dfs(r.left, depth)
            dfs(r.right, depth)

            return depth

        dfs(root, depth=0)
        return max_depth


s = Solution()
print(s.maxDepth(TreeNode(1, TreeNode(2, TreeNode(3)))))
