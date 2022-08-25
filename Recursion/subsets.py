class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(nums, slate, index):
            
            if index > len(nums)-1:
                result.append(slate[:])
                return 
            
            dfs(nums, slate, index+1)
            slate.append(nums[index])
            dfs(nums, slate, index+1)
            slate.pop()
            
        dfs(nums, [], 0)
        
        return result
