class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if len(intervals) == 0:
            return [newInterval]

        # 1. take newInterval 'start' val and find if it's either in interval X or before an interval Y.
        # keep track of index
        start = newInterval[0]
        end = newInterval[1]

        startIndex = None
        for i in range(len(intervals)):
            if start >= intervals[i][0] and start <= intervals[i][1]:
                startIndex = i
                break
            if start < intervals[i][0]:
                startIndex = i
                intervals.insert(startIndex,
                                 [start, start])  # insert new interval because 'start' not in any intervals
                break

        if startIndex is None:
            return intervals + [newInterval]

        # 2. we are then either extending 'startIndex' to end interval OR merging into a second interval
        foundEnd = False
        endIndex = startIndex
        for i in range(startIndex, len(intervals)):
            if end >= intervals[i][0] and end <= intervals[i][1]:
                foundEnd = True
                intervals[startIndex][1] = intervals[i][1]  # set end value of our 'startIndex' interval
                break
            if end < intervals[i][0]:
                # case we need to 'extend' startIndex interval to end at 'end'
                intervals[startIndex][1] = end  # this is because we haven't found end in an interval later in list
                break
            endIndex = endIndex + 1

        if startIndex == endIndex and intervals[startIndex][1] < end:  # case last/only elem in intervals
            intervals[startIndex][1] = end
            return intervals

        # 3. Remove intervals that are now overlapping our new interval
        if foundEnd:
            # remove up to and including end
            intervals = intervals[:startIndex + 1] + intervals[endIndex + 1:]
        else:
            intervals[startIndex][1] = end
            # remove up to and not including end
            intervals = intervals[:startIndex + 1] + intervals[endIndex:]
        return intervals


s = Solution()

smaller = [[1, 3], [6, 9]]
print(s.insert(smaller, [2, 5]))

print(s.insert([[1, 5]], [0, 6]))

larger = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
print(s.insert(larger, [4, 8]))
