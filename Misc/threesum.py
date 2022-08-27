class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict
        nums.sort()
        res = []
        for i in range(len(nums)):
            target = -nums[i]
            start = i +1
            end = len(nums) -1                
            while start < end:

                if (nums[start] + nums[end]) >  target:
                    end -= 1
                elif (nums[start] + nums[end]) <  target:
                    start += 1
                elif (nums[start] + nums[end]) ==  target:
                    res.append((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1      
        return list(set(res))
                
