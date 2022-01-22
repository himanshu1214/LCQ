class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        startfl = 0
        startsl = 0
        final = []
        while startfl < len(firstList) and startsl < len(secondList):
            
            low = max(firstList[startfl][0], secondList[startsl][0])
            high = min(firstList[startfl][1], secondList[startsl][1])
            if low <= high:
                final.append([low, high])
            
            if firstList[startfl][1] > secondList[startsl][1]: # mv only that pointer fr the list which is less than the other 
                startsl += 1
            else:
                startfl += 1
                
        return final
