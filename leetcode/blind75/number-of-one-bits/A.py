import math


class Solution:
    def hammingWeight(self, n: int) -> int:
        # starting from the largest power of 2 that goes into n (call this x)
        # subtracting 2 ^ x from n
        # working down to zero
        # add one to total bit count each time a power of 2 goes into n
        solved = False
        total = 0
        while not solved:
            if n == 0:
                solved = True
                continue
            x = math.floor(math.log(n) / math.log(2))
            n = n - math.pow(2, x)
            total += 1
        return total


s = Solution()
print(s.hammingWeight(11))  # 1011
