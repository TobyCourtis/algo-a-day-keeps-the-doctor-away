class Solution:
    def rob(self, nums: list[int]) -> int:
        prev, prevPrev = 0, 0

        for house in nums:
            temp = max(house + prevPrev, prev)  # either we take current + prev - 1 OR just adjacent house (take the larger)
            # shift the prev and current rob values
            prevPrev = prev
            prev = temp

        return prev


s = Solution()
print(s.rob([1, 2, 3, 1]))
