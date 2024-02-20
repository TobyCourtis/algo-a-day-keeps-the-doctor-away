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

    def numDecodings(self, s: str) -> int:

        @memoize
        def recur(string):
            if len(string) == 0:
                return 1

            if string[0] == "0":
                return 0

            if len(string) > 1 and int(string[0:2]) <= 26:
                return recur(string[1:]) + recur(string[2:])
            else:
                return recur(string[1:])

        for i in range(len(s) - 1, -1, - 1):
            recur(s[i:])

        return recur(s)

    def numDecodingsDynamic(self, s: str) -> int:
        dp = {len(s): 1}  # base case, empty string would return 1

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)

            if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
                res += dfs(i + 2)

            dp[i] = res

            return res

        return dfs(0)


s = Solution()
print(s.numDecodings("12"))
print(s.numDecodingsDynamic("12"))
print(s.numDecodingsDynamic("1201234"))
print(s.numDecodings("111111111111111111111111111111111111111111111"))
