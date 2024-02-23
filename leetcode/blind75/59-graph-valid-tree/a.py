from typing import (
    List,
)


class Node:
    def __init__(self, val):
        self.val = val
        self.siblings = set()


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = {}
        for i in range(n):
            nodes[i] = Node(i)

        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            nodes[n1].siblings.add(n2)
            nodes[n2].siblings.add(n1)

        visited = set()

        def dfs(val, prev):
            if val in visited:
                return False

            visited.add(val)

            for s in nodes[val].siblings:
                if s == prev:
                    continue  # if 0 -> 1, when visiting 1 we do not want to go back to 0
                if not dfs(s, val):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n

    def valid_tree_first(self, n: int, edges: List[List[int]]) -> bool:
        nodes = {}
        for i in range(n):
            nodes[i] = Node(i)

        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            nodes[n1].siblings.add(n2)
            nodes[n2].siblings.add(n1)

        # for node 1, go to all kids
        # none of their kids can be connected OR connected to 1
        for node in nodes.values():
            # node = 1
            for s1 in node.siblings:
                for s2 in node.siblings:
                    if s1 != s2:

                        s1siblings = nodes[s1].siblings.copy()
                        s1siblings.remove(node.val)
                        s1giblings2 = set()
                        for sib in s1siblings:
                            s1giblings2.add(sib)

                        s2siblings = nodes[s2].siblings.copy()
                        s2siblings.remove(node.val)
                        s2giblings2 = set()
                        for sib in s2siblings:
                            s2giblings2.add(sib)

                        if node.val in s1siblings or node.val in s2siblings:
                            return False
                        if s1siblings.intersection(s2siblings):
                            return False
        return True


s = Solution()
print(s.valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(s.valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
