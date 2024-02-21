Attempt (O(log n)):

We know O(log n) usually means a binary search so we need to create binary search with some additional logic

Take first, last = nums[0], nums[-1]

- If last < first then custom logic required for rotated array
- Else, in order so return first (it's the smallest)

Custom logic:

1. If midpoint of array is less than midpoint - 1 then return midpoint (it's smallest elem)
2. If midpoint - 1 < last
    3. Then lowest is in LHS, nums = nums[:midpoint]
3. Else
    4. Then lowest is in RHS, nums = nums[midpoint:]
4. When we keep running this algorithm, we return lowest point eventually

Runtime beat 98%, memory 50%