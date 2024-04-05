from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder=preorder[1:mid + 1],
                                   inorder=inorder[:mid])

        root.right = self.buildTree(preorder=preorder[mid + 1:],
                                    inorder=inorder[mid + 1:])

        return root


s = Solution()
tree = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print(tree.val)
print(tree.left.val)
print(tree.right.val)
