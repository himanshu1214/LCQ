from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        aux = []
        heapq.heapify(aux)
        for num in range(len(points)):
            point_x = points[num][0]
            point_y = points[num][1]
            # print(point_x, point_y)
            dist = sqrt(point_x**2 + point_y**2)
            heapq.heappush(aux, (dist, points[num]))
        return [heapq.heappop(aux)[1:][0] for i in range(k)]
    
  
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point1, point2 in points:
            sq = point1*point1 + point2*point2
            res.append((sq, [point1, point2]))
            
        res.sort()

        return [res[i][1] for i in range(k)]
