import math


class Solution:
    cache = {}

    def countBits(self, n: int) -> list[int]:
        output = []
        for i in range(n + 1):
            output.append(bin(i).count("1"))
        return output

    def countBitsSecond(self, n: int) -> list[int]:
        output = []
        for i in range(n + 1):
            counter = 0
            tmp = i
            while tmp > 0:
                largest_power = int(math.log(tmp, 2))  # get largest power in i
                tmp = tmp - (2 ** largest_power)  # takeaway 2^ largest power
                counter += 1  # increment that there was another 1 in the binary representation
            output.append(counter)
        return output

    def countBitsCache(self, n: int) -> list[int]:
        output = []
        for i in range(n, -1, -1):  # n to 0 inclusive
            output.insert(0, self.find_ones_in_binary_representation(i))
        return output

    def find_ones_in_binary_representation(self, n):
        if n in self.cache:
            return self.cache[n]
        counter = 0
        tmp = n
        while tmp > 0:
            largest_power = int(math.log(tmp, 2))  # get largest power in i
            tmp = tmp - (2 ** largest_power)  # takeaway 2^ largest power
            counter += 1  # increment that there was another 1 in the binary representation
        self.cache[n] = counter
        return counter


s = Solution()
print(s.countBits(8))
print(s.countBits(5))
print(s.countBits(2))
