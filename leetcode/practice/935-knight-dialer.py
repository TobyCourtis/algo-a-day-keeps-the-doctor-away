class Solution:

    """
    General idea on the phone dial, there are only so many moves that can be made

    Dynamic programming:
    - for every new digit in a phone number (up to n)
    - go through the number of cells that could get to the current cell in one move (these are labelled as rules)
        - e.g if we are adding digit 1 to the end of a phone number, only cell 8 and 6 can get there
        - therefore dp[1] = dp[8] + dp[6]      1 becomes the number of ways we could previously get to 8 and 6
        - repeat n times as there are n digits in the phone number
    """
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10

        rules = [
            [8, 6],
            [7, 9],
            [8, 4],
            [9, 3, 0],
            [],  # 5 has no ways of getting to it
            [7, 1, 0],
            [2, 6],
            [1, 3],
            [4, 2],
            [4, 6]
        ]

        for i in range(1, n):
            tmp_dp = dp.copy()
            for j in range(len(rules)):
                # for cell 1, the ways of getting to it were 8 and 6 so add the totals at 8 and 6
                count = 0
                for rule in rules[j]:
                    count += dp[rule-1]
                tmp_dp[j] = count
            dp = tmp_dp.copy()

        return sum(dp) % ((10**9) + 7)

    # time limit exceeded - simpler problem than a dfs approach
    def knightDialerDFS(self, n: int) -> int:
        grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [-1, 0, -1]
        ]

        count = 0
        cache = {}

        def dfs(x, y, acc):
            if (x < 0 or
                    x >= len(grid) or
                    y < 0 or
                    y >= len(grid[0]) or
                    grid[x][y] == -1):
                return

            if acc >= n:
                nonlocal count
                count += 1
                return

            dfs(x - 2, y + 1, acc + 1)
            dfs(x - 2, y - 1, acc + 1)

            dfs(x - 1, y + 2, acc + 1)
            dfs(x - 1, y - 2, acc + 1)

            dfs(x + 1, y + 2, acc + 1)
            dfs(x + 1, y - 2, acc + 1)

            dfs(x + 2, y - 1, acc + 1)
            dfs(x + 2, y + 1, acc + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1:
                    # go from the 10 starting points
                    dfs(i, j, 1)

        return count % ((1 * 10 ** 9) + 7)


s = Solution()
print(s.knightDialer(1))
print(s.knightDialer(2))
print(s.knightDialer(3131))
