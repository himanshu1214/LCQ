class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals = [[1,3],[6,9]] 
        # newInterval = [2,5] 
        # [1, 3] [2, 5] [6, 9] --> [1, 5] [6, 9]
        
        # 2. intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        # [1, 2] [3, 5] [4, 8] [6, 7] [8, 10] [12, 16]
        # Overlap left only arr[i-1][1] > arr[i][0] < arr[i][0] and 
        # arr[i-1][1] > arr[i][0] < arr[i][0]
        STR = 0
        END = 1
        res = []
        start = 0
        while start < len(intervals) and intervals[start][STR] < newInterval[STR]:
            # add interval to res
            res.append(intervals[start])
            start +=1 
        
        # newinterval not overlapping
        if not res or res[-1][END] < newInterval[STR]:
            res.append(newInterval)
        else:
        # overlap
            res[-1][1] = max(res[-1][1], newInterval[1])

                
        while start < len(intervals):
            interval =  intervals[start]
            s, e = interval
            start += 1
            if res[-1][END] < s:
                res.append(interval)
            else:
                res[-1][END] = max(e, res[-1][END])
        return res
    
    
 class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        
        result = []
        i = 0
        while i < len(intervals):
            if not result:  
                result.append(intervals[i])
            elif result[-1][1] >= intervals[i][0]:
                end = max(result[-1][1], intervals[i][1])
                result[-1][1] = end
            else:
                result.append(intervals[i])
            i += 1
            
        return result
            
