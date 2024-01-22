class Solution:
    def isAnagramNSquared(self, s: str, t: str) -> bool:
        if s == t:
            return False
        if len(s) != len(t):
            return False

        # O(n^2)
        for char in s:
            if char not in t:
                return False
        return True

    def isAnagramNlogN(self, s: str, t: str) -> bool:
        if s == t:
            return False
        if len(s) != len(t):
            return False

        # O(n log n)
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        for i in range(len(s)):  # O(n)
            if s[i] != t[i]:
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}
        for i in range(len(s)):  # O(n)
            if s[i] not in s_dict:
                s_dict[s[i]] = 0
            if t[i] not in t_dict:
                t_dict[t[i]] = 0

            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

        return s_dict == t_dict


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("foo", "bar"))
