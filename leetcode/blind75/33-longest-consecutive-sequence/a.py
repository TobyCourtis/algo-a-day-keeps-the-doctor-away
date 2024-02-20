class Solution:
    def longestConsecutiveFirstAttempt(self, nums: list[int]) -> int:
        ranges = {}

        # all numbers in nums are unique
        maximum = 1
        for num in nums:
            if num in ranges:
                if num - 1 in ranges:
                    # we're at the upper end of the range because num - 1 and num are in ranges.
                    # increase range upper bound to num + 1
                    ranges[num + 1] = ranges[num] + 1
                    # increase range value on lower end
                    ranges[num - (ranges[num] + 1)] += 1
                    # overwrite maximum if new was found
                    maximum = max(maximum, ranges[num] + 1)

                elif num + 1 in ranges:
                    # we're at the lower end of the range because num and num + 1 are in range
                    # decrease range lower bound to num - 1
                    ranges[num - 1] = ranges[num] + 1
                    # increase range value on upper end
                    ranges[num + (ranges[num] + 1)] += 1
                    # overwrite maximum if new was found
                    maximum = max(maximum, ranges[num] + 1)

            else:
                ranges[num - 1] = 1
                ranges[num + 1] = 1

        return maximum

    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        maximum = 0
        for num in nums:
            if num - 1 in nums:
                continue
            else:
                index = num
                count = 0
                while index in nums:
                    index += 1
                    count += 1
                maximum = max(maximum, count)

        return maximum


s = Solution()
print(s.longestConsecutive([1, 3, 2, 100, 4, 200]))
