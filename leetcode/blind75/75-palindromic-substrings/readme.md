attempt:

Plan was for every substring in 's', check if it's a palindrome.

O(n^2) to go through each substring and O(n) to check isPalindrome = O(n^3)

<br>

Neetcode:

Loop through every char in s, treating the current char as the MIDDLE of the palindrome.

Drastically reduces computation. O(n) to loop through and O(n) to check palindrome = O(n^2 solution).

<br>

case "bab"

1. we loop through string in O(n)
2. when using left and right pointers, the worst case for checking palindromes is n steps.
   3. "a" is palindrome
   4. a-1 == a+1 (b == b) is palindrome 
      5. This constant time step can take place at most n / 2 times for each char = O(n)

Therefore complexity = O(n^2)

