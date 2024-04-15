# attempt 1 adding cache
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


class Solution:

    def wordBreakFirst(self, s: str, wordDict: list[str]) -> bool:
        wordDict = set(wordDict)

        @memoize
        def recur(s):
            if s == '':
                return True

            for i in range(len(s)):
                sub_string = s[:i + 1]
                if sub_string in wordDict:
                    if recur(s[i + 1:]):
                        return True

            return False

        return recur(s)

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        dp = [False] * (len(s) + 1)  # inclusive of 0
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # are there enough characters remaining
                # and
                # starting at index s[i] does s[i:] match w
                # i.e s[i:i+len(w)] == w
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    # dp[4] = dp[4 + len('code')] for case 'leetcode'
                    # dp[4] = dp[8]  which == True (empty string)
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]  # given we start at beginning of word, can we make it to the end


s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]))
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat", "an"]))
print(s.wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
