from typing import List


class Solution:
    def pacificAtlanticFirstAttempt(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        visited = set()
        pacific = set()  # top and left
        atlantic = set()  # bottom and right

        # issue, we need to add everything in the path that could reach the ocean
        def dfs(i, j, path=[]):
            if path is None:
                path = set()

            path.append((i, j))

            if (i, j) in visited:
                if (i, j) in atlantic:
                    for p in path:
                        atlantic.add(p)
                if (i, j) in pacific:
                    for p in path:
                        pacific.add(p)
                return

            visited.add((i, j))

            if i == 0 or j == 0:
                if i == m - 1 or j == n - 1:
                    for p in path:
                        atlantic.add(p)
                for p in path:
                    pacific.add(p)
                return

            if i == m - 1 or j == n - 1:
                for p in path:
                    atlantic.add(p)
                return

            current = heights[i][j]
            if i > 0 and heights[i - 1][j] <= current:  # up
                dfs(i - 1, j, path)
            if j > 0 and heights[i][j - 1] <= current:  # left
                dfs(i, j - 1, path)
            if i < m - 1 and heights[i + 1][j] <= current:  # down
                dfs(i + 1, j, path)
            if j < n - 1 and heights[i][j + 1] <= current:  # right
                dfs(i, j + 1, path)

        for i in range(m):
            for j in range(n):
                dfs(i, j, [])

        return list(pacific.intersection(atlantic))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(i, j, visited):
            if (i, j) in visited:
                return

            visited.add((i, j))

            current = heights[i][j]
            if i > 0 and heights[i - 1][j] >= current:  # up
                dfs(i - 1, j, visited)
            if j > 0 and heights[i][j - 1] >= current:  # left
                dfs(i, j - 1, visited)
            if i < m - 1 and heights[i + 1][j] >= current:  # down
                dfs(i + 1, j, visited)
            if j < n - 1 and heights[i][j + 1] >= current:  # right
                dfs(i, j + 1, visited)

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)

        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)

        return [[x, y] for x, y in list(pacific.intersection(atlantic))]


s = Solution()
out = s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
print(out)
# assert out == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
