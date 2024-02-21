Attempt 1:

Add all values to a stack then rebuild head by alternately taking from start or end of stack.

Beat 12% run, 50% memory


Attempt 2 (neetcode):

1. Split list in half
2. take second half and reverse it
3. merge the two lists
   4. Take one from firstHalf, next = one from secondHalf etc

runtime beat 31%, memory 72%