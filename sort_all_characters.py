import heapq

def sort_array(arr):
    
    min_heap = []
    heapq.heapify(min_heap)
    for i in arr:
        heapq.heappush(min_heap, [ord(i), i])
        
    return [heapq.heappop(min_heap)[1] for i in arr]
