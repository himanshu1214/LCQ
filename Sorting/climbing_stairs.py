class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return []
        hash_map = {}
        def helperfunc(n):
            if n ==1 or n==0:
                return 1
            if n in  hash_map:
                return hash_map[n]
            
            ans = helperfunc(n- 1) + helperfunc(n-2)
            hash_map[n] = ans
            return ans
        res = helperfunc(n)
        return res
