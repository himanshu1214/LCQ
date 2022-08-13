class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
        mid = len(nums)//2
        res = {}
        for i in range(len(nums)):
            if str(nums[i]) not in res:
                res[str(nums[i])] = 1
            else:
                res[str(nums[i])] += 1
            
        _sort = [v[0] for v in sorted(res.items(), key=lambda kv: (kv[1], kv[0]))]

        return _sort[-1]
