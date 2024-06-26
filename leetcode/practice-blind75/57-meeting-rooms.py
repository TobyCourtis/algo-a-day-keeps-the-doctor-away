from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i + 1][0] < intervals[i][1]:
                return False
        return True


s = Solution()
print(s.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
print(s.canAttendMeetings([[7, 10], [2, 4]]))
