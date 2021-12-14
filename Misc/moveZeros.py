class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, 0
        while end < len(nums):
            if nums[end] == 0:
                end += 1
            else:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
                start += 1
                end += 1
        return nums
