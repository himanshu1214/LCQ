class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        right = [1]*n
        left[1] = nums[0]
        right[-2] = nums[-1]
        
        for i in range(2, len(nums)):
            left[i] = left[i-1]*nums[i-1]
            
        for j in range(len(nums)-3, -1, -1):
            right[j] = right[j+1]*nums[j+1]
        
        res = [0]*n
        for i in range(n):
            res[i] = left[i]*right[i]
        
        return res
