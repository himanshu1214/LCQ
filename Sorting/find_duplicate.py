class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        min_nums, max_nums = min(nums), max(nums)
        
        arr = [0 for i in range(max_nums + 1)]

        for i in nums:
            arr[i] += 1
            if arr[i] > 1:
                return i
