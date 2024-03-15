class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        length = len(s) - 1
        maximum = s[0]
        max_len = 1
        for i in range(len(s)):
            left = i - 1
            right = i + 1
            tmp = s[i]
            tmp_len = 1

            while left >= 0 and right <= length and s[left] == s[right]:
                tmp = s[left] + tmp + s[right]
                tmp_len += 2
                left -= 1
                right += 1

            if tmp_len > max_len:
                max_len = tmp_len
                maximum = tmp

            if i < length and s[i] == s[i + 1]:
                left = i - 1
                right = i + 2
                tmp = s[i] + s[i + 1]
                tmp_len = 2
                while left >= 0 and right <= length and s[left] == s[right]:
                    tmp = s[left] + tmp + s[right]
                    tmp_len += 2
                    left -= 1
                    right += 1

            if tmp_len > max_len:
                max_len = tmp_len
                maximum = tmp

        return maximum


s = Solution()
print(s.longestPalindrome("babad"))
