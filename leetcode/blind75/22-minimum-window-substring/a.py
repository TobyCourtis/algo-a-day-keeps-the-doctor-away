from collections import defaultdict
import math


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if t == "":
            return ""

        have_map, need_map = defaultdict(int), defaultdict(int)
        for char in t:
            need_map[char] += 1
        have, need = 0, len(need_map.keys())

        out, outLength = [-1, -1], math.inf
        l = 0

        for r in range(len(s)):
            # 1. get next char
            cur_char = s[r]

            if cur_char in need_map:
                have_map[cur_char] += 1
                # we need to come in and say if it's greater than or equal
                # and not counted already then need += 1
                if have_map[cur_char] == need_map[cur_char]:
                    have += 1

            while have == need:
                if (r - l) < outLength:
                    out = [l, r]
                    outLength = r - l

                # decrease window size
                prev_char = s[l]
                if prev_char in need_map:
                    have_map[prev_char] -= 1
                    if have_map[prev_char] < need_map[prev_char]:
                        have -= 1
                l += 1

        return s[out[0]:out[1] + 1]


    """
    This process used len(output) string which was not O(1) and therefore the submission only beat 40% in runtime.
    """
    def minWindowFirst(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if t == "":
            return ""

        current_map, t_map = defaultdict(int), defaultdict(int)

        for char in t:
            t_map[char] += 1
        current_total = 0
        t_map_total = len(t_map.keys())

        out = ""
        l, r = 0, 0
        while r <= len(s) - 1:
            # increase window size
            next_char = s[r]
            if next_char in t_map:
                if current_map[next_char] >= t_map[next_char]:
                    current_map[next_char] += 1
                    r += 1
                    continue

                current_map[next_char] += 1
                if current_map[next_char] >= t_map[next_char]:
                    current_total += 1
            r += 1

            while current_total == t_map_total:
                if not out or (r - l) < len(out):
                    out = s[l:r]

                # decrease window size
                prev_char = s[l]
                if prev_char in t_map:
                    current_map[prev_char] -= 1
                    if current_map[prev_char] < t_map[prev_char]:
                        current_total -= 1

                l += 1

        return out


s = Solution()
# print(s.minWindow("ADOBECODEBANC", "ABC"))
# print(s.minWindow("a", "b"))
print(s.minWindow("aa", "aa"))
