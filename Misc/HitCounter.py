class HitCounter:
    from collections import deque
    def __init__(self):
        self.add_timestamp = deque()

    def hit(self, timestamp: int) -> None:
        self.add_timestamp.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        pop_time = timestamp - 300
        print(pop_time)
        while True:
            if pop_time < 0:
                return len(self.add_timestamp)
            else:
                if  self.add_timestamp and self.add_timestamp[0] <= pop_time:
                    self.add_timestamp.popleft()
                else:
                    return len(self.add_timestamp)
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
