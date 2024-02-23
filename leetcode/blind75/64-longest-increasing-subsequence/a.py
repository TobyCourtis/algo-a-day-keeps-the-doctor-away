from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        DP = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):  # loop backwards through nums
            for j in range(i + 1, len(DP)):  # loop through DP[j] where j starts after i index
                if nums[i] < nums[j]:
                    DP[i] = max(DP[i], 1 + DP[j])  # either the largest is current value or 1 + a previous DP value

        return max(DP)


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
