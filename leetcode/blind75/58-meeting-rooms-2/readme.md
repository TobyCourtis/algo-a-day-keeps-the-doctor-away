Attempt:

Same as meeting rooms 1 but with additional constraints.

If a meeting overlaps multiple meetings, do any of the overlapped meetings overlap?

General approach, we need to find the maximum overlapping number of meetings at any one time

1. sort input
2. create start times array and end times array. sort them both.
3. Go every time we hit a start time += 1 to count (multiple running)
4. Every time we hit an end time, -= 1 to count (one has stopped running)
5. return count

Could not run due to premium leetcode problem. 


<br>
<br>

Open Q - why does this work separately sorting start/end times?

### Example 1 (work through):

if we had meetings: [0, 5], [10, 15], [20, 30]

start = [0, 10, 20]

end =   [5, 15, 30]

start 0 so count += 1

end 5 < start 10 so count -= 1

start 10, end 15 so + 1

e15 -1

s20 +1

e30 -1

max count = 1

<br>

### Example 2:

In contrast, when overlapping e.g [0, 30], [10, 15], [20, 25]

start = [0, 10, 20]

end = [15, 25, 30]

s0 += 1

s10 += 1

e15 -= 1

s20 += 1


max count = 2


 as we can see in example 2, the lowest end time is 15 and two start times start before 15, therefore, 
 we get a count of two.
 
#### THIS is why the method works ^^