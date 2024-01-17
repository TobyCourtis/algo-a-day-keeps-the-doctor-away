I made two attempts during the time limit:
1. Attempted O(n^2) two loops which fails reaching the time limit (expected but this was a first pass)

2. Attempted an improved O(n) method which begins a search from the front and back of the string at the same time, searching for the longest substring. Failed on a missed test case 'asjrgapa' as the search begins with a on both sides and resets at the next a it finds. In this case missing the large substring 'sjrgap' in the centre


Optimal:
In general I wasn't far from this method with my own two pointer method.

1. Keep track of a left pointer that starts at 0 and charSet (or just a string)
2. Loop through string with a right pointer that begins at 0 and goes to len(string)
3. If 'right' not in charSet then append to it. Update max_length if required where max length is the distance between the two pointers currently.
4. If 'right' is in the charSet then we need to remove from the charSet until 'right' is not in the charSet. We remove from the left hand side. We have a while loop that removes 'left' and increments it by 1 until 'right' is no longer in the charSet
5. Append 'right' to charSet
6. Continue from step 2

This method works as follows 'abzcdzef'

1. Record up to 'abzcd'
2. Remove a then b then z. Now we have 'cd'
3. Now we can append z then e then f 
4. We're left with 'cdzef'


