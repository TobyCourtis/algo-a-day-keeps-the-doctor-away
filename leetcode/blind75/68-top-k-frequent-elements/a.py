from collections import defaultdict
from typing import List


class Solution:
    def topKFrequentFirstAttempt(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)  # default 0

        for num in nums:
            map[num] += 1

        list = [(k, v) for k, v in map.items()]
        list.sort(reverse=True, key=lambda x: x[1])

        out = []
        for i in range(k):
            out.append(list[i][0])

        return out

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)  # default 0
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            map[num] += 1

        for num, count in map.items():
            freq[count].append(num)

        out = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                if k == 0:
                    break
                out.append(num)
                k -= 1

        return out


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
