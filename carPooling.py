#Daily Jan 5
# Similart to Meeting Rooms 
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        list_of_rides = []
        for ppl, ridein, rideout in trips:
            list_of_rides.append((ridein, ppl))
            list_of_rides.append((rideout, -ppl))
        
        list_of_rides.sort()
        print(list_of_rides)
        
        for tm, ppl in list_of_rides:
            capacity -= ppl
            if capacity < 0:
                return False
        return True
        
                
                
