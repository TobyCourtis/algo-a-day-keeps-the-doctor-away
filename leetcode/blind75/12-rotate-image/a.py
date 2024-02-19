class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        # note matrix is always square n == m
        left, right = 0, len(matrix) - 1

        while left < right:
            for index in range(right - left):
                top, bottom = left, right  # having 4 vars makes logic below more readable

                t_left = matrix[top][left + index]

                # bottom left to top left
                # 2,0   1,0   0,0       tl = 0,0   0,1       0,2
                matrix[top][left + index] = matrix[bottom - index][left]

                # bottom right to bottom left
                matrix[bottom - index][left] = matrix[bottom][right - index]

                # top right to bottom right
                matrix[bottom][right - index] = matrix[top + index][right]

                # top right to top left
                matrix[top + index][right] = t_left

            left += 1
            right -= 1



s = Solution()
s.rotate([[1, 2, 3],  # [7,4,1]
          [4, 5, 6],  # [8,5,2]
          [7, 8, 9]])  # [9,6,3]
