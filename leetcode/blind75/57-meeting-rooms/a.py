from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


s = Solution()
test_cases = [
    ([[0, 30], [5, 10], [15, 20]], False),
    ([[7, 10], [2, 4]], True)
]
# Perform assertions with custom messages
for intervals, expected_result in test_cases:
    assert s.canAttendMeetings(
        intervals) == expected_result, f"expected {expected_result} for {intervals} but was {not expected_result}"

print("All tests passed.")
