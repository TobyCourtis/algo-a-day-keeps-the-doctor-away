from typing import List


class Solution:

    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left = top = 0
        right = bottom = len(matrix) - 1

        max_index = len(matrix) - 1

        while left < right:
            # could have made this simpler by doing i in range(right - left) and then it's left + index etc
            for i in range(left, right):
                tmp = matrix[top][i]

                matrix[top][i] = matrix[max_index - i][left]  # bottom left

                matrix[max_index - i][left] = matrix[bottom][max_index - i]  # bottom right

                matrix[bottom][max_index - i] = matrix[i][right]  # top right

                matrix[i][right] = tmp

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Simpler method where index goes from 0 to right - left    and index is appended or decremented
        """
        left = 0
        right = len(matrix) - 1

        while left < right:
            for index in range(right - left):
                top, bottom = left, right

                tmp = matrix[top][left + index]

                matrix[top][left + index] = matrix[bottom - index][left]  # top left set to bottom right

                matrix[bottom - index][left] = matrix[bottom][right - index]  # bottom left set to bottom right

                matrix[bottom][right - index] = matrix[top + index][right]  # bottom right set to top right

                matrix[top + index][right] = tmp

            left += 1
            right -= 1

        return


s = Solution()
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# s.rotate(matrix)
#
# for row in matrix:
#     print(row)

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
s.rotate(matrix)

for row in matrix:
    print(row)
