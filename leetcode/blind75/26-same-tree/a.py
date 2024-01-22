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

        if p is None:
            if q is not None:
                return False
        if q is None:
            if p is not None:
                return False

        if p.val != q.val:
            return False

        return self.isSameTree(p=p.left, q=q.left) and self.isSameTree(p=p.right, q=q.right)

    def factorial(self, n):
        if n == 1:
            return 1
        return n * self.factorial(n - 1)


p = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
q = TreeNode(1, left=TreeNode(2), right=TreeNode(3))

s = Solution()
print(s.isSameTree(p, q))
