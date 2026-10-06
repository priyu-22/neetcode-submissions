class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        brackets = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for ch in s:
            if ch in brackets:
                stack.append(brackets[ch])
            elif not stack or ch != stack.pop():
                return False
        return not stack
        
