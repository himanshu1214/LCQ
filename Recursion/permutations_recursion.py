class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        def helper(nums, ind, slate):
            if ind >= len(nums):
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
    
#Space Complexity:
# Input + Aux + Outpu
# O(n) + O(n) + O(n!*n) ~ (Total number of leaves * size of leave)

#Time Complexity
# Work by end leaves and internal node worker
# Total leaves* work by each leave worker to copy in external bag + (50% the number of leaves*1)
# ~O(n!*n)

