import collections

nums = [2, 7, 11, 15]
target = 9


def foo(nums, target) -> list:
    nums_map = collections.defaultdict(list)

    for i in range(len(nums)):
        nums_map[nums[i]].append(i)

    for key in nums_map.keys():
        leftover = target - key
        if leftover == key:
            if len(nums_map[key]) > 1:
                return nums_map[key]
        elif leftover in nums_map:
            return nums_map[key] + nums_map[leftover]


print(foo(nums, target))
print(foo([3, 2, 4], 6))
print(foo([3, 3], 6))

# runtime beat 56%
