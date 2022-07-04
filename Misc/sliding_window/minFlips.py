class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count1 = 0 
        count0 = s.count("0")
        
        res = len(s) - count0
        
        for i in s:
            if i  == "0":
                count0 -= 1
                
            if i == "1":
                res = min(res, count0 + count1)
                count1 += 1
        return res
