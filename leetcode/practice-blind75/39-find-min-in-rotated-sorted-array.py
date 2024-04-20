from typing import List

is_rotated = lambda x: x[0] > x[-1]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        mid_index = len(nums) // 2
        left = nums[:mid_index]
        right = nums[mid_index:]

        if is_rotated(nums):
            if is_rotated(left):
                return self.findMin(left)
            else:
                return self.findMin(right)

        else:
            return nums[0]  # first in array


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
