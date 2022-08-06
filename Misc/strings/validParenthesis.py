class Solution:
    def isValid(self, s: str) -> bool:
        from collections import defaultdict
        if len(s) % 2 == 1:
            return False
        
        stack = []
        mapper = {"(": ")", "{": "}", "[": "]"}
        for i in range(len(s)):
            
            if not stack:
                stack.append(s[i])
            elif stack and stack[-1] in mapper and mapper[stack[-1]] == s[i]:
                stack.pop()
            elif stack and s[i] in mapper:
                stack.append(s[i])
            elif stack and s[i] not in mapper:
                return False

        return True if not stack else False
