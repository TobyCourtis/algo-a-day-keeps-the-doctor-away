attempt:

Fairly trivial, add occurrence counts to a hash map, order by values ascending and then return the two largest values.

Runtime beat 40%, memory 73%


<br>


Neetcode (bucket sort):

1. Begin the same by creating map of key:value referring to number:occurrence count
2. We initialise a frequency list of list where index = count and value array = the numbers in the input array that have the correesponding count
   3. e.g [1,1,1,2,2,100] k=2
   4. = [[], [100], [2], [1], [], [], []]  # index 1, 100 occurs once, index 3, 1 occurs 3 times
3. Iterate in reverse through the array created in step 2. Add k elements to an output array. Here we append 1 then 2 and output [1,2] 

Runtime beat 50%, memory 40%