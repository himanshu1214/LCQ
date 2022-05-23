class Solution:
    def climbStairs(self, n: int) -> int:
        hash_map = {}
        def helper(n):
            if n == 0 or n == 1:
                return 1

            if n < 0:
                return 0

            if n in hash_map:
                return hash_map[n]

            val = helper(n-1) + helper(n-2)
            hash_map[n] = val
            return val
            
        hash_map[n] = helper(n)
        return hash_map[n]

    
    
class Solution:
    def climbStairs(self, n: int) -> int:
        #                   n 
        #           n-1             n-2
        #       n-2   n-3       n-3     n-4
        dp = [None for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
