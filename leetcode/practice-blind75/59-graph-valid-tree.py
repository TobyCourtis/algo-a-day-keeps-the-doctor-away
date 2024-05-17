import collections
from typing import List


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= 1:
            return True

        nodes = {}
        for i in range(n):
            nodes[i] = set()

        for edge in edges:
            nodes[edge[0]].add(edge[1])
            nodes[edge[1]].add(edge[0])

        visited = set()

        def dfs(val: int, prev: int):
            if val in visited:
                return False

            visited.add(val)

            # go through each neighbour of nodes[val] and add to visited
            for nbr in nodes[val]:
                if nbr == prev:
                    continue  # we don't want to go back to node we just came from
                if not dfs(nbr, val):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n


s = Solution()
print(s.valid_tree(n=5,
                   edges=[[0, 1], [0, 2], [0, 3], [1, 4]]))
print(s.valid_tree(n=5,
                   edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
