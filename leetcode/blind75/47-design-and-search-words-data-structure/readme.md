Attempt 1:

Looks very similar to the Trie implemented in another leetcode problem with additional logic.

My attempt was very close and I could not repeat a failing test on leetcode.com locally. I presume it was not performant
enough.

General idea:

- When we begin the pool of searchable next nodes is root.children
- If we encounter a ".", the pool increases to every child of current the children
- If no children match the next character, return False
- If final character has "isEnd" = False then return False
- Else True (word was found)

<br>

Neetcode:

Very similar code to mine, but he used dfs().

See search() commented code. If a "." is encountered, we call dfs() with the remaining word, for all children of current node.



Runtime beat 32%, memory 16%