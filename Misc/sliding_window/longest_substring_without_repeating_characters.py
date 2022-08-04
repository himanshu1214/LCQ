class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        dq = deque()
        res = 0
        start = 0
        while  start < len(s):
            dq.append(s[start])
            while dq and len(dq) != len(set(dq)):
                dq.popleft()
                
            if res < len(dq):
                res = len(dq)
            start += 1
            
        return res
