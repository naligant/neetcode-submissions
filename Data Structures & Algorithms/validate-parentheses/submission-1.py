class Solution:
    def isValid(self, s: str) -> bool:
        valid_open = ['(', '{', '[']
        stack = []
        for char in list(s):
            if char in valid_open:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == '(' and char == ')':
                    stack.pop()
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                elif stack[-1] == '[' and char == ']':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False