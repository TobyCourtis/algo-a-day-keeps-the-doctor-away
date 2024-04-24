Attempt:

Fairly trivial, at each index we take max(current + prevPrev, previous).

prevPrev = nums[current_index - 2]
prev = nums[current_index - 1]

Case: [1, 2, 3, 1]

example:
0. Take 1
1. Take max(2, 1)
2. take max(current+index 0, index1) = max(4, 2)
3. take max(current+index 1, index3) = max(3, 4)