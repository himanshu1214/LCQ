class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from heapq import heapify, heappush, heappop
        min_heap = []
        max_heap = []
        res = 0
        j = 0
        for i, val in enumerate(nums):
            heappush(min_heap, (-val, i))
            heappush(max_heap, (val, i))
            while -max_heap[0][0] - min_heap[0][0] > limit:
                j = min(min_heap[0][1], max_heap[0][1]) + 1
                while max_heap[0][1] < j:
                    heappop(max_heap)
                while min_heap[0][1] < j:
                    heappop(min_heap)
            

            res = max(res, i-j +1)
        return res
