from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[-1] = True  # empty string = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


s = Solution()
print(s.wordBreak(s="leetcode",
                  wordDict=["leet", "code"]))

print(s.wordBreak(s="catsandog",
                  wordDict=["cats", "dog", "sand", "and", "cat"]))
