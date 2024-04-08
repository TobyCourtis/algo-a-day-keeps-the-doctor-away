import collections


class Solution:

    def minStepsSlower(self, s: str, t: str) -> int:
        s_map = self.make_map(s)
        t_map = self.make_map(t)

        steps = 0
        """
        if we loop through both maps twice, worst case is 26 * 2 = 52 loops
        
        instead see minSteps() where we go through a-z which is always 26 steps
        """
        for k, v in s_map.items():
            if t_map[k] < v:
                steps += v - t_map[k]

        for k, v in t_map.items():
            if s_map[k] < v:
                steps += v - s_map[k]

        return steps

    def minSteps(self, s: str, t: str) -> int:
        s_map = self.make_map(s)
        t_map = self.make_map(t)

        steps = 0
        for char in 'abcdefghijklmnopqrstuvwxyz':  # always constant 26 loops
            steps += abs(s_map[char] - t_map[char])

        return steps

    def make_map(self, string):
        out = collections.defaultdict(int)
        for char in string:
            out[char] += 1
        return out


s = Solution()
print(s.minSteps("leetcode", "coats"))
