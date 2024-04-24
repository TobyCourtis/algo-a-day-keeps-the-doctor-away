from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        maximum = 0

        def recur(index, count):
            nonlocal maximum

            if index > len(nums) - 1:
                maximum = max(maximum, count)
                return

            count = count + nums[index]
            recur(index + 2, count)
            recur(index + 3, count)

        recur(0, 0)
        return maximum


s = Solution()
print(s.rob([2, 7, 9, 3, 1]))
print(s.rob([100, 7, 9, 100, 1]))
print(s.rob([100, 7, 99, 100, 99]))
