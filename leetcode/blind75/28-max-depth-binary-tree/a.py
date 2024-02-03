class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:

    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:
        if root is None:
            return depth
        return max(self.maxDepth(root.left, depth + 1), self.maxDepth(root.right, depth + 1))


s = Solution()
root = TreeNode(1, None, TreeNode(2))
print(s.maxDepth(root))
