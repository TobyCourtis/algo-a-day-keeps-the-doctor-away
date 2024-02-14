class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestorTimeLimitExceeded(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        out = []
        found_p = False
        found_q = False

        def dfs(node):
            nonlocal found_p, found_q

            if node is None:
                return False

            if not found_p:
                if node.val == p.val:
                    found_p = True
            if not found_q:
                if node.val == q.val:
                    found_q = True

            if found_p and found_q:
                return True

            return dfs(node.left) or dfs(node.right)

        out = [None]

        def dfs2(node2):
            nonlocal found_p, found_q

            if node2 is None:
                return

            if dfs(node2):
                out[-1] = node2
                found_p = False
                found_q = False
            else:
                found_p = False
                found_q = False
                return

            return dfs2(node2.left) or dfs2(node2.right)

        dfs2(root)
        return out[-1]

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node):
            if node is None:
                return None

            if node.val == p.val or node.val == q.val:
                return node

            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            else:
                # return the result that was non-null
                # this is the correct output!
                # this is also the key to not running dfs many times (we've only run on the full tree once)
                # equivalent to:
                # if left is None:
                #    return right
                # else:
                #    return left

                return left or right

        return dfs(root)


s = Solution()
root = TreeNode(3)
p = TreeNode(1)
root.left = p
q = TreeNode(5)
root.right = q
print(s.lowestCommonAncestor(root, p, q).val)
