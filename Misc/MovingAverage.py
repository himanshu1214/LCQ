class MovingAverage:
    from collections import deque
    def __init__(self, size: int):
        self.window = size
        self.num_list = deque()

    def next(self, val: int) -> float:

        self.num_list.append(val)
        if self.window >= len(self.num_list):
            return sum(self.num_list) / len(self.num_list)
        else:
            self.num_list.popleft()
            return sum(self.num_list) / self.window
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
