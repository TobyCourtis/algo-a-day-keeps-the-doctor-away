# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        output = []
        count = 0

        def level(count, root):
            if root is None:
                return

            if len(output) <= count:
                output.append([])

            output[count].append(root.val)
            count += 1
            level(count, root.left)
            level(count, root.right)
        level(count,  root)
        return output


root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
s = Solution()
print(s.levelOrder(root))
