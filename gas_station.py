# Greedy algo
# time O(n) and Spce O(1)

# We can ignore looking back for the starting point.
# since gas[i] + Delta(gas) this Delta(gas) can be zero or more from the prervious stn.
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        else:
            start = 0
            tdelta = 0
            for i in range(len(gas)):
                tdelta += gas[i] - cost[i]
                if tdelta < 0:
                    start = i+1
                    tdelta = 0
                
                    
            return start
