class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1 = "0"*(len(num2) - len(num1)) + num1
        else:
            num2 = "0"*(len(num1) - len(num2)) + num2
            
        res = [] 
        carry = 0 
        
        for i in range(len(num1)-1, -1, -1):

            val_add = int(num1[i]) + int(num2[i]) + carry
            carry = 0
            if val_add >= 10:
                res.append(str(val_add % 10))
                carry = 1
            else:
                res.append(str(val_add))
        if carry > 0:
            res.append(str(carry))
        res.reverse()
            
        return "".join(res)
