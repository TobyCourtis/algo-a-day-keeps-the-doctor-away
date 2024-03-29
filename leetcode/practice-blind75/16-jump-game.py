from typing import List


class Solution:
    """
    runtime 30%
    memory 87%
    """

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i  # reduce goal to be nearer to 0th index

        return True if goal == 0 else False

    """
    runtime 5%
    memory 75%
    """

    def canJump1(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        nums[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                nums[i] = False
            else:
                nums[i] = any(nums[i + 1:i + nums[i] + 1])

        return nums[0]


s = Solution()
print(s.canJump([2, 3, 1, 1, 4]))
print(s.canJump([3, 2, 1, 0, 4]))
