from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        cur = 1
        for i in range(len(nums)):
            cur *= nums[i]
            prefix[i] = cur

        cur = 1
        for i in range(len(nums)):
            cur *= nums[-(i + 1)]
            postfix[-(i + 1)] = cur

        output = []
        for i in range(len(nums)):
            pre = prefix[i - 1] if i > 0 else 1
            post = postfix[i + 1] if i < len(nums) - 1 else 1
            output.append(pre * post)

        return output


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
