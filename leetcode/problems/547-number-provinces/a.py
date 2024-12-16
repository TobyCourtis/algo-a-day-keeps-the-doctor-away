"""
Not part of blind 75

To solve this problem optimally we need to use the union find algorithm
"""


class Solution:

    # we need to find the number of provinces (group of directly or indirectly connected cities)
    # input = city matrix where matrix[i][j] = 1 if city i is connected to j
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        city_count = len(isConnected)
        parent = [i for i in range(city_count)]
        rank = [1] * city_count

        def find_parent(city):
            current = city

            while current != parent[current]:
                parent[current] = parent[parent[current]]
                current = parent[current]

            return current

        def union(city1, city2):
            parent1 = find_parent(city1)
            parent2 = find_parent(city2)

            if parent1 == parent2:
                return 0

            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += 1
            else:
                parent[parent1] = parent2
                rank[parent2] += 1
            return 1

        number_provinces = city_count
        for i in range(city_count):
            for j in range(i + 1, city_count):
                if i != j:
                    if isConnected[i][j] == 1:  # if 1 then we have an edge we need to perform a union with
                        number_provinces -= union(i, j)
        return number_provinces


s = Solution()
print(s.findCircleNum([[1, 1, 0],
                       [1, 1, 0],
                       [0, 0, 1]]))
