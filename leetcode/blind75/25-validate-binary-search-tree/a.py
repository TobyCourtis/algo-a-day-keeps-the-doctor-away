# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, lower_bound, upper_bound):
            if node is None:
                return True
            if not (node.val < upper_bound and node.val > lower_bound):
                return False

            # when we go left, the upper bound is updated to node.val because we cannot be larger than said node
            # when we go right, the lower bound updated because we cannot go lower than said node
            return dfs(node.left, lower_bound, node.val) and dfs(node.right, node.val, upper_bound)

        return dfs(root, lower_bound=-math.inf, upper_bound=math.inf)

    def isValidBSTInitial(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left_max, right_max):
            if node is None:
                return True

            if node.val < right_max or node.val > left_max:
                return False

            if node.left:
                if node.left.val >= node.val:
                    return False

            if node.right:
                if node.right.val <= node.val:
                    return False

            # 1. if we go left, update the left max to be current node as everything left needs to be less than current
            # do not update right max
            # 2.  the first time we go right, set right_max to current node value
            # do not update left
            return dfs(node.left, node.val, right_max) and dfs(node.right, left_max,
                                                               node.val if right_max == -math.inf else right_max)

        return dfs(root, math.inf, -math.inf)


root = TreeNode(2, TreeNode(1), TreeNode(3))
# root = TreeNode(27,
#                 left=TreeNode(10,
#                               left=TreeNode(1), right=TreeNode(11,
#                                                                left=TreeNode(2), right=TreeNode(12))))
# root2 = TreeNode(27,
#                  left=TreeNode(10,
#                                left=TreeNode(1), right=TreeNode(11,
#                                                                 left=TreeNode(2), right=TreeNode(28))))
root3 = TreeNode(5, left=TreeNode(4), right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)))

# [3,1,5,0,2,4,6]
root4 = TreeNode(3, left=TreeNode(1, left=TreeNode(0), right=TreeNode(2)),
                 right=TreeNode(5, left=TreeNode(4), right=TreeNode(6)))

s = Solution()
# print(s.isValidBST(root))
# print(s.isValidBST(root3))
# print(s.isValidBST(root2))
print(s.isValidBST(root4))
