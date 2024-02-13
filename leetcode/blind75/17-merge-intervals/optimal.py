class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if lastEnd >= start:
                output[-1][1] = max(end, lastEnd)
            else:
                output.append([start, end])
        return output
