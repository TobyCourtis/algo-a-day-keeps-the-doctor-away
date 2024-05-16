from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []

        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])

        start.sort()
        end.sort()
        res = 0
        count = 0
        while start:
            s = start[0]
            e = end[1]

            if s < e:
                count += 1
                start.pop(0)
            else:
                count -= 1
                end.pop(0)
            res = max(res, count)
        return res


s = Solution()
print(s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
print(s.minMeetingRooms([[0, 30], [5, 16], [15, 20]]))
print(s.minMeetingRooms([[7, 10], [2, 4]]))
