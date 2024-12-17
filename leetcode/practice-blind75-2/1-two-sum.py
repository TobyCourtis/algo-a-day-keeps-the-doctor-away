import collections
from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index_map = collections.defaultdict(list)

        for i in range(len(nums)):
            num_to_index_map[nums[i]].append(i)

        for num in num_to_index_map.keys():
            leftover = target - num
            if leftover == num:
                if len(num_to_index_map[num]) > 1:
                    return num_to_index_map[num]
            elif leftover in num_to_index_map:
                return num_to_index_map[num] + num_to_index_map[leftover]

    def twoSumNLogN(self, nums: List[int], target: int) -> List[int]:
        # would need improving to lookup original index from map
        nums.sort()
        print(nums)
        start = 0
        end = len(nums) - 1
        while nums[end] > target:
            end -= 1

        while True:
            if (nums[start] + nums[end]) == target:
                return [start, end]
            elif (nums[start] + nums[end]) > target:
                end -= 1
            elif (nums[start] + nums[end]) < target:
                start += 1

    def twoSumNSquare(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]


s = Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums, target))
nums = [3, 2, 4]
target = 6
print(s.twoSum(nums, target))
nums = [3, 3]
target = 6
print(s.twoSum(nums, target))
