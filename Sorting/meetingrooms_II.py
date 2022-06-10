from collections import defaultdict
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        rooms = 0

        min_heap=[]
        intervals.sort(key= lambda x: x[0])

        dict_ = defaultdict(int)
        for i in intervals:
            dict_[i[0]] += 1
            dict_[i[1]] -= 1


        dict_keys = list(dict_.keys())
        dict_keys.sort()


        curr_rooms = 0
        for i in dict_keys:
            curr_rooms +=  dict_[i]
            if rooms  < curr_rooms:
                rooms = curr_rooms
            print(f"indx: {i}, max rooms : {rooms}, curr_rooms in use : {curr_rooms}")
        return rooms

    
    class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1
        from heapq import heappush, heappop
        start = 0
        end = len(intervals)
        
        tmp = []
        intervals.sort()
        count = 0 
        min_heap = []
        heapify(min_heap)
        while start < end:
            if not min_heap:
                fir, sec = intervals[start]
                heappush(min_heap, [sec, fir])
                
            else:
                
                if min_heap[0][0] <= intervals[start][0]:
                    # FREE
                    min_el = heappop(min_heap)

                    min_el[0] = intervals[start][1]
                    heappush(min_heap, min_el)

                else:
                    # NOT FREE
                    fir, sec = intervals[start]
                    heappush(min_heap, [sec, fir])
            start += 1

        return len(min_heap)
                
            
