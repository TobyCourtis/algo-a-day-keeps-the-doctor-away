class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0

        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])

        return maxLength


s = Solution()
test_cases = [
    ("abcabcbb", 3),
    ("bbbb", 1),
    ("pwwkew", 3),
    ("ohomm", 3),
    ("asjrgapa", 6),
    (" ", 1),
    ("umvejcuuk", 6)
]
for test in test_cases:
    try:
        assert s.lengthOfLongestSubstring(test[0]) == test[1]
    except AssertionError as e:
        print(f"For string '{test[0]}' expected length {test[1]} but was {s.lengthOfLongestSubstring(test[0])}")
