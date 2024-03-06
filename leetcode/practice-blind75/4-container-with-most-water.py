from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height) - 1
        l, r = 0, n

        max_area = 0
        while l < r:
            cur_area = (r - l) * min(height[l], height[r])

            max_area = max(max_area, cur_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

# runtime beat 69%
