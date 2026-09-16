class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(', '}':'{', ']':'['}
        for ch in s:
            if ch in brackets and (stack and stack[-1] == brackets[ch]):
                stack.pop()
            else:
                stack.append(ch)
        return True if not stack else False
