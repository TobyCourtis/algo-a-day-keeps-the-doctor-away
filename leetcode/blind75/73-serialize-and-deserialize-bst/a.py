# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CodecFirst:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        out = []

        def dfs(node):
            if node is None:
                return
            out.append(str(node.val) + "#")

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        string = ""
        for val in out:
            string += val
        return string

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        data = [2, 1, 3]
        cur = out = TreeNode(data[0])

        def dfs(node, index):
            if index >= len(data) - 2:
                return

            node.left = TreeNode(data[index + 1])
            dfs(node.left, index + 1)
            node.right = TreeNode(data[index + 2])
            dfs(node.right, index + 2)

        dfs(cur, 0)
        return out


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        out = []

        def dfs(node):
            if node is None:
                out.append("N")
                return
            out.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(out)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

ser = Codec()
deser = Codec()

tree = ser.serialize(root)
print(tree)

ans = deser.deserialize(tree)
print(ans.val)
print(ans.left.val)
print(ans.right.val)
