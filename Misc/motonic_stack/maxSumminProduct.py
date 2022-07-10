class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = 0
        prefix = [0]
        st = []
        for i in nums:
            prefix.append(prefix[-1]+ i)
            
        for i, val in enumerate(nums):
            newStart = i
            while st and st[-1][1] > val:
                start, new_val = st.pop()
                total = new_val * (prefix[i] - prefix[start])
                res = max(res, total)
                newStart = start
                
            st.append((newStart, val))
            
        for start, val in st:
            total = val * (prefix[len(nums)] - prefix[start]) 
            res = max(res, total)
            
        return res % (10**9+7)
