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
