class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0

        for i in range(len(s)):
            l, r = i, i  # odd case, length 1, 3, 5, 7 ...
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes += 1
                l -= 1
                r += 1

            l, r = i, i + 1  # even case length 2, 4, 6 ...
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes += 1
                l -= 1
                r += 1

        return palindromes


s = Solution()
print(s.countSubstrings("aaa"))
# print(s.countSubstrings("aaab"))
