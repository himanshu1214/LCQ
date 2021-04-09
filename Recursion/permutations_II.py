class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        def helper(nums, ind, slate):
            if ind >= len(nums):
                copy_ = slate[:]
                if copy_ not in result:
                    result.append(slate[:])
                return 
            else:
                for j in range(ind, len(nums)):
                    nums[j], nums[ind] = nums[ind], nums[j] 
                    slate.append(nums[ind])
                    helper(nums, ind+1, slate)
                    slate.pop()
                    nums[j], nums[ind] = nums[ind], nums[j] 
                # print(slate)

        helper(nums, 0, [])
        return result
