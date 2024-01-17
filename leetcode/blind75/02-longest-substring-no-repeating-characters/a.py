class Solution:
    # time limit exceeded with large strings
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        tmp_longest = ""
        for i in range(len(s)):
            max_len = max(max_len, len(tmp_longest))
            tmp_longest = s[i]
            for j in range((i+1), len(s)):
                if s[j] not in tmp_longest:
                    tmp_longest += s[j]
                else:
                    max_len = max(max_len, len(tmp_longest))
                    tmp_longest = ""
                    continue
        return max(max_len, len(tmp_longest))

    # fails 'asjrgapa'
    def lengthOfLongestSubstringFailed(self, s: str) -> int:
        max_len1 = 0
        tmp_longest = ""

        max_len2 = 0
        tmp_longest2 = ""
        for i in range(len(s)):
            if s[i] not in tmp_longest:
                tmp_longest += s[i]
            else:
                max_len1 = max(max_len1, len(tmp_longest))
                tmp_longest = s[i]

            if s[-(i + 1)] not in tmp_longest2:
                tmp_longest2 += s[-(i + 1)]
            else:
                max_len2 = max(max_len2, len(tmp_longest2))
                tmp_longest2 = s[-(i + 1)]

        return max(len(tmp_longest), len(tmp_longest2), max_len1, max_len2)


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
