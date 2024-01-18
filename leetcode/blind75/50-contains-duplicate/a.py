class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()  # O(1) lookup whereas list is O(n)
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3]))
