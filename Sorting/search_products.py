#Sol1
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        for i in range(len(searchWord)):
            match = searchWord[:i+1]
            j = 0
            tmp = []
            while len(tmp) < 3 and j < len(products):
                if products[j][:i+1] == match:
                    tmp.append(products[j])
                j += 1
            res.append(tmp[:])
        return res
      
 
# Sol2
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:        
        start,end = 0, len(products)-1
        index = 0
        products.sort()
        res = []
        while index < len(searchWord):
            while start <= end and (len(products[start]) <= index or products[start][index] != searchWord[index]):      
                    start += 1

            while start <= end and (len(products[end]) <= index or products[end][index] != searchWord[index]):
            
                end -= 1
            index += 1   
        
            res.append(products[start:min(end+1, start+3)])
        return res
