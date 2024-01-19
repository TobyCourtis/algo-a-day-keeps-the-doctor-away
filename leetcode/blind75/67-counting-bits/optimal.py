class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)  # init array of 0s
        for i in range(1, n + 1):
            # use i bitshifted by 1 and the end flag in i
            # 5 = 101
            # bitshift = 01
            # last flag i = 1

            # so here ans[5] == ans[2] + 1

            # the point in this approach is we've already done the calculation
            # of ans[i >> 1] therefore it's a simple lookup rather than recomputing
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
