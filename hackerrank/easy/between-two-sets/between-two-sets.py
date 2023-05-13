#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    foundFactors = []
    # from max in A TO min in B?
    maxA = max(a)
    minB = min(b)
    possibleFactor = maxA
    while possibleFactor <= minB:
        found_factor = True
        for elem in a:
            if possibleFactor % elem != 0:
                found_factor = False

        for elem in b:
            if elem % possibleFactor != 0:
                found_factor = False

        if found_factor:
            foundFactors.append(possibleFactor)
        possibleFactor += maxA

    return len(foundFactors)

if __name__ == '__main__':
    arr = list(map(int, "3 4".rstrip().split()))

    brr = list(map(int, "24 48".rstrip().split()))

    total = getTotalX(arr, brr)
    print(total)