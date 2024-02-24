attempt:

Fairly trivial, we are designing a method of storing where the word ends when encoding so that we can create the input list when decoding.

Idea:

1. for each word ["leet", "code"]
2. encode: length(word) + "#" + word e.g 4#leet
3. When decoding, parse the count up to # value (e.g 4) and then from the index after the hashtag, we add the word of length 4
   4. So `4#leet` adds 'leet' to the decode output list and then moves on to the next word




Could not run code as it's a premium problem