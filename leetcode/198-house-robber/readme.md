Attempt:

We can break the problem up into subproblems

rob = max(arr[0], + rob[2:])   # 0th index, skip 1 then 2nd index to the end
rob = max(rob, max(arr[1] + rob[3:]))  # first index, skip 1 then 3rd index to end

rob[x:]  # this is a subproblem (max of rest of array)

These two combinations are all we need to compute the max robbing amount.

The approach coding:

1. Loop through each num in nums
2. For each, compute the maximal value up to this point and save it in the current array position.
    3. Two cases (we take the larger value):
        1. We take current num + previous rest of array count
        2. We do not use current num, we just take the adjacent value instead which is larger
    4. Example:
        5. [1,2,3,1]
        6. index 0 = 1
        7. index 1 = 2
        8. index 2 = max(index 1, current + previous rest of array) = max(2, 3 + 1) = 4
        9. index 3 = max(index 2, current + previous rest of array) = max(4, 1 + 2) = 4 again
    3. Note - We only ever need to maintain the previous 2 max values. Either we take adjacent val OR the val before
       that.
4. return final max value find (in the example above it's index 3)