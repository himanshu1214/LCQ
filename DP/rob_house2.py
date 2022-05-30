class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = {}
        def helper(nums, index):
            if index > len(nums)-1 :
                return 0
            if index in memo:
                return memo[index]
            val = max(nums[index] + helper(nums, index + 2), helper(nums, index+1))
            memo[index] = val
            return val
        
        val1 = helper(nums[:-1], 0)
        memo = {}
        val2 = helper(nums[1:], 0)
        
        val_max = max(val1, val2)
        
        return val_max
