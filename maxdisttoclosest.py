class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # ==> go right
        distance = [None for i in range(len(seats))]
        val =0
        pre = 0   
        for i in range(len(seats)):
            if seats[i] == 1:
                distance[i] = 0
                val = 0
                pre = 1
            else:
                if pre == 0:
                    val = len(distance)
                    distance[i] = val
                else:
                    val += 1
                    distance[i] = val
                
        val = 0
        pre = 0
        for j in range(len(seats)-1, -1, -1):
            if seats[j] == 1:
                val = 0
                distance[j] = 0
                pre = 1
            else:
                if pre == 0:
                    val = len(distance) + 100
                    distance[j] = min(distance[j], val)
                else:
                    val += 1
                    distance[j] = min(distance[j], val)
            
        return max(distance)
    
            
        
        # ==> go left
