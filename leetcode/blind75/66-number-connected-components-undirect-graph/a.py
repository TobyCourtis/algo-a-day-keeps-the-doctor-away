import collections


class Solution:

    def numberConnected(self, n, edges) -> int:
        return self.numberConnectedUnionFind(n, edges)

    def numberConnectedDFS(self, n, edges) -> int:
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

    def numberConnectedUnionFind(self, n, edges) -> int:
        parents = [i for i in range(n)]
        rank = [1] * n

        def find_parent(node):
            current = node

            while current != parents[current]:
                # see iPad notes for the below line logic
                parents[current] = parents[parents[current]]  # optimising to make the parent a root parent node
                current = parents[current]
            return current

        def union(edge0, edge1):
            parent1 = find_parent(edge0)
            parent2 = find_parent(edge1)

            if parent1 == parent2:
                return 0

            if rank[parent1] > rank[parent2]:
                parents[parent2] = parent1
                rank[parent1] += 1
            else:
                parents[parent1] = parent2
                rank[parent2] += 1
            return 1

        connected_components = n
        for edge in edges:
            connected_components -= union(edge[0], edge[1])

        return connected_components


s = Solution()
print(s.numberConnected(5, [[0, 1], [1, 2], [3, 4]]))
