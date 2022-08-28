class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, slate, index):
            
            if index >= len(nums):
                res.append(slate[:])
                return 
            
            for i in range(index, len(nums)):
                
                nums[i], nums[index] = nums[index], nums[i]
                slate.append(nums[index])
                dfs(nums, slate, index+1)
                nums[i], nums[index] = nums[index], nums[i]
                slate.pop()
                
        dfs(nums, [], 0)
        
        return res
