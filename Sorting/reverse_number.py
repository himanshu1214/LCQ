class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
            x *= -1
        rev = 0
        while x > 0:
            if rev*10 > 2**31 -1 or rev*10 < -2**31:
                return 0
            else:
                rev =  x % 10 + rev*10
                x = x//10
        return rev if not flag else -1*rev