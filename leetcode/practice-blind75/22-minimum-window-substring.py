import collections
import math


class Solution:

    """
    Improve on minWindow(1), O(1) while have == need, which happens n times.

    O(n) runtime
    """
    def minWindow(self, s: str, t: str) -> str:
        need_map = collections.defaultdict(int)
        for char in t:
            need_map[char] += 1
        need = len(need_map.keys())

        have_map = collections.defaultdict(int)
        have = 0

        left, right = 0, 0
        minLeft, minRight = 0, len(s)  # right will never be len(s) so if left/right are found it will overwrite these
        while right < len(s):
            if s[right] in need_map:
                have_map[s[right]] += 1

                if have_map[s[right]] == need_map[s[right]]:
                    have += 1

            while have == need:
                if (right - left) < (minRight - minLeft):
                    minRight = right
                    minLeft = left

                if s[left] in need_map:
                    have_map[s[left]] -= 1

                    if have_map[s[left]] < need_map[s[left]]:
                        have -= 1

                left += 1

            right += 1

        return s[minLeft:minRight + 1] if minRight != len(s) else ""


    """
    O(n*n) runtime due to while self.equal(dict, dict) being O(n) which occurs n times. 
    """
    def minWindow1(self, s: str, t: str) -> str:
        need_map = collections.defaultdict(int)
        for char in t:
            need_map[char] += 1

        have_map = collections.defaultdict(int)

        left, right = 0, 0
        minLeft, minRight = 0, len(s)  # this is larger than left/right will ever be
        while right < len(s):
            if s[right] in need_map:
                have_map[s[right]] += 1

            while self.equal(have_map, need_map):
                if (right - left) < (minRight - minLeft):
                    minRight = right
                    minLeft = left
                if s[left] in need_map:
                    have_map[s[left]] -= 1
                left += 1
            right += 1

        return s[minLeft:minRight + 1] if minRight != len(s) else ""

    def equal(self, have_map, need_map):
        for key, value in need_map.items():
            if have_map[key] < value:
                return False
        return True


s = "ADOBECWEFEKWLJFBANC"
t = "ABC"

c = Solution()
print(c.minWindow(s, t))
