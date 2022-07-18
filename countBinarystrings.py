class Solution:

    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        preCnt = 0
        i = 0
        n = len(s)
        while i < n:
            currCnt = 1
            while i < n-1 and s[i] == s[i+1]:
                currCnt += 1
                i += 1
                
            if preCnt > 0:
                ans += min(preCnt, currCnt)
            preCnt = currCnt
            i += 1
        return ans
    
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
            res = [0]
            start = 1
            prev = float('-inf')
            while  start < len(s):
                if s[start] != s[start-1]:
                    f_ptr, s_ptr = start-1, start
                    while f_ptr >=0 and s_ptr <= len(s)-1 and s[f_ptr] != s[s_ptr]:
                        if f_ptr < prev:
                            break
                        res[0] += 1
                        f_ptr -= 1
                        s_ptr += 1              
                    prev = start
                start += 1
            return res[0]

