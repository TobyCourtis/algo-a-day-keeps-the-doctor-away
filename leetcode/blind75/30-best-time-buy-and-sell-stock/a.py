class Solution:
    def maxProfitONSquared(self, prices: list[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                maxProfit = max(maxProfit, prices[j] - prices[i])
        return maxProfit

    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        min = prices[0]  # set min to first day
        for i in range(1, len(prices)):
            current = prices[i]
            # update min if current is less than min
            if current < min:
                min = current
            # record profit if current - min (sell - buy) is greater than maxProfit
            elif (current - min) > maxProfit:
                maxProfit = current - min
        return maxProfit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
