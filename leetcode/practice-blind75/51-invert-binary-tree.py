# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pointer = root

        def dfs(node):
            if node is None:
                return
            tmp = node.right
            node.right = node.left
            node.left = tmp
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return pointer


s = Solution()
tree = s.invertTree(TreeNode(1, left=TreeNode(2), right=TreeNode(3)))

while tree:
    print(tree.val)
    tree = tree.left
