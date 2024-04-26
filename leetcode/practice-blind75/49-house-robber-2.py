from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        return max(self.houseRobber(nums[:-1]),
                   self.houseRobber(nums[1:]))

    def houseRobber(self, nums: List[int]) -> int:
        prev, prevPrev = 0, 0

        for house in nums:
            tmp = max(house + prevPrev, prev)
            prevPrev = prev

            prev = tmp
        return prev


s = Solution()
print(s.rob([1, 2, 3, 1]))
