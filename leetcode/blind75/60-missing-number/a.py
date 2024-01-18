class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums_set:
                return i


s = Solution()
print(s.missingNumber([0, 1, 3]))
