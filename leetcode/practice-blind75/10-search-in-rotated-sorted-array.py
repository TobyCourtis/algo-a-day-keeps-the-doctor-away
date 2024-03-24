from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0

        while len(nums) > 0:
            midpoint = len(nums) // 2
            if len(nums) == 1 and nums[midpoint] != target:
                return -1

            if nums[midpoint] == target:
                return index + midpoint

            left = nums[:midpoint]
            right = nums[midpoint:]
            if nums[0] > nums[-1]:  # is rotated
                if left[0] > left[-1]:  # is left rotated
                    if right[0] <= target <= right[-1]:  # check if it's in RHS
                        nums = right
                        index += midpoint
                    else:
                        nums = left
                else:
                    if left[0] <= target <= left[-1]:  # check if it's in LHS
                        nums = left
                    else:
                        index += midpoint
                        nums = right
            else:  # default search case
                if target < nums[midpoint]:
                    nums = nums[:midpoint]
                else:
                    index += midpoint
                    nums = nums[midpoint:]
        return -1


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
