class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        set_nums = set(nums)
        seq = {}
        for i in range(len(nums)):
            if nums[i] - 1 not in set_nums:
                seq[nums[i]] = 1
                tmp  = nums[i] + 1
                while tmp in set_nums:
                    seq[nums[i]] += 1
                    tmp += 1
                    
        return sorted(seq.items(), key=lambda item: item[1])[-1][1]
        
