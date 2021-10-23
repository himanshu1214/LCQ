class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        ct =0 
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            
        return False
