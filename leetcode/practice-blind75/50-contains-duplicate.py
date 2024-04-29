from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
