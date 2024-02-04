class Solution:

    def maxSubArrayOne(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        left = 0
        right = 0
        maximum = nums[0]

        while right < len(nums):
            maximum = max(maximum, sum(nums[left:right + 1]))  # left up to right inclusive

            # case we move both pointers forward because next value is larger than the whole sum we've created so far
            next_index = right + 1
            if next_index < len(nums) and nums[next_index] > maximum:
                left = next_index
                right = next_index
            else:
                right = next_index  # increment right because we're expanding the current subarray to find larger maximum

        return maximum

    def maxSubArrayTwo(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        left = 0
        right = 0
        maximum = nums[0]

        while right < len(nums):
            cur_sum = sum(nums[left:right + 1])
            maximum = max(maximum, cur_sum)  # left up to right inclusive

            # case we move both pointers forward because next value is larger than the whole sum we've created so far
            next_index = right + 1
            if next_index < len(nums) and cur_sum <= 0:
                left = next_index
                right = next_index
            else:
                right = next_index  # increment right because we're expanding the current subarray to find larger maximum

        return maximum

    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        next_index = 1
        maximum = nums[0]
        cur_sum = nums[0]

        len_nums = len(nums)
        while next_index < len_nums:
            if cur_sum < 0:
                cur_sum = nums[next_index]  # Current sum is negative so reset sum to current value
            else:
                cur_sum = cur_sum + nums[next_index]  # Current sum is positive, append next value to accumulate sum

            next_index = next_index + 1
            maximum = max(maximum, cur_sum)

        return maximum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 20]))
print(s.maxSubArray([1]))
