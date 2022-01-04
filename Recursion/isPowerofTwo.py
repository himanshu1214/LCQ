class Solution:

    def isPowerOfTwo(self, n: int) -> bool:
        res = [0]
        def helper(n):
            if n == 0:
                return False
            
            if ( n == 1 or n ==2):
                res[0] = True
                return 

            if n % 2 != 0:
                res[0] = False
                return 

            helper(n//2)
        helper(n)
        print(res)
        return res[0]
