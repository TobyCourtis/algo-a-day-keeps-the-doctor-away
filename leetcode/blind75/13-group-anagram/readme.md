Attempt:

General idea:

1. For each word, build a character count of occurrences of chars in the word
2. Create list for words with same characters (anagrams)
3. return list of lists

Code for char count:

1. make array of length 26 ([0] * 26)
2. For each char in array:
   2. if 'a' array[0] += 1, 'b' array[1] += 1 etc ...
3. Result array = same for anagrams.
   4. tuple of this array = immutable identifier for a word
   5. output_map = tuple key : list(words with same identifier) e.g tuple : ['dog', 'god']
6. Return list of the output_map values as result