class Solution:

    # neetcode
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    # 1 + the diagonal
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]

    # my attempt
    def longestCommonSubsequenceFirstAttempt(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            shortest = text1
            longest = text2
        else:
            shortest = text2
            longest = text1

        combinations = []

        def combos(index, acc=[]):
            if index >= len(shortest):
                combinations.append(acc)
                return

            for i in range(1, len(shortest[index:]) + 1):
                combos(index + i, acc + [shortest[index]])

        # build all combos in the shortest string
        for i in range(len(shortest)):
            combos(i)

        combinations.sort(key=lambda x: len(x), reverse=True)

        maximum = 0
        for combo in combinations:
            index = 0
            if len(combo) > maximum:
                for char in longest:
                    if char == combo[index]:
                        index += 1
                    if index == len(combo):
                        maximum = max(len(combo), maximum)
                        break

        return maximum


s = Solution()
print(s.longestCommonSubsequence("adbec", "abc"))
print(s.longestCommonSubsequence("abc", "def"))
