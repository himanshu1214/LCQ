class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        heapify(max_heap)
        for i in nums:
            heappush(max_heap, -1*i)

        j = 1    
        while j <=k-1:
            heappop(max_heap)
            j += 1
        return max_heap[0]*-1
