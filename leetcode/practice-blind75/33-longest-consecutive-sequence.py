    from typing import List


    class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
            maximum = 0
            nums = set(nums)

            for num in nums:
                if num - 1 not in nums:
                    cur_sequence_length = 1
                    while num + 1 in nums:
                        num = num + 1
                        cur_sequence_length += 1
                    maximum = max(maximum, cur_sequence_length)

            return maximum


s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
