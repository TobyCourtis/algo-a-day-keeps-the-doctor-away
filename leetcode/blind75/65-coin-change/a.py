class Solution:
    def coinChangeFirst(self, coins: list[int], amount: int) -> int:
        coins.sort()
        if amount == 0:
            return 0
        out = 1
        while True:
            for i in range(len(coins) - 1, -1, -1):
                tmp = amount - coins[i]
                if tmp > 0:
                    # start process again with amount
                    amount = tmp
                    break
                elif tmp == 0:
                    return out
            out += 1

            if tmp < 0:
                return -1

    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)  # dp values inclusive of 0
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if (a - coin) >= 0:
                    # for case [1,3,4,5]
                    #  dp[7] = 1 + dp[6]  # 1 + dp[7 - coin_value]
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != (amount + 1) else -1


s = Solution()
# print(s.coinChange(coins=[1, 2, 5], amount=11))
print(s.coinChange(coins=[186, 419, 83, 408], amount=6249))
