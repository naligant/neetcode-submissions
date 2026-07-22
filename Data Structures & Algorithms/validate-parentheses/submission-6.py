class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_open = ["(", "{", "["]
        for char in list(s):
            try:
                if char in valid_open:
                    stack.append(char)
                elif char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            except IndexError:
                return False
        if len(stack) == 0:
            return True
        else:
            return False