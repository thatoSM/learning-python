# LeetCode #20 — Valid Parentheses (Easy)

# Given a string of brackets, check if they are balanced and properly nested.
# Valid: "()", "()[]{}", "{[]}"
# Invalid: "(]", "([)]"

# My approach: use a stack. Push opening brackets onto the stack.
# When you see a closing bracket, check if it matches the most recent
# opening bracket on the stack. If not, it's invalid. At the end,
# the stack must be empty for the string to be valid.

# Key concept: stack (LIFO - Last In, First Out)
# In Python, a list with .append() and .pop() works as a stack.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in pairs:
                if not stack:
                    return False
                top = stack.pop()
                if top != pairs[char]:
                    return False
            else:
                stack.append(char)
    
        return len(stack) == 0