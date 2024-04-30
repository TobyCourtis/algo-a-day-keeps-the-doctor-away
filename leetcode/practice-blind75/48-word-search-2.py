from typing import List


class TrieNode:

    def __init__(self, val, isEnd=False):
        self.val = val
        self.children = {}
        self.isEnd = isEnd

    def insertChar(self, c):
        if c not in self.children:
            self.children[c] = TrieNode(c)
        return self.children[c]


class Trie:

    def __init__(self):
        self.root = TrieNode("ROOT")

    def insert(self, word):
        prev = self.root
        for char in word:
            prev = prev.insertChar(char)
        prev.isEnd = True

    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.isEnd


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. load words into a Trie
        # 2. for each cell on board
        # 3. begin seeing in cur in trie
        # 4. if yes, go one node deeper and one letter deeper
        trie = Trie()
        for word in words:
            trie.insert(word)

        found = set()
        visited = set()

        def dfs(i: int, j: int, node: TrieNode, word: str = ""):
            if (
                    i < 0 or
                    i > len(board) - 1 or
                    j < 0 or
                    j > len(board[0]) - 1 or
                    (i, j) in visited
            ):
                return
            cur_char = board[i][j]
            if cur_char not in node.children:
                return
            word += cur_char
            node = node.children[cur_char]
            if node.isEnd:
                found.add(word)

            visited.add((i, j))

            dfs(i, j - 1, node, word)
            dfs(i, j + 1, node, word)
            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)

            visited.remove((i, j))  # removing once all dfs is done making it free to search again

            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie.root)

        return list(found)


s = Solution()
print(s.findWords(board=[["o", "a", "a", "n"],
                         ["e", "t", "a", "e"],
                         ["i", "h", "k", "r"],
                         ["i", "f", "l", "v"]],
                  words=["oath", "pea", "eat", "rain"]))
# Output: ["eat","oath"]
