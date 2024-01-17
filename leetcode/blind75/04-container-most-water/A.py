list_input = [1, 8, 6, 2, 5, 4, 8, 3, 7]


class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = -1
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                distance_between = j - i
                min_height = min(height[i], height[j])
                max_area = max((distance_between * min_height), max_area)
        return max_area


s = Solution()
print(s.maxArea(list_input))
