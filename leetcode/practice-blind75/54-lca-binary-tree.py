# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node: TreeNode):
            if node is None:
                return None

            if node.val == p.val or node.val == q.val:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            else:
                # return the result of the call which returned a node
                # e.g. if we're going left, eventually we return (p or q node exactly),
                # or the recursive call returned left and right which was the point at which the tree split
                # p and q.
                if left is None:
                    return right
                if right is None:
                    return left

        return dfs(root)


s = Solution()
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

print(s.lowestCommonAncestor(root, root.left, root.right).val)
