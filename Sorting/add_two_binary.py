class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)
        res = bin(num1 + num2)
        return str(res)[2:]
        
