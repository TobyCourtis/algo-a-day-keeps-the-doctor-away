class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(0)
            dp.append(tmp)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == (m - 1) or j == (n - 1):
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j + 1] + dp[i + 1][j]

        return dp[0][0]


s = Solution()
print(s.uniquePaths(3, 7))


# beat 70% runtime, 50% memory
