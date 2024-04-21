class Solution:

    def reverseBits(self, n: int) -> int:
        n = format(n, 'b')  # turn int into binary
        binary = n.zfill(32)  # add zeros up to 32 bit length

        return int(binary[::-1], 2)  # reverse and give us the base 2 integer


s = Solution()
print(s.reverseBits(4294967293))
