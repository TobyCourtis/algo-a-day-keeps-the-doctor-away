class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff  # = 32 bits all 1s

        logical_xor = a
        logical_and = b

        while (logical_and & mask):
            prev_logical_xor = logical_xor

            logical_xor = (logical_xor ^ logical_and) & mask
            logical_and = ((prev_logical_xor & logical_and) << 1) & mask

        # if we have negative number
        if logical_xor > mask // 2:
            # XOR then NOT
            return ~(logical_xor ^ mask)  # convert to python's negative binary representation
        else:
            return logical_xor


s = Solution()
print(s.getSum(9, 11))
print(s.getSum(1, 2))
print(s.getSum(2, 3))
print(s.getSum(-12, -8))
