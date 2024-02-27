Attempt:

Naive method

1. For each char in the string (cur)
2. while next char == cur or k > 0:   # essentially do we have a repeating sequence and if the next char isn't the same
   as the first char in sequence, decrement k
    3. if next char != cur:   k -= 1  (we decrement the k count we have left)
3. return max length sequence found for all substrings

Time limit exceeded.

<br>

Neetcode (two pointers, sliding window)

For each substring we build a map of "char: occurrence count". The substring is valid iff length_substring -
most_occurring_char >= k:

Case: "ABBB", k = 1. length (4) - max (3) >= 1 # True so 4 is max string.

1. begin with a left and right pointer at 0
2. if (length substring l to r) - (count max occurring char in string) >= k
    3. r += 1 # extend sliding windows
3. else
    4. l -= 1 # decrease sliding window size
4. if (length sub string) > maxiumum: maximum = length

runtime beat 70%, memory 47%. 


