class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)  # init array of 0s
        for i in range(1, n + 1):
            # use i bitshifted 1 and the end flag in i
            # 5 = 101
            # bitshift = 01
            # last flag i = 1

            # so here ans[5] == ans[2] + 1
            ans[i] = ans[i >> 1] + (i & 1)
        return ans