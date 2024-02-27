from typing import List


class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])  # sort by start

        removed = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:  # while we have not reached end of array
            if start >= prev_end:
                prev_end = end
            else:
                removed += 1
                prev_end = min(prev_end, end)  # new end is the lowest of previous end or next interval end

        return removed

    def eraseOverlapIntervalsFirstAttempt(self, intervals: List[List[int]]) -> int:
        # my plan

        overlap = {tuple: list(tuple)}
        # 1. go through each interval and count how many intervals it overlaps with

        # 2. remove interval with largest count
        # removed += 1
        # 2.5 for inter in overlap[(i, j)]
        # remove (i, j) from overlap[inter]

        # 3. if all are 0 then return 'removed' count
        return 0


s = Solution()
print(s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
