class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        if len(nums)== 1:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        while left < right:

            mid = (left + right)//2
            print(left, right, mid)
            if len(nums[left: right+1]) == 2:
                if nums[left] > nums[right]:
                    return left
                else:
                    return right
            elif ((nums[mid] > nums[mid+1]) and (nums[mid-1] < nums[mid])): # mid lies on ascending plane
                return mid
            elif nums[mid-1] > nums[mid]: # mid lies on descending plane meaning peak is on the left
                right = mid -1
            elif nums[mid] < nums[mid+1]: # mid lies on ascending plane meaning peak is on the right
                left = mid + 1

        mid = (left + right)//2
        return mid
