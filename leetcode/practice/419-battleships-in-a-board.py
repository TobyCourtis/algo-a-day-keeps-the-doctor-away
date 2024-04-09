from typing import List


class Solution:

    def countBattleships(self, board: List[List[str]]) -> int:
        # 1. find x
        # 2. go either vertical or horizontal in search
        # 3. mark all as visited
        visited = set()
        m = len(board)
        n = len(board[0])

        ship_count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X" and (i, j) not in visited:
                    ship_count += 1
                    visited.add((i, j))
                    if ((i > 0 and board[i - 1][j] == "X") or
                            (i < m - 1 and board[i + 1][j] == "X")):
                        top, bottom = i - 1, i + 1
                        found = True
                        while found:
                            found = False
                            if top > 0 and board[top][j] == "X":
                                visited.add((top, j))
                                found = True
                                top -= 1
                            if bottom < m and board[bottom][j] == "X":
                                visited.add((bottom, j))
                                found = True
                                bottom += 1
                    else:
                        left, right = j - 1, j + 1
                        found = True
                        while found:
                            found = False
                            if left > 0 and board[i][left] == "X":
                                visited.add((i, left))
                                found = True
                                left -= 1
                            if right < n and board[i][right] == "X":
                                visited.add((i, right))
                                found = True
                                right += 1

        return ship_count

    """
    recursive looks clean and is the right order of magnitude O(m*n), but does more unnecessary steps which caused
    the solution to only be better than 20% in runtime. The iterative method above beat 60% of users.
    """

    def countBattleshipsRecursive(self, board: List[List[str]]) -> int:
        # 1. find x
        # 2. go either vertical or horizontal in search
        # 3. mark all as visited
        visited = set()
        m = len(board)
        n = len(board[0])

        def dfs(i, j, vertical: bool):
            if (i < 0 or
                    i >= m or
                    j < 0 or
                    j >= n or
                    board[i][j] != 'X' or
                    (i, j) in visited):
                return None

            visited.add((i, j))

            if vertical:
                # vertical
                dfs(i + 1, j, vertical)
                dfs(i - 1, j, vertical)

            else:
                # horizontal
                dfs(i, j + 1, vertical)
                dfs(i, j - 1, vertical)

        ship_count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X" and (i, j) not in visited:
                    ship_count += 1
                    if ((i > 0 and board[i - 1][j] == "X") or
                            (i < m - 1 and board[i + 1][j] == "X")):
                        dfs(i, j, True)
                    else:
                        dfs(i, j, False)

        return ship_count


s = Solution()
print(s.countBattleships([["X", ".", ".", "X"],
                          ["X", ".", ".", "X"],
                          [".", ".", ".", "X"]]))

print(s.countBattleships([[".", "X", ".", "."],
                          [".", ".", ".", "."],
                          ["X", "X", "X", "."]]))

print(s.countBattleships([[".", "X ", ".", "."],
                          [".", "X", ".", "."],
                          [".", ".", ".", "."]]))
