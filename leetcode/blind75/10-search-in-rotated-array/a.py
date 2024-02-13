class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        # need to do in log(n) which is divide and conquer

        index_accumulator = 0  # if we split in half and take rhs we need to add half the length to the accumulator
        while True:
            midpoint = len(nums) // 2

            if len(nums) % 2 == 0:
                left = nums[:midpoint]
                right = nums[midpoint:]
            else:
                if target == nums[midpoint]:
                    return index_accumulator + midpoint
                left = nums[:midpoint]
                right = nums[midpoint + 1:]

            if self.is_target_in_array(left, target):
                nums = left
            elif self.is_target_in_array(right, target):
                index_accumulator += midpoint if len(nums) % 2 == 0 else midpoint + 1
                nums = right
            else:
                return -1

    def is_target_in_array(self, arr, target):
        if len(arr) == 1:
            return True if arr[-1] == target else False

        # case the array has been rotated and our start elem is larger than end elem
        if arr[0] > arr[-1]:
            if target >= arr[0] or target <= arr[-1]:
                return True
        # default case where we're looking at a regular sorted array
        else:
            if arr[0] <= target <= arr[-1]:
                return True

        return False  # not in array


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
print(s.search([1], 0))
print(s.search([1, 3], 3))
