#Similar to k closest points to origin


from math import sqrt
import heapq
def nearest_neighbours(p_x, p_y, k, n_points):
    # Write your code here
    min_dist_heap = []
    heapq.heapify(min_dist_heap)
    for row_num in range(len(n_points)):
        x, y = n_points[row_num][0], n_points[row_num][1]
        dist =  sqrt((p_x - n_points[row_num][0])**2 + (p_y - n_points[row_num][1])**2)
        heapq.heappush(min_dist_heap, [dist, (x, y)])
    return [heapq.heappop(min_dist_heap)[1] for i in range(k)]
    
