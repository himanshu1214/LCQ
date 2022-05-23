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
