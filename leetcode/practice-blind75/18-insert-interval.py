from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]

            new_start = newInterval[0]
            new_end = newInterval[1]
            if new_end < cur_start:
                # we add newInterval before current interval
                res.append(newInterval)
                return res + intervals[i:]  # we've added interval so append rest of list
            elif new_start > cur_end:
                res.append(intervals[i])
            else:
                newInterval = [min(new_start, cur_start), max(new_end, cur_end)]
                # let's say we insert [5, 100] into [4,7] = [4, 100]
                # next loop if we encounter [90, 150]
                # we again hit this else statement and update newInterval to be [4, 150]
                # this else ensures nothing is added to the output list BUT we update the newInterval if required
                # this process merges intervals that overlap with newInterval
                # when applicable, the newInterval is then inserted into the intervals list

        intervals.append(newInterval)  # we reached end of list without returning so append newInterval

        return intervals


s = Solution()
# print(s.insert([[1, 3], [6, 9]], [2, 5]))
# print(s.insert([[1, 3], [6, 9]], [4, 5]))
# print(s.insert([[1, 3], [4, 9]], [2, 5]))

# print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
# [[1, 2], [3, 10], [12, 16]]
print(s.insert([[1, 5]], [6, 8]))
