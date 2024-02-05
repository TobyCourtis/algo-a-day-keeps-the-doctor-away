Initial attempt:

- The general logic in this problem was okay, I ended up with many edge cases which meant reaching first submission took me a lot longer than expected
- See code comments for approach

1. start val is either within an existing interval OR we need a new interval
   2. Find index and insert new interval if required
2. end is either in existing interval OR not 
3. From step 1 we have our new or modified interval. Called 'current'
   4. Case 1: 'end' lies in a pre-existing interval. We need to take the end of that interval and make it the end of 'current'
   5. Case 2: end is not in another interval and we need to update 'current' to end at 'end'.
4. Remove overlapping intervals

Submission
Beat 57% runtime, 56% memory (both green as correct O(n)) 

<br>
Optimal:

- Slightly cleaner approaches but same complexity. I'm happy to call mine optimal. 