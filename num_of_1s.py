class Solution:
    def hammingWeight(self, n: int) -> int:
        ct = 0
        while n:
            ct += n%2
            n = n >> 1
        
        return ct
