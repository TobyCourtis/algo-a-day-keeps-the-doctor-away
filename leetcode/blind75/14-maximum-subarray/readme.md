My attempt:

NB - see solutions one/two for my first approach

General approach:
1. sum is set to first value
2. `sum = sum + next_val`
   3. `max = max(max, sum)`
4. If sum is negative, reset `sum = next_val` (begin accumulation again)
5. Increment next_val


Attempt 1:

- Incorrectly implemented step 3 where I only reset sum when next index is greater than maximum.
- This was incorrect as you shouldn't be resetting the accumulating sum IF the previous sum is still positive

Case:

`[2,3,-4,10]`

- When we get to `10` we shouldn't reset the total to `10` as `2 + 3 -4 = 1`  
- Instead just append 10 to the positive sum (1)
- max = `11`

Attempt 2:

- Good approach, time limit exceeded. O(n^2) due to use of sum() func in each loop


Attempt 3:

- I didn't like that I was using sum() function every loop
- Successfully implemented solution where I keep track of 'current sum' and then we append the next_value to that sum or reset the sum when required

Submission:
Beat 71% runtime, 70% memory







<br>
Optimal:
Mine was optimal