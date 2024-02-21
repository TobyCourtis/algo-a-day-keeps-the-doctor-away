Attempt:

Issue:

1. [-1, 5, 5] max = 25
2. [-1, 5, 5, -1] max = 25

We have to do a search from each elem in the array because of case 2.

If we encounter 0 we should always break (as there is no chance of improving)

Time limit exceeded, O(n^2)

<br>

Attempt 2 (Neetcode dynamic programming):

Essentially for each subarray we keep track of a max and a min product. Given there could be an odd or even number of
negatives this is required.

- Case: [-1, -2, -3]

- [-1, -2] > min = -2, max = 2

- Now [-1, -2, -3] our min = -6 (max * -3), max = 6 (min * -2)

If we hit a 0, we reset min/max to 1 as this resets our searching process. 

Runtime beat 97%, memory 92%