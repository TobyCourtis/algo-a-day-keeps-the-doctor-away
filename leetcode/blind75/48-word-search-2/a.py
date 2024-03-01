from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)

        m = len(board)
        n = len(board[0])

        output = set()
        visited = set()

        def dfs(i, j, node, word=""):
            if (i, j) in visited:
                return
            if board[i][j] not in node.children:
                return

            node = node.children[board[i][j]]
            word += board[i][j]

            if node.isEnd:
                output.add(word)

            visited.add((i, j))

            if j < n - 1:
                dfs(i, j + 1, node, word)  # right
            if j > 0:
                dfs(i, j - 1, node, word)  # left
            if i < m - 1:
                dfs(i + 1, j, node, word)  # down
            if i > 0:
                dfs(i - 1, j, node, word)  # up

            visited.remove((i, j))

            return

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return list(output)


class SolutionRefactored:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)

        rows = len(board)
        cols = len(board[0])

        output = set()
        visited = set()

        def dfs(i, j, node, word=""):
            if (
                    i < 0 or
                    j < 0 or
                    i == rows or
                    j == cols or
                    (i, j) in visited or
                    board[i][j] not in node.children
            ):
                return

            visited.add((i, j))

            word += board[i][j]
            node = node.children[board[i][j]]

            if node.isEnd:
                output.add(word)

            dfs(i, j + 1, node, word)  # right
            dfs(i, j - 1, node, word)  # left
            dfs(i + 1, j, node, word)  # down
            dfs(i - 1, j, node, word)  # up

            visited.remove((i, j))

            return

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return list(output)


s = Solution()
print(s.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                  ["oath", "pea", "eat", "rain"]))
print(s.findWords([["a"], ["a"]],
                  ["aaa"]))
print(s.findWords([["a"]], ["a"]))

print("")
s = SolutionRefactored()
print(s.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                  ["oath", "pea", "eat", "rain"]))
print(s.findWords([["a"], ["a"]],
                  ["aaa"]))
print(s.findWords([["a"]], ["a"]))
