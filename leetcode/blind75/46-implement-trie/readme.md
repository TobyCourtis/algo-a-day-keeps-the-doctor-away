Attempt 1:

Seemed fairly trivial, Beat 82% runtime, 94% memory

1. insert word into words set 
2. insert each substring of that word into substrings set
3. Lookup search/startsWith is a lookup in set 1/2 respectively



Optimal (my attempt):

Should have actually implemented a Trie rather than answering the question.

- watched neetcodce and made notes on approach without looking at the code
- implemented Trie successfully first attempt


Optimal (neetcode):

Very similar in terms of complexity and implementation but a few differences made code cleaner and easier to understand

1. Nodes do not need a val as the 'val' (letter) is stored in the 'children' dictionaries
2. If we make the Trie `self.root = TrieNode()` this is cleaner than a standalone dict and makes search/insert functions easier
3. search/insert simply becomes going through each char in word and inserting in children if they do not exist.


See iPad for notes on Trie logic.