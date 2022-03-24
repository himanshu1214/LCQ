class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        from heapq import heapify, heappush, heappop
        c = Counter(s)
        
        print(c)
        min_heap = [(-v, k) for k, v in c.items()]
        heapify(min_heap)
        
        prev = None
        out = ""
        while min_heap or prev:
            # a -> 3 b -> 1
            # a -> 2 b-> 1
            # a -> 2 b -> 0
            # a -> 1 min_heap empty and prev non empty
            if prev and not min_heap:
                return ""
            
            v, k = heappop(min_heap)
            
            out += k
            v += 1

            
            if prev:
                heappush(min_heap, prev)
                prev = None

                            
            if v != 0:
                prev = (v, k)
                
        return out
