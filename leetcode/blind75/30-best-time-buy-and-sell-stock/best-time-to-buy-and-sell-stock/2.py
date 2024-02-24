class Solution:
    def maxProfit(self, prices: [int]) -> int:
        buy = 0
        maxProfit = 0
        maxProfitIndex = None
        broke = False
        while buy < len(prices) - 1:  # account for length of array minus one with index - 1 from that
            if prices[buy + 1] <= prices[buy]:
                buy = buy + 1
                continue
            for sell in range(buy + 1, len(prices)):
                if prices[sell] < prices[buy]:
                    buy = sell  # found a value to buy at less than the current one in the future
                    # however, we have still recorded profits up to this sell value
                    broke = True
                    break
                profit = prices[sell] - prices[buy]
                if profit > maxProfit:
                    maxProfit = profit
                    maxProfitIndex = sell
            if maxProfitIndex is not None:
                buy = maxProfitIndex + 1
                maxProfitIndex = None
            elif not broke:
                buy = buy + 1
            else:
                broke = False

        return maxProfit


s = Solution()
with open('large_input.txt', 'r') as file:
    largeIn = file.read()
print(s.maxProfit([int(x) for x in largeIn.split(',')]))
