class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0

        for house in nums:
            temp = max(house + rob1, rob2)  # either we take current + prev - 1 OR just adjacent house (take the larger)
            # shift the prev and current rob values
            rob1 = rob2
            rob2 = temp

        return rob2


s = Solution()
print(s.rob([1, 2, 3, 1]))
