class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        def helper(nums, index):
            if index > len(nums)-1:
                return 0
            if index in memo:
                return memo[index]
            
            val = max(nums[index] + helper(nums, index+2), helper(nums, index+1))
            memo[index] = val
            return val
        
        return helper(nums, 0)
