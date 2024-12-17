import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = collections.defaultdict(int)
        t_dict = collections.defaultdict(int)

        for char in s:
            s_dict[char] += 1
        for char in t:
            t_dict[char] += 1

        return s_dict == t_dict


s = Solution()
print(s.isAnagram("carrace", "racecar"))
print(s.isAnagram("foo", "bar"))
