class Solution:
    def maxProfit(self, prices: [int]) -> int:

        maxProfit = 0
        min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
            elif (prices[i] - min) > maxProfit:
                maxProfit = prices[i] - min

        return maxProfit


s = Solution()
with open('./large_input.txt', 'r') as file:
    largeIn = file.read()
print(s.maxProfit([int(x) for x in largeIn.split(',')]))
