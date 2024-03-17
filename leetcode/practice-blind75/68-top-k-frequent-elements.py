import collections
from typing import List


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = collections.defaultdict(int)  # default 0
        freq = [[] for _ in range(len(nums))]

        for num in nums:
            map[num] += 1

        for num, count in map.items():
            freq[count - 1].append(num)

        out = []
        for i in range(len(nums) - 1, -1, -1):
            for num in freq[i]:
                out.append(num)
                k -= 1
                if k == 0:
                    return out

        return out


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(s.topKFrequent([3, 0, 1, 0], 1))
