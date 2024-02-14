Attempt:

Case: "catsandog", ["cats", "dog", "sand", "and", "cat"]
1. loop through input string increasing the current substring by 1 each time
   2. c, ca, cat ....
3. if substring in word_dict, remove substring from start of word and repeat for remaining characters
   4. remove "cat", continue with "sandog"
5. Recursively do this and if the leftover string is empty ("") then return True
6. If we never reach the end case for all substrings, return False

Worked. Time limit exceeded.

caching - runtime beat 71%, memory 65%

<br>
Attempt 1.1 (match word_dict to string not substring to word_dict):

Slighty more performant

- wordDict is going to be smaller than the max size of the string (question states this)

- Rather than look for each substring of the word in word_dict we'll look for each word in word_dict being in the string instead
  - This is more efficient
  - We can then jump to next input string of `string[len(word):]` 

e.g is any word from ["leet", "code"] in "leetcode", yes, repeat with "code" etc.

<br>
Attempt 2 (dynamic programming):

Take a bottom up approach. Case "leetcode" again. See wordBreak() for implementation.

DP[8] = '' = True (empty string)

DP[7] = 'e' = False

DP[6] = 'de' = False

DP[5] = 'ode' = False

DP[4] = 'code' = True

DP[3] = 'tcode' = False

DP[2] = 'etcode' = False

DP[1] = 'eetcode' = False

DP[0] = 'leetcode' = True


DP[0] matches leet so we go to DP[0 + len('leet')]
DP[4] = True
DP[8] = True

Runtime beat 71, memory 65.