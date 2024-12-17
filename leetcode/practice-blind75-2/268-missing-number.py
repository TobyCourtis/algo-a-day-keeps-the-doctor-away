from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        accumulator = len(nums)
        for i in range(len(nums)):
            accumulator += i
            accumulator -= nums[i]
        return accumulator


s = Solution()
print(s.missingNumber([3, 0, 1]))
print(s.missingNumber([0, 1]))
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
