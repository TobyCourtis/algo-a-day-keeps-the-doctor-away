class Solution:
    def twoSumOptimalSpace(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if (nums[i] + nums[j]) == target:
                        return [i, j]
        return []

    def twoSumOptimalTime(self, nums: list[int], target: int) -> list[int]:
        hash = {}  # val : index
        for index in range(len(nums)):
            val = nums[index]
            if val not in hash:
                hash[val] = []
            hash[val] += [index]

        if target % 2 == 0:
            mid = target // 2
            if mid in hash:
                if len(hash[mid]) > 1:
                    return hash[mid]
                else:
                    del hash[mid]

        for i in range(len(nums)):
            if nums[i] in hash and (target - nums[i]) in hash:
                return [] + hash[nums[i]] + hash[target - nums[i]]


nums = [2, 3, 4, 5, 6, 7, 11, 15]
target = 9
s = Solution()

print(s.twoSumOptimalSpace(nums, target))
print(s.twoSumOptimalSpace([3, 3], 6))

print(s.twoSumOptimalTime(nums, target))
print(s.twoSumOptimalTime([3, 3], 6))
print(s.twoSumOptimalTime([-3, 4, 3, 90], 0))
print(s.twoSumOptimalTime([3, 2, 4], 6))
