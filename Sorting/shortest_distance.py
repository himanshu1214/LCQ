class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        found, found_index = None, 0
        mindistance = len(wordsDict)-1
        for i in range(len(wordsDict)):
            if wordsDict[i] in [word1, word2]:
                if found != wordsDict[i] and found:
                    mindistance= min(mindistance, i-found_index)

                found, found_index = wordsDict[i], i
        return mindistance    
                    
