class Solution:
    def existAttempt1(self, board: list[list[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    index = 1
                    tmp_i = i
                    tmp_j = j
                    while index < len(word):
                        if (tmp_i - 1, tmp_j) not in visited:
                            up = board[tmp_i - 1][tmp_j] if tmp_i > 0 else None
                            if up == word[index]:
                                index += 1
                                visited.add((tmp_i - 1, tmp_j))
                                tmp_i -= 1
                                continue
                        if (tmp_i + 1, tmp_j) not in visited:
                            down = board[tmp_i + 1][tmp_j] if tmp_i < len(board) - 1 else None
                            if down == word[index]:
                                index += 1
                                visited.add((tmp_i + 1, tmp_j))
                                tmp_i += 1
                                continue
                        if (tmp_i, tmp_j - 1) not in visited:
                            left = board[tmp_i][j - 1] if tmp_j > 0 else None
                            if left == word[index]:
                                index += 1
                                visited.add((tmp_i, tmp_j - 1))
                                tmp_j -= 1
                                continue
                        if (tmp_i, tmp_j + 1) not in visited:
                            right = board[tmp_i][tmp_j + 1] if tmp_j < len(board) - 1 else None
                            if right == word[index]:
                                index += 1
                                visited.add((tmp_i, tmp_j + 1))
                                tmp_j += 1
                                continue

                        break  # wasn't in any surrounding cell
                    if index >= len(word):
                        return True

        return False

    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, index):
            if index == len(word):
                return True

            if (r < 0 or
                    c < 0 or
                    r >= rows or
                    c >= cols or
                    word[index] != board[r][c] or
                    (r, c) in visited):
                return False

            visited.add((r, c))

            result = (
                    dfs(r, c + 1, index + 1) or  # right
                    dfs(r + 1, c, index + 1) or  # down
                    dfs(r, c - 1, index + 1) or  # left
                    dfs(r - 1, c, index + 1)  # up
            )

            # if the very first call was 0,0 which was "H" whilst search for "HELLO"
            # if we reach the line below, H and all of it's neighbours have recursively been visited
            # therefore we can remove it from visited now.
            visited.remove((r, c))  # now we've visited every possible cell in the recursion above, remove (r, c) from
            # visited so it can be visited in future calls to dfs()

            return result

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False


s = Solution()
# print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
# print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
print(s.exist([["a", "a"]], "aaa"))
