class Solution:
    def findMin(self, nums: list[int]) -> int:
        while True:
            mid = len(nums) // 2

            first, last = nums[0], nums[-1]
            if last < first:  # is rotated, custom binary search logic
                if len(nums) % 2 != 0:
                    if nums[mid - 1] > nums[mid]:  # check if middle element is lowest value (elem to left is greater)
                        return nums[mid]

                if nums[mid - 1] < last:
                    nums = nums[:mid]  # left
                else:  # last in rhs is lower than last in lhs so we go right
                    if len(nums) % 2 != 0:
                        mid += 1
                    nums = nums[mid:]  # right
            else:
                # return first because array is in order
                return first


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
print(s.findMin([8, 1, 2, 3]))
print(s.findMin([7, 8, 9, 0]))
print(s.findMin([1, 2, 3, 4]))
print(s.findMin([8, 1, 2, 3, 4]))
print(s.findMin([9, 0, 1, 2, 3]))
print(s.findMin([4, 5, 6, 1, 2, 3]))
