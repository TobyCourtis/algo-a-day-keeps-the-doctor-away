Attempt:

See my pseudo code for an attempt which had time limit exceeded. O(n^2) to produce the overlap map.



Neetcode (sort by start):

1. sort by start val. end = intervals[0][1]
2. for start, end in intervals[1:]
   3. if start >= prev_end   # non overlapping case and prev_end = end
   4. else  # overlapping case - previous end should be set to the lower value of the two end values. 
      5. removed count += 1
      6. we have effectively removed the interval with the larger end value because this interval had more chance of overlapping with the next interval


Runtime beat 87%, memory beat 55% 