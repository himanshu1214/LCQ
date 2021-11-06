class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
         
        ind = 0
        res = 0
        while ind < len(nums):
            if target > nums[ind]:
                res += 1
            ind +=1
        return res
