class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        res = []
        tmp = []
        size = 0
        while start <= end and end < len(s):
            if s[end] not in tmp[start:end]:
                tmp.append(s[end])
                end += 1
            else:
                if end - start > size:
                    size = end - start
                start += 1
        if (end-start) > size:
            size = end - start

        return size
    
    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = len(s) 
        if not s:
            return 0
        
        if s[0] == " ":
            return 1
     
#     Solution#2
    from collections import deque
    dq = deque()
    dq_ln = 0
    while start < end:

        if start == 0:
            dq.append(s[start])
            start += 1

        elif s[start] not in dq:
            dq.append(s[start])
            start += 1
        else:
            if len(dq) > dq_ln :
                dq_ln = len(dq)

            while dq[0] != s[start]:
                dq.popleft()                    
            dq.popleft()

    if len(dq) > dq_ln :
        dq_ln = len(dq)

    return dq_ln
