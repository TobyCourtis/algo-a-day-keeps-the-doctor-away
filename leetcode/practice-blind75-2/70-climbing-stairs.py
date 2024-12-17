class Solution:
    cache = {}

    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        if n in self.cache:
            return self.cache[n]
        else:
            res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.cache[n] = res
            return res

    def climbStairsUp(self, n: int) -> int:

        ways = 0

        def dfs(n, cur):
            nonlocal ways

            if n == cur:
                ways += 1
                return
            elif cur > n:
                return
            dfs(n, cur + 1)
            dfs(n, cur + 2)

        dfs(n, 0)
        return ways


s = Solution()
print(s.climbStairs(3))
