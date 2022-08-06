class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        res = 0
        for i in range(len(s)):
            start, end = i-1, i
            
            flag = False
            while start >=0 and end < len(s) and not flag:
                if s[start] == s[end]:
                    start -= 1
                    end += 1    
                    res += 1
                else:
                    flag = True
                    
        for i in range(len(s)):
            start, end = i, i
            flag = False
            while start>=0 and end < len(s) and not flag:
                if s[start] == s[end]:
                    start -=1
                    end += 1
                    res += 1
                else:
                    flag = True
            
        return res
