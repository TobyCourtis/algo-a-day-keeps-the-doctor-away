Attempt:

1. Loop through all intervals saving "current_start" and "current_end"
2. See if "current_end" in next interval
    3. If yes, increment interval and do step 2 again
    4. If no, break
4. Append [x, y] to output where x is start from step 1 and y is the 'end' from step 2 (which may be many intervals on
   from the initial interval)
5. Begin step 1 from the interval reached in step 2.
6. Return out

NB - changes were made to also compare initial start value to start value from intervals later in intervals list

NB 2 - Had so many issues for a long time because I **!assumed!** that the list was sorted. Sorting was vital and solved
all issues.

Runtime - Beat 98%, memory beat 53%





<br>
<br>

Optimal:

Just written cleaner. Works to update end value in output arr.