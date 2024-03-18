class Solution:
    cache = {}

    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        if n in self.cache:
            return self.cache[n]
        else:
            out = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.cache[n] = out
            return out


s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
