class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        tmp = []
        from collections import deque
        d = deque()
        l , r =0, 0
        output = []
        while r < len(nums):
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            d.append(r)    
            # this is for pop left element for keeping only valid elements
            if l > d[0]:
                d.popleft()
            
            # get the max value at every step
            if r+1 >= k:
                output.append(nums[d[0]])
                l += 1
                
            r += 1
        return output
