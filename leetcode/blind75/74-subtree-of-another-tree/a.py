class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,
                                                                                                      subRoot)

    def isSameTree(self, one: Optional[TreeNode], two: Optional[TreeNode]) -> bool:
        if one is None and two is None:
            return True

        if one is None:
            if two is not None:
                return False
        if two is None:
            if one is not None:
                return False

        if one.val != two.val:
            return False

        return self.isSameTree(one=one.left, two=two.left) and self.isSameTree(one=one.right, two=two.right)


subroot = TreeNode(4, left=TreeNode(1), right=TreeNode(2))
root = TreeNode(val=3,
                left=subroot,
                right=TreeNode(5))


# subroot = TreeNode(1)
# root = TreeNode(1, left=TreeNode(1))

s = Solution()
print(s.isSubtree(root, subroot))
