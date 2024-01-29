class Solution:

    # attempt 1, for each char walk out - not optimised
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        length = len(s)
        if length == 2 and s[0] == s[1]:
            return s
        for i in range(1, length):
            left = i - 1
            right = i + 1
            tmp = s[i]
            while left >= 0 and right < length:
                if s[left] != s[right]:
                    break
                tmp = s[left] + tmp + s[right]
                if len(tmp) > len(longest):
                    longest = tmp
                left = left - 1
                right = right + 1

            left = i - 1
            right = i
            tmp = ""
            while left >= 0 and right < length:
                if s[left] != s[right]:
                    break
                tmp = s[left] + tmp + s[right]
                if len(tmp) > len(longest):
                    longest = tmp
                left = left - 1
                right = right + 1
        return longest


s = Solution()
print(s.longestPalindrome("cbabd"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("abb"))
