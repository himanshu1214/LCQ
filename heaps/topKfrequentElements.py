class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        hash_map = defaultdict(int)
        from heapq import heappush, heappop, heapify
        for i in nums:
            hash_map[i] += 1
            
            
        max_heap = []
        for m, v in hash_map.items():
            heappush(max_heap, (-v, m))
        
        res = []
        while max_heap:
            res.append(heappop(max_heap)[1])

        return  res[:k]
