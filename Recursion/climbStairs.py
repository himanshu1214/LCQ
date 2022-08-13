class Solution:
    def climbStairs(self, n: int) -> int:
        hash_map = {}
        def dfs(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            
  
            if n in hash_map:
                return hash_map[n]
            
            val = dfs(n-1) + dfs(n-2)
            hash_map[n] = val
            
            return val
        dfs(n)
        return hash_map[n]
