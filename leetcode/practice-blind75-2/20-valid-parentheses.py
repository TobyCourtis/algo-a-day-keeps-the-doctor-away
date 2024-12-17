class Solution:
    def isValid(self, s: str) -> bool:
        left = {"(", "{", "["}
        stack = []
        for char in s:
            if char in left:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if char == ")" and prev != "(":
                    return False
                elif char == "}" and prev != "{":
                    return False
                elif char == "]" and prev != "[":
                    return False

        if stack:
            return False
        return True


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([])"))
