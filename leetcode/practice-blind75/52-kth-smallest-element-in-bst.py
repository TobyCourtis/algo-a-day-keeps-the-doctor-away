# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def kthSmallestRecur(self, root: Optional[TreeNode], k: int) -> int:
        # smallest = all the way left?

        out = []
        visited = 0

        def dfs(node):
            if len(out) == k or node is None:
                return

            dfs(node.left)
            if len(out) < k:
                out.append(node.val)

            dfs(node.right)
            # out.append(node.val)

        dfs(root)
        return out[-1]

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        temp = root
        visited = 0

        while temp or stack:
            while temp:
                stack.append(temp)
                temp = temp.left

            temp = stack.pop()
            visited += 1
            if visited == k:
                return temp.val

            temp = temp.right

        return 0


s = Solution()
print(s.kthSmallest(TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4)), 1))
print(s.kthSmallestRecur(TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4)), 1))
