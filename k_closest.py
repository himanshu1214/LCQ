class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_list = []
        for x, y in points:
            dist = (x**2 + y**2)**0.5
            dist_list.append((dist, (x, y)))
            
        dist_list.sort()
        dist_list = [dist_list[i][1] for i in range(k)]
        return dist_list
