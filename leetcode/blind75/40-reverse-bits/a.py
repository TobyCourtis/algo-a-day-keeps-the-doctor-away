class Solution:
    def reverseBitsFirst(self, n: int) -> int:
        binary = str(n)
        cnt = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                cnt += (2 ** i)
        return cnt

    def reverseBitsAuto(self, n: int) -> int:
        binary = str(n)
        binary = binary[::-1]
        return int(binary, 2)

    def reverseBits(self, n: int) -> int:
        n = format(n, 'b')
        binary = n.zfill(32)

        return int(binary[::-1], 2)




s = Solution()
print(s.reverseBits(4294967293))
print(s.reverseBitsAuto(11111111111111111111111111111101))
print(s.reverseBitsFirst(11111111111111111111111111111101))
