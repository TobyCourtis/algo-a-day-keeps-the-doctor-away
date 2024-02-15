class Solution:
    def uniquePathsFirst(self, m: int, n: int) -> int:
        matrix = [[0] * n for _ in range(m)]

        matrix[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                right = down = 0
                if j < n - 1:
                    right = matrix[i][j + 1]
                if i < m - 1:
                    down = matrix[i + 1][j]

                matrix[i][j] += right + down

        return matrix[0][0]

    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]


s = Solution()
# print(s.uniquePaths(3, 3))
print(s.uniquePaths(3, 7))
