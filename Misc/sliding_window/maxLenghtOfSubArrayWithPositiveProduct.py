class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        pos = [0]*len(nums)
        neg = [0] *len(nums)
        pos[0] = 1 if nums[0] > 0 else 0 
        neg[0] = 1 if nums[0] < 0 else 0
        
        for i in range(1, len(nums)):    
            if nums[i] > 0:
                pos[i] = pos[i-1] + 1 if pos[i-1] else 1
                neg[i] = neg[i-1] + 1 if neg[i-1] else 0
                
            if nums[i] < 0:
                pos[i] = neg[i-1] + 1 if neg[i-1] else 0
                neg[i] = pos[i-1] + 1 if pos[i-1] else 1
            
            
        return max(pos)
