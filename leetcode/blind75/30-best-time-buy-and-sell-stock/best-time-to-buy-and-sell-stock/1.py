import time


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        start = time.time()
        maxProfit = 0
        for buy in range(len(prices) - 1):
            for sell in range(buy + 1, len(prices)):
                if prices[sell] <= prices[buy]:
                    continue
                profit = prices[sell] - prices[buy]
                if profit > maxProfit:
                    maxProfit = profit
        end = time.time()
        print(f"{end - start} seconds")
        return maxProfit


s = Solution()
print(s.maxProfit([4, 9, 3, 8, 1, 8]))
