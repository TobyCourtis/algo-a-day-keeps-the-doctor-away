from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # for every node in root, check if subroot matches via dfs
        # first is dfs for going through tree, second is dfs for matching

        def dfs(r, sr):
            if r is None and sr is None:
                return True
            elif r is None or sr is None:
                return False
            elif r.val == sr.val:
                return dfs(r.right, sr.right) and dfs(r.left, sr.left)
            else:
                return False

        def dfs_all(main, sub):
            if main is None:
                return False
            return dfs(main, sub) or dfs_all(main.right, sub) or dfs_all(main.left, sub)

        return dfs_all(root, subRoot)


s = Solution()
print(
    s.isSubtree(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)), TreeNode(4, TreeNode(1), TreeNode(2))))
