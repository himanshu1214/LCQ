class Solution:
    def findMin(self, nums: List[int]) -> int:
#         2 3 4 5 6 7
#         4 5 6 7 2 3
        if nums[0] < nums[-1]:
            return nums[0]
        
                
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            
            if nums[mid] > nums[mid + 1] :
                return nums[mid + 1]
            elif nums[mid] < nums[mid-1]:
                return nums[mid]
            
            elif nums[mid] < nums[0]: # see right
                right = mid -1
            elif nums[mid] > nums[0]: # see left
                left = mid + 1
         

                
                
