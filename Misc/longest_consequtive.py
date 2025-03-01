# Brute force
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0 
        for num in nums:
            current_num = num
            current_streak = 1
            
            while current_num +1 in nums:
                current_num += 1
                current_streak += 1
                
            longest_streak = max(longest_streak, current_streak)
            
        return longest_streak


# Sorting

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        
        print(nums)
        current_streak = 1
        longest_streak = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] +1:
                current_streak += 1
            
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
        longest_streak = max(longest_streak, current_streak)          
        
        return longest_streak
