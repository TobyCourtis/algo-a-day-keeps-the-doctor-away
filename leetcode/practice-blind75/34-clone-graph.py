class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node, nodes_dict):
            if node.val not in nodes_dict:
                nodes_dict[node.val] = Node(node.val)

                for nbr in node.neighbors:
                    nodes_dict[node.val].neighbors.append(dfs(nbr, nodes_dict))

            return nodes_dict[node.val]

        return dfs(node, {}) if node else None


s = Solution()
