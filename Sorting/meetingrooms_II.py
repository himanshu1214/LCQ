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
