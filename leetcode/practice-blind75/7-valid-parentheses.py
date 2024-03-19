class Solution:
    def isValid(self, s: str) -> bool:
        open = {"(", "[", "{"}

        stack = []
        for char in s:
            if char in open:
                stack.append(char)
            else:
                if not stack:
                    return False  # stack empty

                prev = stack.pop()
                if char == ")":
                    if prev != "(":
                        return False
                elif char == "}":
                    if prev != "{":
                        return False
                elif char == "]":
                    if prev != "[":
                        return False

        if stack:
            return False
        return True


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("))(("))
print(s.isValid("(]"))
