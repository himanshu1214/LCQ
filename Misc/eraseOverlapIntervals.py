class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        
        start = 0
        end = len(intervals)
        intervals.sort()
        tmp = []
        count = 0
        while start < end:
            if not tmp:
                tmp = intervals[start]
            elif tmp[1] > intervals[start][0]:
                #overlap
                count += 1
                mx = min(tmp[1], intervals[start][1])
                tmp[1] = mx
            else:
                tmp = intervals[start]
            start += 1
            
        return count
