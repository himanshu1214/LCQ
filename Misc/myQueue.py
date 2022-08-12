from collections import deque
class MyQueue:

    def __init__(self):
        self.stack_one = deque()

    def push(self, x: int) -> None:
        self.stack_one.append(x)
        
    def pop(self) -> int:
        return self.stack_one.popleft()
        

    def peek(self) -> int:
        return self.stack_one[0]
    

    def empty(self) -> bool:
        return not bool(len(self.stack_one))
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
