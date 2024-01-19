class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ''.join(char for char in s if char.isalnum()).lower()

        for i in range(len(clean_string) // 2):
            if clean_string[i] != clean_string[-(i + 1)]:
                return False
        return True


s = Solution()
print(s.isPalindrome("1racecar1"))
