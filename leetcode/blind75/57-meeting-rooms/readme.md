Attempt:

Best we can do is to sort the list of intervals before we begin solving. O(n log n).

1. sort by START value
2. iterate through intervals
    3. if current meeting END is after next meeting START, return False
3. return True if all pass

Was not able to run on neetcode due to it being a premium problem.e