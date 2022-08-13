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



class MinStack:
    from heapq import heapify, heappush, heappop
  
    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return 
        curr_min_val = self.stack[-1][1]
        self.stack.append((val, min(curr_min_val, val)))

    
    def pop(self) -> None:
        self.stack.pop()
        return 
    
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

class MinStack:
    from heapq import heapify, heappush, heappop
  
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
    
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        
    
    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            self.stack.pop()
            self.min_stack.pop()
        else:
            self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.min_stack)
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
