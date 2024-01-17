class Solution:
    left_brackets = ["(", "[", "{"]
    right_brackets = [")", "]", "}"]

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        for current_bracket in s:
            if current_bracket in self.left_brackets:
                stack.append(current_bracket)
            elif len(stack) > 0:
                top_stack_bracket = stack.pop()
                if self.left_brackets.index(top_stack_bracket) != self.right_brackets.index(current_bracket):
                    return False
            else:
                return False

        return True if len(stack) == 0 else False


string_input = "()[]{}"
s = Solution()
print(s.isValid(string_input))
