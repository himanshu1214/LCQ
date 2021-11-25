class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}

        def helper(n):

            if n <= 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            if n in cache:
                return cache[n]

            if n > 2:
                cache[n] = helper(n - 1) + helper(n - 2) + helper(n - 3)

            return cache[n]
        
        return helper(n)
