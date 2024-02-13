class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])

        START_INDEX = 0
        END_INDEX = 1

        out = []

        i = 0
        while i < len(intervals):
            cur_start = intervals[i][START_INDEX]
            cur_end = intervals[i][END_INDEX]
            j = i + 1

            while j < len(intervals):
                next_start = intervals[j][START_INDEX]
                next_end = intervals[j][END_INDEX]

                # if next start is less than current end, we need to merge
                if next_start <= cur_end:
                    cur_end = max(cur_end, next_end)  # we want the maximal end value
                    j += 1
                else:
                    break

            out.append([
                cur_start,
                cur_end
            ])

            i = j

        return out


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge([[1, 4], [0, 4]]))
print(s.merge([[1, 4], [2, 3]]))
print(s.merge([[1, 4], [0, 2], [3, 5]]))

print(s.merge([[1, 4], [4, 5]]))
print(s.merge([[1, 4], [0, 0]]))
print(s.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
