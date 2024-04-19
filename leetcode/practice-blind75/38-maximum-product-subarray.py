from typing import List


class Solution:
    """
    key is:

    - could be odd or even number of negative values
    - 0 'resets' the subarray search because it always makes arr sum 0
    -  for each subarray keep a curMin and curMax.
        - then [-1, 2, 2] min = -4 max = 4
    - at each step the max can be:
        1. curNum * max
        2. curNum * min
        3. curNum   (on its own)

    - at each step the min can be:
        1. curNum * max (this might be negative now)
        2. curNum * min (this could also be negative)
        3. curNum (again could be smallest)

    """

    def maxProduct(self, nums: List[int]) -> int:
        out = max(nums)

        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            new_max = curMax * n
            curMax = max(new_max, curMin * n, n)
            curMin = min(new_max, curMin * n, n)

            out = max(out, curMax)

        return out


s = Solution()
print(s.maxProduct([-2, 2, 2, -1]))
