class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:  # both on left of root
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:  # both on right of root
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root  # p and q are either side of root so return current node
