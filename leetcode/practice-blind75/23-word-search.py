from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(i, j, word_index):
            if ((i, j) in visited or
                    i < 0 or
                    i > len(board) - 1 or
                    j < 0 or
                    j > len(board[0]) - 1 or
                    board[i][j] != word[word_index]):
                return False

            visited.add((i, j))

            if word_index == len(word) - 1:
                return True

            result = (
                    dfs(i, j - 1, word_index + 1) or
                    dfs(i, j + 1, word_index + 1) or
                    dfs(i - 1, j, word_index + 1) or
                    dfs(i + 1, j, word_index + 1)
            )

            visited.remove((i, j))  # crucial to solve.

            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
                visited = set()

        return False


s = Solution()
# print(s.exist([["A", "B", "C", "E"],
#                ["S", "F", "C", "S"],
#                ["A", "D", "E", "E"]], "ABCCED"))
# print(s.exist([["A", "B", "C", "E"],
#                ["S", "F", "C", "S"],
#                ["A", "D", "E", "E"]], "TOBYC"))

# print(s.exist([["A", "B", "C", "E"],
#                ["S", "F", "C", "S"],
#                ["A", "D", "E", "E"]], "ABCB"))
print(s.exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"))
