list_input = [1, 8, 6, 2, 5, 4, 8, 3, 7]


class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = -1
        left, right = 0, len(height) - 1

        while left < right:
            distance_between = right - left
            min_height = min(height[left], height[right])
            max_area = max((distance_between * min_height), max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


s = Solution()
print(s.maxArea(list_input))
