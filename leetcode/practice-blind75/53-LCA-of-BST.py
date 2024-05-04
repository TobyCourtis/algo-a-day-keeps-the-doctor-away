class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # cases:
            # 1) root == p.val or root == q.val
            # 2) p.val < root.val < q.val  or  q.val < root.val < p.val

            # either way we want to just return the root value, either we've split the tree with p one side and q other,
            # or we've hit one of the values and the other is a descendant of root
            return root


s = Solution()
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
print(s.lowestCommonAncestor(root, root.left, root.right).val)
