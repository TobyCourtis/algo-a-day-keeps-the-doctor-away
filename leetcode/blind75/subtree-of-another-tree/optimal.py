# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(ns, nt):  # check current root/subnode are equal
            if ns is None and nt is None:
                return True
            elif ns is None or nt is None:
                return False
            elif ns.val == nt.val:
                return dfs(ns.right, nt.right) and dfs(ns.left, nt.left)
            else:
                return False

        # run DFS for all nodes
        def dfs_all(main, sub):
            if main is None:
                return False
            else:
                return dfs(main, sub) or dfs_all(main.right, sub) or dfs_all(main.left, sub)

        return dfs_all(root, subRoot)
