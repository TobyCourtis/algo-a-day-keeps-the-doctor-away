attempt:

Would have been O(n) inserts and O(1) median find.

- maintain sorted list, with inserts requiring shuffling the rest of the list

<br>

Neetcode (heap and priority queue)

O(log(n)) inserts and O(1) median find.

1. create 'small' heap which is a maxHeap and 'large' which is a minHeap
   1. O(log n) to insert
   2. 'small' will be LHS of our overall array and 'large' the RHS. 
   3. if [3,2,1,4] are inserted: small=[1,2] large=[3,4]

addNum() implementation:

1. always add to small heap first as default
   1. in python, only min heap is implemented as default so we multiply the input by -1 to create a maxheap
2. (is all small <= all large)
   1. IF max(small) <= min(large): valid.
   2. ELSE remove max from small and add to large.
3. (uneven size heap check)
   1. IF small is 2 elems longer than large, remove from small and add to large
   2. ELIF large is 2 elems longer than small, remove from large and att to small


Runtime beat 77%, memory 49%.