class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1]> intervals[i+1][0]:
                return False
        return True

# Try2:
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        start = 1
        end = len(intervals)
        
        if len(intervals) == 1:
            return True
        
        intervals.sort()
        while start < end:
            if intervals[start-1][1] > intervals[start][0]:
                return False
            start +=1   
        return True
                
