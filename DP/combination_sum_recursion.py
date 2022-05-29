class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def helper(nums, target):
            if target < 0:
                return -1
            if target == 0:
                return 1
            val = 0
            for num in nums:
                if target in memo:
                    return memo[target]
                tmp = helper(nums, target-num)
                if tmp != -1:
                    val += tmp
                
            memo[target] = val
            return val

        helper(nums, target)
        return memo[target]
