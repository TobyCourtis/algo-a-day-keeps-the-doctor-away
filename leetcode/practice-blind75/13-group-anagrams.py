import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for str in strs:
            alphabet_array = [0] * 26
            for char in str:
                alphabet_array[ord(char) - ord('a')] += 1
            groups[tuple(alphabet_array)].append(str)
        return groups.values()


s = Solution()
# print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.groupAnagrams(["ac", "c"]))
