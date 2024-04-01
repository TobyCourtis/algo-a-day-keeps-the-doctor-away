class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}  # base case when we get to end of string, number ways to decode is 1

        def dfs(index):
            if index in dp:
                return dp[index]  # either base case when index == len(s) OR cache
            if s[index] == "0":
                return 0  # no ways to decode

            res = dfs(index + 1)  # dfs for next index because whatever the next char is (1-9), it is valid

            if index < len(s) - 1 and int(s[index:index + 1]) <= 26:  # if less than 26, we can take next 2 chars
                res += dfs(index + 2)

            dp[index] = res  # set dp for current index to the accumulated total

            # return result for use in dfs() call.
            return res

        return dfs(0)


s = Solution()

# Input: "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
print(s.numDecodings("12"))
print(s.numDecodings("226"))
print(s.numDecodings("06"))
