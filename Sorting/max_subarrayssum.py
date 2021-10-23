class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_array = []
        array_sum = 0
        subarray = []
        for i in range(len(nums)):
            if not subarray:
                subarray.append(nums[i])
    
            elif nums[i] + subarray[-1]> nums[i]:
                val = subarray[-1] + nums[i]
                subarray.append(val)
                
            else:
                subarray.append(nums[i])
        print(subarray)
        return max(subarray)
