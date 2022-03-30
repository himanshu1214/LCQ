class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = [0]
        for i in range(len(nums)):
            tmp = [0]
            _max = nums[i]
            _min = nums[i]
            for j in range(i, len(nums)):
                _max, _min = max(_max, nums[j]), min(_min, nums[j])
                val = _max - _min
                tmp[0] +=val
            res[0] += tmp[0]

        return res[0]
                
