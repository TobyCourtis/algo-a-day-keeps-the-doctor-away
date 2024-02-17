# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []
        out = None

        def dfs(root):
            nonlocal out
            if not root or len(in_order) >= k:
                return

            dfs(root.left)

            if len(in_order) < k:
                in_order.append(root.val)

            dfs(root.right)

            return

        dfs(root)
        return in_order[-1]

    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize an empty stack to perform in-order traversal
        stack = []
        # Initialize a variable to count the number of visited nodes
        n = 0
        # Start with the root node
        temp = root

        # Perform in-order traversal
        while temp or stack:
            # Traverse as far left as possible, pushing each node onto the stack
            while temp:
                stack.append(temp)
                temp = temp.left
            # Once we reach the leftmost node, start popping nodes from the stack
            temp = stack.pop()
            # Increment the count of visited nodes
            n += 1
            # If count becomes equal to k, return the value of the current node
            if n == k:
                return temp.val
            # Move to the right subtree and continue traversal
            temp = temp.right

        # Return 0 if kth smallest element not found (shouldn't happen in a valid BST)
        return 0


s = Solution()
root = TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4))
print(s.kthSmallest(root, 1))
