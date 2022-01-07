class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        from math import ceil
        start, end = 0, len(nums)-1
        target_set =  set()
        print(start, end)
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                target_set.add(mid)
                
                left = mid-1
                while (left >= 0 and nums[left] == target):
                    target_set.add(left)
                    left -= 1
                   

                right = mid + 1
                while (right < len(nums) and nums[right] == target):
                    target_set.add(right)
                    right += 1
                    
                print(target_set)
                return [min(target_set), max(target_set)] 
                                
            if nums[mid] < target:
                start = mid+1
                
            if nums[mid] > target:
                end = mid-1
        

        return [-1, -1]
        
