Attempt:

My attempt was as follows:

1) loop through all num in nums
2) If num not in ranges dictionary, add the values lower/higher than num
   3) e.g 2, we would add ranges[1] = 1, ranges[3] = 1
3) else if num in ranges
   4) Extend range in the negative direction or positive direction, depending on which end we are at
      5) e.g 3, add ranges[4] to ranges
   5) Increment values at range extremities (1 and 4) = ranges[3] + 1
6) return maximal range at the end

Code was complex and time comsuming to write. Test time would expire



Attempt 2:

1) convert nums to set
2) for each num in nums set
3) if num - 1 in set, continue (we're not at the start of a sequence)
4) else (we're at start of a sequence)
   5) is num + 1 in sequence?
   6) num + 2 in sequence?
   7) etc ...
   8) set maximum = max(maximum, current_sequence_length)
9) return maximum

runtime beat 74%, memory 70%