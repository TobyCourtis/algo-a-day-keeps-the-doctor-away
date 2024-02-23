from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])

        start.sort()
        end.sort()
        res, count = 0, 0
        while start:
            s = start[0]
            e = end[0]

            if s < e:
                count += 1
                start.pop(0)
            else:
                count -= 1
                end.pop(0)
            res = max(res, count)

        return count


# Example tests
if __name__ == "__main__":
    s = Solution()
    meetings1 = [[0, 30], [5, 10], [15, 20]]
    print(s.minMeetingRooms(meetings1))  # Expected: 2

    meetings2 = [[7, 10], [2, 4]]
    print(s.minMeetingRooms(meetings2))  # Expected: 1

    meetings3 = [[0, 30], [5, 10], [10, 20]]
    print(s.minMeetingRooms(meetings3))  # Expected: 2
