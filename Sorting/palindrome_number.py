class Solution:
    def isPalindrome(self, x: int) -> bool:
        val = str(x)
        if val[0] == '-' or val[0] == '+':
            return False
        i = 0 
        j = len(val)-1
        while i <= j:
            if val[i] == val[j]:
                i += 1
                j -= 1
            else:
                return False
            
        return True
            
                
                