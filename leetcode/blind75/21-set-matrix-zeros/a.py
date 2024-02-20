class Solution:
    def setZeroesFirst(self, matrix: list[list[int]]) -> None:
        """
        O(m + n) space complexity, O(m * n) time
        """
        rows = set()
        cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        return

    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        O(1) space complexity, O(m * n) time
        """

        # we are going to override the cell indicating if first row should be zeroed
        # the cell [0][0] will record if first column should be zeroed, we also need to capture if
        # first row should be zeroed
        first_row = False

        # first row will reflect per cell if each corresponding column should be zeroed
        # first column will reflect per call if each corresponding row should be zeroed
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    # for first row, we want [0][0] to indicate that 0th column should be zero, NOT row.
                    if i == 0:
                        first_row = True
                    else:
                        matrix[i][0] = 0  # row indicator

                    matrix[0][j] = 0  # col indicator

        # excluding row 0 and col 0, zero the rest of the matrix if the 0th row/col has a 0 in corresponding cell
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # change first col
        # if any in first col are 0 then make them all 0
        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        # change first row
        if first_row:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        return


s = Solution()
# s.setZeroes([[0, 1, 2, 0],
#              [3, 4, 5, 2],
#              [1, 3, 1, 5]])
# s.setZeroes([[1, 1, 2, 0],
#              [3, 4, 5, 4],
#              [1, 3, 1, 5]])
m = [[1, 1, 1],
     [1, 0, 1],
     [1, 1, 1]]
s.setZeroes(m)
for row in m:
    print(row)
