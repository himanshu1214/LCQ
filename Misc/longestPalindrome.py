class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        
        res = ""
        reslen = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if reslen < (r - l + 1):
                    res = s[l:r+1]
                    reslen = len(res)
                
                l -= 1
                r += 1
            
            l , r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:

                if reslen < (r - l + 1):
                    res = s[l:r+1]
                    reslen = len(res)
                
                l -= 1
                r += 1
 
        return res     


# 2nd attempt 
class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = []
        
        hash = {}
        for i in range(len(s)):
            left = i
            right = i

            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                else:
                    res.append(s[left: right+1])
                    left -= 1
                    right += 1
        
            left = i
            right = i+1
            
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                else:
                    res.append(s[left:right+1])
                    left -= 1
                    right += 1
            
        ln_tracker = ""
        for i in res:
            ln = len(i)
            if len(ln_tracker) < ln:
                ln_tracker = i
        return ln_tracker
        

            
