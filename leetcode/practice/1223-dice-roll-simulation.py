from typing import List


class Solution:

    def memoize(self, func):
        cache = {}

        def wrapper(*args):
            if args in cache:
                return cache[args]
            else:
                result = func(*args)
                cache[args] = result
                return result
        return wrapper

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = (10 ** 9) + 7

        @self.memoize
        def dfs(count=0, prev_num=0, prev_freq=0):
            if count == n:
                return 1

            ans = 0
            for choice in range(1, 7):
                if choice == prev_num:
                    if prev_freq < rollMax[choice - 1]:
                        ans += dfs(count + 1, prev_num, prev_freq + 1)
                else:
                    ans += dfs(count + 1, choice, 1)

            return ans % mod

        return dfs()


s = Solution()
print(s.dieSimulator(n=2, rollMax=[1, 1, 2, 2, 2, 3]))
print(s.dieSimulator(n=2, rollMax=[1, 1, 1, 1, 1, 1]))
print(s.dieSimulator(n=3, rollMax=[1, 1, 1, 2, 2, 3]))
