class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = float("-inf")
        tmp_val = float("-inf")
        for i in range(len(nums)):
            if tmp_val + nums[i] < nums[i]:
                tmp_val = nums[i]
                   
            else:
                tmp_val += nums[i]
            
            if tmp_val > max_val :
                max_val = tmp_val

        return max_val
