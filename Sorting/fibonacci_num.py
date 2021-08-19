class Solution:
    hash_map = {}
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        if n in self.hash_map:
            return self.hash_map[n]
        
        ans = self.fib(n-1) + self.fib(n-2)
        self.hash_map[n] = ans
        return ans
