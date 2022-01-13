class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        from heapq import heappush, heappop, heapify
        points = sorted(points, key=lambda x: (x[0], x[1]))
        max_heap = []
        first = True
        num_arrows = 0
        print(points)
        for i, j in points:
            if first:
                heappush(max_heap, [j, i])
                num_arrows = 1
                first = False
            else:
                if ((max_heap[0][0]) >= i and max_heap[0][1]<= i):
                    val = heappop(max_heap)
                    heappush(max_heap, [min(j, val[0]), max(i, val[1])])
                else:
                    val = heappop(max_heap)
                    heappush(max_heap, [j, i])
                    num_arrows += 1

        return num_arrows
            
