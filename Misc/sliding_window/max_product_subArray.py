class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        curr_max,  curr_min = 1, 1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                curr_max, curr_min = 1, 1
                continue
            tmp = nums[i] * curr_max
            curr_max = max(curr_max * nums[i], nums[i], curr_min * nums[i])
            curr_min = min(tmp, nums[i], curr_min * nums[i])

            res = max(res, curr_max)
            
        return res

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
