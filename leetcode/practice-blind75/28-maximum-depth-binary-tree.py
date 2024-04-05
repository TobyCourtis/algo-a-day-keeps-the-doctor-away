class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:

    # cleaner method, same result
    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:
        if root is None:
            return depth
        return max(self.maxDepth(root.left, depth + 1), self.maxDepth(root.right, depth + 1))

    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        max_depth = 1

        def dfs(root, depth):
            nonlocal max_depth

            if root is None:
                return

            if depth > max_depth:
                max_depth = depth

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 1)
        return max_depth


s = Solution()
tree = TreeNode(3,
                left=TreeNode(9),
                right=TreeNode(20,
                               left=TreeNode(15),
                               right=TreeNode(7)))
print(s.maxDepth(tree))
