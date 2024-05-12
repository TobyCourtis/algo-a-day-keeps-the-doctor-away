class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True

        s_arr = self.make_arr(s)
        t_arr = self.make_arr(t)

        return s_arr == t_arr

    def make_arr(self, s):
        arr = [0] * 26
        for char in s:
            arr[ord(char) - ord('a')] += 1
        return arr


s = Solution()
print(s.isAnagram(s="anagram", t="nagaram"))
