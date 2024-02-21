import math


class Solution:
    def maxProductFirstAttempt(self, nums: list[int]) -> int:
        maximum = - math.inf

        for i in range(len(nums)):
            count = 1
            for j in range(i, len(nums)):
                current_num = nums[j]
                if current_num == 0:
                    maximum = max(maximum, 0)
                    break
                else:
                    count *= current_num
                # save current count if greater than maximum
                maximum = max(maximum, count)

        return maximum

    def maxProduct(self, nums: list[int]) -> int:
        output = max(nums)  # base case, output is largest single value in nums

        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            tmp_max = curMax * n  # so we don't use new curMax when finding curMin below
            curMax = max(n * curMax, n * curMin, n)  # n could be positive or negative
            curMin = min(tmp_max, n * curMin, n)  # again either combo could produce a minimum
            output = max(output, curMax)

        return output


s = Solution()
# print(s.maxProduct([2, 3, -2, 4]))
print(s.maxProduct([-2, 0, -1]))
