from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        remove = set()

        i = 0
        while i < len(intervals) - 1:
            j = i + 1
            while j < len(intervals) and intervals[i][1] >= intervals[j][0]:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                remove.add(j)
                j += 1

            i = j

        out = []
        for i in range(len(intervals)):
            if i not in remove:
                out.append(intervals[i])

        return out


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
print(s.merge([[1, 4], [0, 2], [3, 5]]))
