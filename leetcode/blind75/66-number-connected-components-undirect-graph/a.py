import collections


class Solution:

    def numberConnected(self, n, edges) -> int:
        if n == 0:
            return 0

        edge_dict = collections.defaultdict(list)
        for edge in edges:
            edge_dict[edge[0]].append(edge[1])

        visited = set()
        number_connected = 0

        def dfs(node_val):
            if node_val in visited:
                return
            visited.add(node_val)
            for nbr in edge_dict[node_val]:
                dfs(nbr)

        for node in range(n):
            if node not in visited:
                dfs(node)
                number_connected += 1

        return number_connected


s = Solution()
print(s.numberConnected(5, [[0, 1], [1, 2], [3, 4]]))
