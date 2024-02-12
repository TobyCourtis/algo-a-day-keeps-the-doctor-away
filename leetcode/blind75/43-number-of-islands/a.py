class Solution:
    def numIslandsFirst(self, grid: list[list[str]]) -> int:
        visited = set()

        m = len(grid)
        n = len(grid[0])

        def search(i1, i2):
            if (i1, i2) in visited:
                return

            visited.add((i1, i2))

            if grid[i1][i2] == '1':
                # continue search
                if i2 > 0:
                    search(i1, i2 - 1)  # left
                if i2 < n - 1:
                    search(i1, i2 + 1)  # right
                if i1 < m - 1:
                    search(i1 + 1, i2)  # down
                if i1 > 0:
                    search(i1 - 1, i2)  # up

            return

        # 1. recursive visit
        # 2. if left + right + bottom is 0 then break (or just if current = 0 then break otherwise continue)
        islands = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    if grid[i][j] == '1':
                        search(i, j)
                        islands += 1
                    else:
                        visited.add((i, j))

        return islands

    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def search(i1, i2):
            if grid[i1][i2] == '0':
                return
            else:
                # continue search
                grid[i1][i2] = '0'
                if i2 > 0:
                    search(i1, i2 - 1)  # left
                if i2 < n - 1:
                    search(i1, i2 + 1)  # right
                if i1 < m - 1:
                    search(i1 + 1, i2)  # down
                if i1 > 0:
                    search(i1 - 1, i2)  # up

            return

        # 1. recursive visit
        # 2. if left + right + bottom is 0 then break (or just if current = 0 then break otherwise continue)
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    search(i, j)
                    islands += 1

        return islands


s = Solution()
print(s.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(s.numIslands([
    ["1", "0", "1", "1", "1"],
    ["1", "0", "1", "0", "1"],
    ["1", "1", "1", "0", "1"]]))
