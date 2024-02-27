import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        max_length = 0

        l = 0
        maxf = 0  # used to optimise - unlikely to be asked in interviews
        for r in range(len(s)):
            count[s[r]] += 1  # increment count of char at index r
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1  # decrement count of char at index l before increment l (shortening window)
                l += 1
                # advanced:
                # do not need to decrement maxf because if we did we still cannot beat the max length we previously
                # calculated. To beat max_length we need a maxf larger than maxf currently - therefore do not need
                # to decrement it.

            max_length = max(max_length, r - l + 1)

        return max_length

    def characterReplacementFirstAttempt(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        maximum = 0
        for i in range(len(s) - 1):
            first = s[i]
            index = i + 1
            k_tmp = k

            while index < len(s):
                next = s[index]

                if next != first:
                    if k_tmp <= 0:
                        break
                    k_tmp -= 1

                index += 1

            # if we've got k left over

            length = index - i
            while k_tmp and length < len(s):
                k_tmp -= 1
                length += 1
            maximum = max(length, maximum)
        return maximum


s = Solution()
print(s.characterReplacement("ABAB", 2))
print(s.characterReplacement("ABBB", 2))
print(s.characterReplacement("AABABBA", 1))
