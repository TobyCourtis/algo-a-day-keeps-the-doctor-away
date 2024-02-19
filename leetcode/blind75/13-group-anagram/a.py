from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        output_map = defaultdict(list)

        for s in strs:
            alphabet_array = [0] * 26

            for character in s:
                alphabet_array[ord(character) - ord('a')] += 1  # this makes 'a' index 0, 'b' index 1 etc

            output_map[tuple(alphabet_array)].append(s)  # tuple is shared key for all anagrams, append current string

        return output_map.values()


s = Solution()
print(s.groupAnagrams(["foo", "bad", "dab"]))
