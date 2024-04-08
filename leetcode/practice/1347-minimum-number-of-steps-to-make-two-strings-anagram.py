import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_map = self.make_map(s)
        t_map = self.make_map(t)

        need = 0
        for k, v in s_map.items():
            if t_map[k] < v:
                need += s_map[k] - t_map[k]

        return 1

    def make_map(self, string):
        out = collections.defaultdict(int)
        for char in string:
            out[char] += 1
        return out


s = Solution()
print(s.minSteps("bab", "aba"))
