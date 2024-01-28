class Solution:
    def memoize(func):
        cache = {}

        def wrapper(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]

        return wrapper

    @memoize
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)


s = Solution()
print(s.climbStairs(6))
