
1. countbetween
- given array and low/high array with ranges
- arr = [1,3,5,6,8] low=[2], high=[6]
- Return [x, y] where x is the number of elements in arr between low[0] and high[0], y would be low[1], high[1] etc
- Time limit exceeded in early testing
    - Look for optimal solution

<br>

2. Min friends/max friends. What is the largest minimal connected graph in a graph with n nodes and e edges where all edges/nodes have to be used
- Need to look at how to find connected graphs within an undirected graph

<br>

3. fruit/prices arrays verifying array manipulation (very easy no need to go over)

<br>

4.  

<br>

5. binary superBits
- Given n=int and bitStrings=[]
- e.g n=6 bitString=[2,6]
- Find all possible superBitString for all bitStrings in array provided
- Length of binary = n so 2="10" which is made to be "000010" and then all superBitString combos are found from there
- superBitString = where zero or more 0s are flipped and changed to 1
- bitString = "010", superBitStrings are "110", "011", "111" and "010"
- Make a union of all superBitStrings and return the length of it