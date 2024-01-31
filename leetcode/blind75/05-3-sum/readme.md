Initial thoughts:

1. For each value in nums [-1,0,1,2,-1,-4]
2. `nums[i] + x + y = 0`
3. We basically have a 2 sum problem now for each value
4. Given `0 - nums[i] = x + y`, find all combos x and y
   1. Iterate through all values in nums `for x in nums`
   2. `y = - first_value - x`
   3. Check if y is in nums, given current value of x in formula
   3. Add `(nums[i], x, y)` for all found combinations where y exists in nums

Initial submission:
Beat 37% runtime, 5% memory


<br>
Optimal:

I knew already given the time constraints I hadn't created an optimal solution

<br>
The optimal approach isn't far from the approach i took with a few smarter steps

1. sort nums
2. Create a twosum solution using two pointers left and right
3. total = nums[i] + nums[left] + nums[right]
4. If total is less than 0 we are too negative and need to increment left pointer by one (because it's a sorted list this means we're getting less negqative)
5. If total is greater than 0, too positive, decrement right pointer
6. If total == 0 then create triplet
7. Increment left pointer over all duplicate occurrences of nums[left] to avoid recomputing
8. Repeat 7 by decrementing right


TLDR - A cleaner optimal approach but initial logic was sound. "find_two_sum()" could have been improved

