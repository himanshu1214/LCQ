#Bit manipulation

class Solution:
    def reverseBits(self, n: int) -> int:
        # basic logic: Use AND to get the bit and OR to add to the final result
        # O (1)
        res = 0
        for i in range(32):
            rem = (n >> i) & 1 # AND logic
            res = res | (rem << (31-i))
            
        return res
