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
