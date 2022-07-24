class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = nums[0]
        tmp = nums[0]
        curr_max, curr_min =  nums[0], nums[0]
        for i in range(1, len(nums)):
            
            tmp = curr_max*nums[i]
            
            curr_max = max(tmp, nums[i], curr_min*nums[i])
            
            curr_min = min(tmp, nums[i], curr_min*nums[i])
            
            
            prod = max(curr_max, prod)
                
        return prod
