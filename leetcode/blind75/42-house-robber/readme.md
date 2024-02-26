Attempt:

Fairly trivial, at each index we take max(current + (index(current) - 2), previous).

Case: [1, 2, 3, 1]

index:
0. Take 1
1. Take max(2, 1)
2. take max(current+index 0, index1) = max(4, 2)
3. take max(current+index 1, index3) = max(3, 4)