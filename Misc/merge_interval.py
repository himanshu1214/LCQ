class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start = 0
        end = len(intervals)
        res = []
        intervals.sort()  
 
        while start < end:
            if not res:
                # non overlapping
                res.append(intervals[start])
                
            elif res[-1][1] >= intervals[start][0]:
                print(res[-1][1], intervals[start][0])
                # overlapping
                res[-1][1] = max(res[-1][1], intervals[start][1])
            else:
                res.append(intervals[start])
            
            start += 1
        return res

 # sol2
 class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res
