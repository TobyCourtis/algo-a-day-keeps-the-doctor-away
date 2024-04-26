class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # whole array skipping final val OR whole3 array skipping first val
        return max(self.houseRobber(nums[:-1]), self.houseRobber(nums[1:]))

    """
    House Robber 1 problem (problem 42)
    """

    def houseRobber(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0

        for i in range(len(nums)):
            newRob = max(nums[i] + rob1, rob2)  # either we take current + prev OR adjacent house (whichever is larger)
            # shift the prev and current rob values
            rob1 = rob2
            rob2 = newRob

        return rob2


s = Solution()
print(s.rob([2, 3, 2]))
