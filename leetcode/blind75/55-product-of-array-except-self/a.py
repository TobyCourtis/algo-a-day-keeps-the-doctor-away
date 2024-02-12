class Solution:
    def productExceptSelfLinearMemory(self, nums: list[int]) -> list[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        cur = 1
        for i in range(len(nums)):
            cur *= nums[i]
            prefix[i] = cur

        cur = 1
        for i in range(len(nums)):
            cur *= nums[- (i + 1)]
            postfix[- (i + 1)] = cur

        output = []
        for i in range(len(nums)):
            pre = prefix[i - 1] if i - 1 >= 0 else 1
            post = postfix[i + 1] if i + 1 < len(nums) else 1

            output.append(pre * post)

        return output

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [0] * len(nums)

        cur = 1
        for i in range(len(nums)):
            output[i] = cur  # begin with 1 as nums[0] has no prefix
            cur *= nums[i]

        cur = 1
        for i in range(len(nums)):
            output[- (i + 1)] *= cur  # begin with 1 as nums[-1] has no postfix
            cur *= nums[- (i + 1)]

        return output


s = Solution()
print(s.productExceptSelfLinearMemory([1, 2, 3, 4]))
print(s.productExceptSelf([1, 2, 3, 4]))
