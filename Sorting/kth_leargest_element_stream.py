import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for i in range(len(nums)):
            heapq.heappush(self.min_heap, nums[i])
        i = 0
        n = len(self.min_heap)
        for i in range(n-k):
            heapq.heappop(self.min_heap)
            i += 1
    def add(self, val: int) -> int:
        if not self.min_heap:
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) < self.k :
            heapq.heappush(self.min_heap, val)
        else:
            heapq.heappush(self.min_heap, val)
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
