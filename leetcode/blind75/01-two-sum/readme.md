Initial thoughts:

- Attempted to make the algorithm too efficient too fast
- Fell back on the most intuitive O(n^2) approach with a nested for. If first loop element + second loop element = target then return result

First attempt: beat 7% speed, 81% memory

Optimising myself:
Thoughts:
- Sorting will reduce the time complexity, increase space
- Need to create list that keeps track of original index i.e list of tuples


Execution:
- RTFQ - I did not account for negatives which wasted a great deal of time
- Changed to dictionary for increased lookup time

Second optimised attempt: beat 52% runtime (good for twosum), 23% memory 


Optimal (runtime):
Not far from what I had in second attempt, there are a few ways to make it simpler (read optimal.py comments):
1. Don't have list of values in the hash table, just the index
2. By overriding values in hash table, we save the LAST occurring index of a number
3. 'Midpoint check' I do can be simplified by checking that current index of an element is different to hash table
    saved index and since we loop through nums start to finish, hash table will have a different index if it occurred
    twice. [3,3] target 6 would save index 1 in hash table and when looping through the array index 0 would != index 1
   and therefore we could return an answer [0, 1]. 

Optimal (space):
- Exactly what I had but "for j in range(len(nums)):" can be "for j in range(i+1, len(nums)):" to have 100% memory score