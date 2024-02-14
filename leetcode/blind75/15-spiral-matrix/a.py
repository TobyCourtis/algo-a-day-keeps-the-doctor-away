class Solution:

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        out = []

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:

            # right
            for i in range(left, right):
                out.append(matrix[top][i])
            top += 1

            # down
            for i in range(top, bottom):
                out.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break  # have to do this check as we could have printed every value already

            # left
            for i in range(right - 1, left - 1, -1):
                out.append(matrix[bottom - 1][i])
            bottom -= 1

            # up
            for i in range(bottom - 1, top - 1, -1):
                out.append(matrix[i][left])
            left += 1

        return out


s = Solution()
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
