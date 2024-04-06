from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            sell = prices[i]
            if sell < buy:
                buy = sell
            else:
                profit = max(profit, sell - buy)

        return profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
