Attempt:

Same as meeting rooms 1 but with additonal constraints.

If a meeting overlaps multiple meetings, do any of the overlapped meetings overlap?

General approach, we need to find the maximum overlapping number of meetigns at any one time

1. sort input
2. create start times array and end times array. sort them both.
3. Go every time we hit a start time += 1 to count (multiple running)
4. Every time we hit an end time, -= 1 to 0count (one has stopped running)
5. return count

Could not run due to premium leetcode problem. 