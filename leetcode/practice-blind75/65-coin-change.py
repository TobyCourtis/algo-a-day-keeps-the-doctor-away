from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if (i - coin) >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])  # we've used a coin (hence the '1 +') the rest is dp[i -coin]

        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]


s = Solution()
print(s.coinChange([1, 2, 5], 11))
