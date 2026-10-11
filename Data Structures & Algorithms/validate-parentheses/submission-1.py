class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }
        stack = []
        for char in s:
            if char in parentheses:
                stack.append(parentheses[char])
            else:
                if len(stack) == 0:
                    return False
                close = stack.pop()
                if close != char:
                    return False
        return len(stack) == 0