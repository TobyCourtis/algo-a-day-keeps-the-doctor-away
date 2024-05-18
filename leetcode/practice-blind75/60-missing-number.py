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


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)  # len(nums) is always largest value in the list e.g [0,1,3] len == 3 which is largest.

        # if nums is 0 -> 9 with one number missing then arr length = 9
        # let's begin with res as the largest number (9)
        # if 9 is actually missing then at the end we'll return res which is 9
        # if 8 is actually missing then at one point we'll have:
        # res = 9
        # res += 8
        # res -= 9
        # res = 8   <-- this num is returned

        # think of this approach as building a sum whilst taking away the actual values
        for i in range(len(nums)):
            res += i  # calculate sum of all nums
            res -= nums[i]  # takeaway what actually occurs

        return res
