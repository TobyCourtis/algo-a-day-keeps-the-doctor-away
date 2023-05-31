#!/bin/python3

import os


#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # we need to find the tallest stack and remove
    h1Sum = sum(h1)
    h2Sum = sum(h2)
    h3Sum = sum(h3)
    while (True):
        if any([h1Sum == 0, h2Sum == 0, h3Sum == 0]):
            return 0
        if h1Sum == h2Sum == h3Sum:
            return h1Sum
        minimum = min(h1Sum, h2Sum, h3Sum)
        while h1Sum > minimum:
            popped = h1.pop(0)
            h1Sum -= popped
        while h2Sum > minimum:
            popped = h2.pop(0)
            h2Sum -= popped
        while h3Sum > minimum:
            popped = h3.pop(0)
            h3Sum -= popped


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
