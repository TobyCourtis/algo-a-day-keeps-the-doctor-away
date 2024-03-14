from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def setZeroes(self, matrix: list[list[int]]) -> None:
            """
            O(1) space complexity, O(m * n) time
            """

        first_row = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = True
                    else:
                        matrix[i][0] = 0  # row indicator

                    matrix[0][j] = 0  # col indicator

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        if first_row:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        return


s = Solution()
matrix = [[1, 1, 1],
     [1, 0, 1],
     [1, 1, 1]]

s.setZeroes(matrix)
for row in matrix:
    print(row)

