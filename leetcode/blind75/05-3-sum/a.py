from collections import defaultdict


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        dict_nums = defaultdict(int)
        for num in nums:
            dict_nums[num] = dict_nums[num] + 1

        output = []
        for i in dict_nums.keys():
            combinations = self.find_two_sum(i, nums, dict_nums)
            for combination in combinations:
                output.append([i] + list(combination))

        # lazy as I could just avoid iterating over values earlier in the code
        unique_lists = set()
        for inner_list in output:
            unique_lists.add(tuple(sorted(inner_list)))

        return [list(x) for x in unique_lists]

    def find_two_sum(self, first_value, nums, dict_nums) -> set:
        dict_nums = dict(dict_nums)  # copy
        dict_nums[first_value] -= 1
        if dict_nums[first_value] == 0:
            del (dict_nums[first_value])
        out = set()
        # 1 input
        # 1 + x + y = 0
        # 1 + ? + ? = 0

        # first_value + x + y = 0
        # y = - first_value - x

        for x in nums:
            y = - first_value - x
            if y in dict_nums and x in dict_nums:
                if x == y:
                    if dict_nums[x] < 2:
                        continue

                out.add((x, y))  # frozenset so we have hashable type in output set

                dict_nums[x] -= 1
                if dict_nums[x] == 0:
                    del (dict_nums[x])
                dict_nums[y] -= 1
                if dict_nums[y] == 0:
                    del (dict_nums[y])
        return out


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
# print(s.find_combos(-1, [-1, 0, 1, 2, -1, -4], {-4: 1, -1: 2, 0: 1, 1: 1, 2: 1}))
