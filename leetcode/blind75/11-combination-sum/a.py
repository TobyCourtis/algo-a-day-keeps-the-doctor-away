class Solution:
    def combinationSumDuplicates(self, candidates: list[int], target: int) -> list[list[int]]:

        out = []

        def combos(acc=[]):
            total = sum(acc)
            if total > target:
                return []
            elif total == target:
                out.append(acc)
            for candidate in candidates:
                combos(acc[:] + [candidate])

        combos()
        return out

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        result = []

        # index, current combination and total sum
        def dfs(i, cur, total):  # backtracking algorithm
            if total == target:
                result.append(cur.copy())
                return

            if i >= len(candidates) or total > target:  # base case we've looked at whole list or total GT target
                return

            current_candidate = candidates[i]

            # left in the tree where we can keep using current candidate
            cur.append(current_candidate)
            dfs(i, cur, total + current_candidate)

            # right in the tree where we cannot use current candidate
            cur.pop()  # clean cur by removing the candidate we just used on the LHS
            dfs(i + 1, cur, total)

            return

        dfs(0, [], 0)
        return result


s = Solution()
print(s.combinationSum(candidates=[2, 3, 6, 7], target=7))
