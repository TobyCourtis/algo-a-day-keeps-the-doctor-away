- Initial thoughts:
- Approach appears messy but the logic was sound
1. For every char
2. check if chars left and right are equal, continue until left and right are not equal. Each time they are equal, a new palindrome was created and if this is the longest we've seen then save it as longest
    - Works for "cabad" not "abbd" 
3. Check if the previous char and current char are equal then repeat the end of step 2
   - WOrks for "abbd" as well now

Initial submission:
Beat 50% in runtime, 66% in memory. Double while loop was inefficient.

Optimal (more optimised version of my own without 2 while loops):
To enumerate all palindromic substrings of a given string, we first expand a given string at each possible starting position of a palindrome and also at each possible ending position of a palindrome and keep track of the length of the longest palindrome we found so far.

Approach :

We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and there are only 2n - 1 such centers.
You might be asking why there are 2n - 1 but not n centers? The reason is the center of a palindrome can be in between two letters. Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's.'
Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).
Algorithm :

At starting we have maz_str = s[0] and max_len = 1 as every single character is a palindrome.
Now, we will iterate over the string and for every character we will expand around its center.
For odd length palindrome, we will consider the current character as the center and expand around it.
For even length palindrome, we will consider the current character and the next character as the center and expand around it.
We will keep track of the maximum length and the maximum substring.
Print the maximum substring.
Complexity Analysis

Time complexity : O(n^2). Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).

Space complexity : O(1).

Code