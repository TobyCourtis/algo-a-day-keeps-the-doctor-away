from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def dfs(i, j):
            if (i, j) in visited or i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] != '1':
                return

            visited.add((i, j))

            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited:
                    continue

                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1
                else:
                    visited.add((i, j))

        return islands


s = Solution()
print(s.numIslands(
    [["1", "1", "1", "1", "0"],
     ["1", "1", "0", "1", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "0", "0", "0"]]))

print(s.numIslands(
    [["1", "1", "0", "0", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "1", "0", "0"],
     ["0", "0", "0", "1", "1"]]))
