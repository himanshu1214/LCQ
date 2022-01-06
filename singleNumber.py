class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Basic logic is using XOR operation
        # 1 1 -> 0
        # 0 0 -> 0
        # 1 0 --> 1
        # 0 1 -> 1
        # 2 -->  10 -->   
        # 2 -->  10   --> XOR 
        # 1 -->  01
        # RES -->  01
        res = 0
        for i in nums:
            res = i ^ res
        return res
        
        
