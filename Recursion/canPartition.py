class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total //2
        
        @lru_cache(maxsize=None)
        def helper(nums, index,target):
                        
            if target == 0:
                return True
            
            if index >= len(nums)-1:
                return False
            
            if target <0:
                return False

            
            index += 1
            # include number
            return helper(tuple(nums), index, target-nums[index]) or helper(tuple(nums), index, target)
            
        
        return helper(tuple(nums), 0, target)
