class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])

        # case [3, 9, 20, 15, 7], [9, 3, 15, 20, 7] root = 3, mid = 1 (index)
        # pre order skip root, take up until index of mid, in order take LHS of mid index
        # [9], [9]
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # pre order take after mid index, inorder take RHS of mid index
        # [20, 15, 7], [15, 20, 7]
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root


s = Solution()
print(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
