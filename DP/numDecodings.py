class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def helper(s, index):
            
                        
            if index == len(s):
                return 1
            
            if s[index] == "0":
                return 0
            
            if index == len(s) - 1:
                return 1
            
            if s[index:] in memo:
                return memo[s[index:]]

            val = helper(s, index+1)
                
            if int(s[index: index+2]) <= 26:
                val += helper(s, index+2)  
            memo[s[index:]] = val    
            return val
        
        return helper(s,0)
