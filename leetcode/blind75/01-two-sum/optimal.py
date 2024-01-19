class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            numMap[nums[i]] = i  # second occurrence of a value is overwritten.

        # Find the complement
        for i in range(n):
            # loop through all elements in nums, looking for the complement to that element
            complement = target - nums[i]

            # make sure index of complement is not the same index you're currently on.
            # i.e [3,4,2,6] target = 6 don't count the 3 as it only occurs once
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found


s = Solution()
print(s.twoSum([2, 3, 4, 5, 6, 7, 11, 15], 9))
print(s.twoSum([3, 3], 6))
print(s.twoSum([-3, 4, 3, 90], 0))
print(s.twoSum([3, 2, 4], 6))
