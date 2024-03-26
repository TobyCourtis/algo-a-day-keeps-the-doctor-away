import math
from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        maximum = nums[0]
        acc = nums[0]
        index = 1

        while index < len(nums):
            if acc < 0:
                acc = nums[index]
            else:
                acc = acc + nums[index]

            maximum = max(maximum, acc)

            index += 1

        return maximum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
