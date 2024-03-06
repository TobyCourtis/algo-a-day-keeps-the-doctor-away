from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # a + b + c = 0
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                b = nums[l]
                c = nums[r]
                threeSum = a + b + c

                # this section is two sum:
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, b, c])

                    l += 1  # increment left because we have used the left value already
                    while nums[l] == nums[l - 1] and l < r:
                        # keep incrementing left until it's value changes to avoid duplicates
                        l += 1

        return res


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
