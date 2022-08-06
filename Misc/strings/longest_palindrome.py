class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        res = ""
        for i in range(1, len(s)):
            start, end = i, i-1
            
            flag = False
            while start >=0 and end < len(s) and not flag:
                if s[start] == s[end]:
                    start -= 1
                    end += 1        
                else:
                    flag = True
                    
            if len(res) < (end-1 - start+1):
                res = s[start+1:end]

                    
        for i in range(1, len(s)):
            start, end = i-1, i+1
            flag = False
            while start>=0 and end < len(s) and not flag:
                if s[start] == s[end]:
                    start -=1
                    end += 1
                else:
                    flag = True
                    
            if len(res) < (end-1 - start+1):
                res = s[start+1:end]
                print(f"SEC: {res}", i, start, end)
            
        return res
                    
