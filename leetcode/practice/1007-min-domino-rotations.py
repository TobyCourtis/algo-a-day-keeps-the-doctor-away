from typing import List


class Solution:

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        to_check = {1, 2, 3, 4, 5, 6}

        top_count = {x: 0 for x in range(1, 7)}
        bottom_count = {x: 0 for x in range(1, 7)}

        for i in range(len(tops)):
            remove = []
            cur_domino = (tops[i], bottoms[i])
            top_count[tops[i]] += 1
            bottom_count[bottoms[i]] += 1

            if len(to_check) == 0:
                return -1

            for c in to_check:
                if c not in cur_domino:
                    remove.append(c)

            for val in remove:
                to_check.remove(val)

        if len(to_check) == 0:
            return -1

        val = to_check.pop()
        return len(tops) - max(top_count[val], bottom_count[val])

    def minDominoRotationsFirst(self, tops: List[int], bottoms: List[int]) -> int:
        top = tops[0]
        bot = bottoms[0]
        to_check = [top, bot]

        flip = 0
        for i in range(1, len(tops)):
            top_check = tops[i] in to_check
            bottom_check = bottoms[i] in to_check

            if top not in (tops[i], bottoms[i]):
                if top in to_check:
                    to_check.remove(top)
            if bot not in (tops[i], bottoms[i]):
                if bot in to_check:
                    to_check.remove(bot)

            if not top_check and not bottom_check:
                return -1
            elif tops[i] == bottoms[i]:
                continue
            elif top_check:
                if tops[i] != top:
                    bottoms[i] = tops[i]
                    tops[i] = top
                    flip += 1
            else:
                if bottoms[i] != bot:
                    tops[i] = bottoms[i]
                    bottoms[i] = bot
                    flip += 1

        return min(flip, len(tops) - flip)


s = Solution()
print(s.minDominoRotations([2, 1, 2, 4, 2, 2],
                           [5, 2, 6, 2, 3, 2]))
#
# print(s.minDominoRotations([3, 5, 1, 2, 3],
#                            [3, 6, 3, 3, 4]))

# print(s.minDominoRotations([2, 1, 2, 4, 2, 2],
#                            [5, 2, 6, 2, 3, 2]))

# print(s.minDominoRotations([1, 2, 1, 1, 1, 2, 2, 2],
#                            [2, 1, 2, 2, 2, 2, 2, 2]))

# print(s.minDominoRotations([2, 1, 1, 3, 2, 1, 2, 2, 1],
#                            [3, 2, 3, 1, 3, 2, 3, 3, 2]))
