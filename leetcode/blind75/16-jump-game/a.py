class Solution:

    def canJumpFirstAttempt(self, nums: list[int]) -> bool:

        if len(nums) == 1:
            return True

        for i in range(1, nums[0] + 1):
            if self.canJump(nums[i:]):
                return True

        return False

    def canJumpSecondAttempt(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True

        # backtrack
        cache = [False] * len(nums)

        cache[len(nums) - 1] = True

        first = nums[0]

        for i in range(len(nums) - 2, -1, -1):
            victim = nums[i]
            for j in range(1, victim + 1):
                if i + j >= len(nums):
                    break
                elif cache[i + j]:
                    cache[i] = True
                    break

            if i < first + 1 and cache[i]:
                return True

        return False

    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False


s = Solution()
print(s.canJump([2, 3, 1, 1, 4]))
print(s.canJump([3, 2, 1, 0, 4]))
