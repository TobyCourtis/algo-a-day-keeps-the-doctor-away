#!/bin/python3

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    totalArea = 0
    for i in range(len(A)):
        for j in range(len(A)):
            surfaceAreaAtCell = 0
            stackSizeAtCell = A[i][j]
            if stackSizeAtCell == 0:
                continue  # add no area on

            surfaceAreaAtCell += 2  # top and bottom area added

            # check all four sides around the current cell to see how much area of current
            # cell is blocked by other blocks
            newJ = j - 1
            if newJ < 0:
                # overflow means checking against empty region so all of that side is exposed
                surfaceAreaAtCell += stackSizeAtCell
            else:
                surfaceAreaAtCell += find_remaining_SA(i, newJ, A, stackSizeAtCell)

            newI = i - 1
            if newI < 0:
                # overflow means checking against empty region so all of that side is exposed
                surfaceAreaAtCell += stackSizeAtCell
            else:
                surfaceAreaAtCell += find_remaining_SA(newI, j, A, stackSizeAtCell)

            newJ = j + 1
            if newJ >= len(A):
                # overflow means checking against empty region so all of that side is exposed
                surfaceAreaAtCell += stackSizeAtCell
            else:
                surfaceAreaAtCell += find_remaining_SA(i, newJ, A, stackSizeAtCell)

            newI = i + 1
            if newI >= len(A):
                # overflow means checking against empty region so all of that side is exposed
                surfaceAreaAtCell += stackSizeAtCell
            else:
                surfaceAreaAtCell += find_remaining_SA(newI, j, A, stackSizeAtCell)

            totalArea += surfaceAreaAtCell

    return totalArea


def find_remaining_SA(i, j, A, stackSizeAtCell):
    remainingArea = stackSizeAtCell - A[i][j]
    return 0 if remainingArea < 0 else remainingArea


if __name__ == '__main__':
    A = [[1, 3, 4],
         [2, 2, 3],
         [1, 2, 4]]

    result = surfaceArea(A)
    print(result)
