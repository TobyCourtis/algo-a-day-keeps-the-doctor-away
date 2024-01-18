Very straight forward.

First submission beat 70% in terms of speed but only 30% in terms of memory.

Use of set over list makes this O(n) time and O(n) space.


Thoughts on how to avoid high memory use (higher time complexity though):
1. Sort list
2. see if ith item == i+1th item (loop through length of list - 1)
3. If equal then return True, else False

NB - Bizarrely I used exactly the same code and variable names as one of the solutions on l33tcode