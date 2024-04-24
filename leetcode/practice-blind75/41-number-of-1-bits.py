class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count("1")


s = Solution()
print(s.hammingWeight(5))
