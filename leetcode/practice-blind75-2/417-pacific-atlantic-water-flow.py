from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        atlantic = set()
        pacific = set()

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
            dfs(i, 0, pacific)  # start pacific col 0 (left)
            dfs(i, n - 1, atlantic)  # start atlantic col -1 (right)

        for j in range(n):
            dfs(0, j, pacific)  # start pacific row 0 (top)
            dfs(m - 1, j, atlantic)  # row -1  (bottom)

        return [[x, y] for x, y in list(pacific.intersection(atlantic))]


s = Solution()
out = s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
print(out)
