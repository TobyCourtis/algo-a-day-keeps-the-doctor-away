# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if ((p is None and q is not None) or
                (p is not None and q is None) or
                (p.val != q.val)):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


s = Solution()
print(s.isSameTree(TreeNode(1, left=TreeNode(2), right=TreeNode(3)),
                   TreeNode(1, left=TreeNode(2), right=TreeNode(4))))
