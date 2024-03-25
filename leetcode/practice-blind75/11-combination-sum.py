import collections
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # we begin with a choice from candidate, if we go left in tree, we can choose all the same candidates
        # if we go right, do not allow the choice of same candidate again

        output = []

        def dfs(index, cur, total):
            if total == target:
                output.append(cur.copy())
                return

            if index >= len(candidates) or total > target:
                return

            current_candidate = candidates[index]
            cur.append(current_candidate)

            # left, we can use the same values
            dfs(index, cur, total + current_candidate)

            # right, we remove the last value in cur and don't add candidate to total
            cur.pop()
            dfs(index + 1, cur, total)

        dfs(0, [], 0)
        return output


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
