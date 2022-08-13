class MinStack:
    from heapq import heapify, heappush, heappop
  
    def __init__(self):
        self.stack = []
        self.min_heap = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        heappush(self.min_heap, val)
        return
    
    def pop(self) -> None:
        self.stack.pop()
        self.min_heap = self.stack.copy()
        heapify(self.min_heap)
        return 
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_heap[0] if self.min_heap else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
