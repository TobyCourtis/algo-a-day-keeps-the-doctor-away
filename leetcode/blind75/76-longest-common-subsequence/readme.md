attempt:

1. find shortest
2. produce all combinations of (in order) characters
3. sort in descending order
4. for each combination, if it appears in order in the longer input string, set maxiumum to the length of the combination
5. return maximum

Time limit exceeded.

<br>

Neetcode:

Dynamic programming, 2D matrix, backtracking. See iPad notes for why the diagonal process makes sense. We have to cover each cell in the matrix so O(n*n).

1. Create matrix with text1 x text2. With an outer layer of 0s along bottom and right hand side

```
   | a   c   e
----------------
a |              | 0
b |              | 0
c |              | 0
d |              | 0
e |              | 0
-----------------
   0     0     0     
```

2. we start from bottom right and backtrack through every cell.
   3. If text1[i] == text2[j] then add 1 to current cell.
      1. To accumulate values we do dp[i][j] = 1 + dp[i+1][j+1] (diagonal value)
   4. If text1[char] != text2[char] then we do max(dp[i][j + 1], dp[i+1][j])
      1. The reason for doing this is we want to carry the largest value through the matrix
      2. case 'abcde' and 'aze'. e and e are a match in dp[4][2]
      3. we want to carry that 1 up and left through the matrix so when we reach cell dp[4][1] we take the 1 already created in cell dp[4][2]

```
   | a   z   e
----------------
a |             | 0
b |             | 0
c |             | 0
d |             | 0
e |           x | 0
----------------
     0   0    0
```

3. return dp[0][0] which is always the maximum value


runtime beat 86%, memory beat 35%
