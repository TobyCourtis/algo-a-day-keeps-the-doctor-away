# [0,1,2,3] ^ [0,1,3] = 2
# with XOR all duplicates will cancel out and we are left with the one value that's EXCLUSIVE to one array.
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)  # nums is one less in size than the list of full range [0 .. n] so we begin with res as 'n'
        for i in range(len(nums)):
            res += (i - nums[i])

        return res


s = Solution()
print(s.missingNumber([0, 1, 3]))
