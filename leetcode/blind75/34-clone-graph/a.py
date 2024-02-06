# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node, nodes_dict):
            # 1. if node not already in dictionary then we need to create it
            if node.val not in nodes_dict:
                # create the Node without neighbors in node dict
                nodes_dict[node.val] = Node(node.val)
                for nbr in node.neighbors:
                    # for every neighbor, append to 'neighbors' attribute for node with val node.val
                    # the node itself is created through calling dfs again
                    nodes_dict[node.val].neighbors.append(dfs(nbr, nodes_dict))

            # at the end return the copied node you have just created in the node dictionary
            return nodes_dict[node.val]

        return dfs(node, {}) if node is not None else None


s = Solution()
