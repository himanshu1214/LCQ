class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        def binary_search(nums):
            left, right = 0, len(nums)-1

            while left <= right:
                mid = (left + right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid +1
                elif nums[mid] > target:
                    right = mid -1
            return -1   
        
        if nums[0] < nums[-1]:
            return binary_search(nums)
        
        left, right = 0, len(nums)-1
        inflection_point = 0
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < nums[mid-1]:
                inflection_point = mid
                break  
            elif nums[mid] > nums[mid+1]:
                inflection_point = mid+1
                break
                
            elif nums[0] > nums[mid]:
                right = mid -1
            elif nums[0] < nums[mid]:
                left = mid + 1
                    
        print(inflection_point)
        
        if nums[0] == target:
            return 0
        elif nums[0] > target:
            nums = nums[inflection_point:]
            val = binary_search(nums)
            return -1 if val == -1 else val + inflection_point
        elif nums[0] < target:
            nums = nums[:inflection_point]
            val = binary_search(nums)
            return val
        
            
