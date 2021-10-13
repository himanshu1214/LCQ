class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        from heapq import heappush, heappop, heapify
        intervals.sort()
        intervals = [[i[0]*-1, i[1]] for i in intervals]
        max_heap = []
        heappush(max_heap, intervals[0])
        print(f"BRGINGIN: {max_heap}")
        for interval in intervals[1:]:
            val = heappop(max_heap)
            if val[1] - interval[0]*-1 >= 0:
                val[1] = max(val[1], interval[1])
                heappush(max_heap, val)
            else:
                heappush(max_heap, val)
                heappush(max_heap, interval)
            print(max_heap)
        lis = []
        while len(max_heap) > 0:
            pop = heappop(max_heap)
            lis.append([pop[0]*-1, pop[1]])
        return lis
            
            
        
