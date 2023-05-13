#!/bin/python3

import os


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    minScore = scores[0]
    maxScore = scores[0]
    max_min_times_array = [0, 0]
    for i in range(1, len(scores)):
        if scores[i] < minScore:
            minScore = scores[i]
            max_min_times_array[1] += 1
        if scores[i] > maxScore:
            maxScore = scores[i]
            max_min_times_array[0] += 1
    return max_min_times_array


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
