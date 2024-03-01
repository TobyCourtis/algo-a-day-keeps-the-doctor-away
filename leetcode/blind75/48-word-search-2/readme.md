attempt:

1. Use Trie to store all the words in the words array
2. GO through every cell on board
3. dfs() for each cell, trying all combos in the prefix Trie. 
   1. So if we're on "a", do dfs() on every word that starts with "a" which can be efficiently foudn using the Trie



NB - for the Trie to decrease computation, we pass the node into the dfs() rather than searching the tree every time we simply say is board[i][j] in node.children.


See refactored for a cleaner base case in dfs().

Runtime beat 50%, memory 53%